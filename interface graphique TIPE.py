from tkinter import *
from tkinter.filedialog import *
from Algorithme import *
from PIL import ImageTk
import pickle

# ============== Classes de Type de fenêtres ==============

class CiblanteDeDonnees(Toplevel):
	def __init__(self, données, function, multiple = True):
		super().__init__()
		
		self.geometry('300x300')
		self.title("Ciblante")
		
		n = len(données)
		V = [IntVar() for i in range(n)]
		
		if multiple:
			L = [Checkbutton(self, text=données[i], variable = V[i], onvalue=1, offvalue=0) for i in range(n)]
		else:
			cible = StringVar()
			L = [ Radiobutton(self, text=données[i], variable=cible, value=données[i]) for i in range(n) ]
		
		for box in L:
			box.pack()
		
		def recupCibles():
			if multiple:
				Cibles = [ données[i] for i in range(n) if V[i].get() == 1 ]
			else:
				if '->' in cible.get():
					Cibles = [ cible.get().split('->')[:2] ]
				else:
					Cibles = [ cible.get() ]
			
			for a in Cibles:
				function(a)
				
			self.destroy()

		Button(self, text="Valider", command=recupCibles).pack(side = BOTTOM)
		
class LianteDeDonnees(Toplevel):
	def __init__(self, données, function):
		super().__init__()
		
		self.geometry('600x300')
		self.title("Liante")
		
		n = len(données)	
		frame1 = LabelFrame(self, text="départ")
		frame1.pack(side = LEFT)
		frame2 = LabelFrame(self, text="arrivées")
		frame2.pack(side = RIGHT)

		cible1 = StringVar()
		cible2 = StringVar()
		L1 = [ Radiobutton(frame1, text=données[i], variable=cible1, value=données[i]) for i in range(n) ]
		L2 = [ Radiobutton(frame2, text=données[i], variable=cible2, value=données[i]) for i in range(n) ]

		for k in range(n):
			L1[k].pack()
			L2[k].pack()
		
		def recupCibles():
			function(cible1.get(), cible2.get())
			self.destroy()

		Button(self, text="Valider", command=recupCibles).pack(side = BOTTOM)

# ============ Quelques fonctions auxiliaires =============

def clear_graph():
	G.effacer()

def parser(filename):
	fichier = open(filename,'r')
	LIGNES = []
	for ligne in fichier:
		if ligne[0] == "[":
			LIGNES.append([])
		else:
			LIGNES[-1].append(ligne.rstrip('\n'))
	return LIGNES

def import_ligne():
	LIGNES = parser(askopenfilename(filetypes=[("Texte","*.txt"),("Tableau","*.csv"),("JSON","*.json")]))
	
	for ligne in LIGNES:
		for station in ligne:
			G.ajouter_sommet(station)
		
		for k in range(len(ligne)-1):
			rp = G.randomPoids()
			G.ajouter_arc(ligne[k],ligne[k+1],rp)
			G.ajouter_arc(ligne[k+1],ligne[k],rp)
				
def save_graph():
	filename = asksaveasfilename(filetypes=[("Binary Graph","*.gbin")])
	outfile = open(filename, 'wb')
	pickle.dump(G, outfile)
	outfile.close()

def import_graph():
	global G
	filename = askopenfilename(filetypes=[("Binary Graph","*.gbin")])
	infile = open(filename,'rb')
	G = pickle.load(infile)
	infile.close()
	
def define_poids_statique(A,B, stochastique = True):
	fenetre = Toplevel()
	fenetre.geometry('600x600')
	if stochastique:
		Label(fenetre, text="Combien d'issues possibles ? ").pack()
		s = Spinbox(fenetre, from_=0, to=10)
		s.pack()

		def creerstochastique(window,nb):
			window.destroy()
			fenetre = Toplevel()
			fenetre.geometry('600x600')
			valeurs = LabelFrame(fenetre, text="valeurs")
			valeurs.pack(fill="y", expand="no", side = LEFT)
			probas = LabelFrame(fenetre, text="probas")
			probas.pack(fill="y", expand="no", side = RIGHT)
			plist = [Spinbox(probas, from_=0, to=1, increment=0.1) for k in range(nb)]
			clist = [Spinbox(valeurs, from_=0, to=10) for k in range(nb)]
			for k in range(nb):
				plist[k].pack()
				clist[k].pack()
			
			def rentrerPSS():
				valeurs = [int(spinbox.get()) for spinbox in clist]
				probas = [float(spinbox.get()) for spinbox in plist]
				
				if sum(probas) != 1.0 :
					raise Exception("Désolé, ce n'est pas une distribution de probabilité")
				
				G.ajouter_arc(A,B,PSS(zip(valeurs,probas)))
				fenetre.destroy()
			
			Button(fenetre, text="Valider",command = rentrerPSS).pack()

		Button(fenetre, text="Valider", command= lambda : creerstochastique(fenetre, int(s.get()))).pack()
	else:
		Label(fenetre, text="Valeur du poids deterministe statique ? ").pack()
		s = Spinbox(fenetre, from_=0, to=10)
		s.pack()
		def rentrerPoids():
			G.ajouter_arc(A,B,Poids(int(s.get())))
			fenetre.destroy()
		Button(fenetre, text="Valider", command=rentrerPoids).pack()

def define_poids_dynamique(cycle, periode, stochastique = True):
	fenetre = Toplevel()
	fenetre.geometry('600x600')
	elements = cycle // periode

	if stochastique:
		def creerstochastique(nb):
			fenetre = Toplevel()
			fenetre.geometry('600x600')
			valeurs = LabelFrame(fenetre, text="valeurs")
			valeurs.pack(fill="y", expand="no", side = LEFT)
			probas = LabelFrame(fenetre, text="probas")
			probas.pack(fill="y", expand="no", side = RIGHT)
			for k in range(nb):
				Spinbox(probas, from_=0, to=1, increment=0.1).pack()
				Spinbox(valeurs, from_=0, to=10).pack()
			Button(fenetre, text="Valider").pack()

		for k in range(elements):
			Label(fenetre, text="Combien d'issues possibles pour la {}e periode ? ".format(k+1)).pack()
			s = Spinbox(fenetre, from_=0, to=10)
			s.pack()
			Button(fenetre, text="Valider", command= lambda : creerstochastique(int(s.get()))).pack()

	else:
		for k in range(elements):
			Label(fenetre, text="Valeur du poids sur la {}e periode ? ".format(k+1)).pack()
			Spinbox(fenetre, from_=0, to=10).pack()

		Button(fenetre, text="Valider").pack()

def setPoids(A,B):
	if not (A in G and B in G):
		raise Exception("Désolé, cet arc ne peut être construit")
	
	# on supprimer l'arc qui va être modifié (s'il existe déjà)
	for a in G.arcs:
		if a.origine == A and a.destination == B:
			G.supprimer_arc(a)
	
	if typeGraphe == 'DS':
		define_poids_statique(A,B,False)
	elif typeGraphe == 'DD':
		define_poids_dynamique(cycle,periode,False)
	elif typeGraphe == 'SD':
		define_poids_dynamique(cycle,periode)
	else: # typeGraphe == 'SS':
		define_poids_statique(A,B,True)

def setName(sommet):
	fenetre = Toplevel()
	fenetre.geometry('300x300')
	Label(fenetre, text="Nouveau nom : ").pack()
	nouveauNom = Entry(fenetre)
	nouveauNom.pack()
	def modifiersommetdugraphe():
		G.modifier_sommet(sommet, nouveauNom.get())
		fenetre.destroy()

	Button(fenetre, text="valider", command = modifiersommetdugraphe).pack()

def afficherpcc(A,B,frame):
	for widget in frame.winfo_children():
		widget.destroy()
	
	Visualiser(A,B,G,modeApercu.get(), engine_render.get())
	
	photo = ImageTk.PhotoImage(file="Graphe.gv.png")
	canv = Canvas(frame, width=1000, height=600, scrollregion=(0, 0, photo.width(), photo.height()))

	defilY = Scrollbar(frame, orient='vertical',command=canv.yview)
	defilY.grid(row=0, column=1, sticky='ns')

	defilX = Scrollbar(frame, orient='horizontal',command=canv.xview)
	defilX.grid(row=1, column=0, sticky='ew')

	canv['xscrollcommand'] = defilX.set
	canv['yscrollcommand'] = defilY.set
	canv.create_image(0, 0, anchor=NW, image=photo)
	canv.image = photo
	
	canv.grid(row=0, column=0)

def previsualiser(frame):
	for widget in frame.winfo_children():
		widget.destroy()

	G.Visualisation(modeApercu.get(),engine_render.get())
	photo = ImageTk.PhotoImage(file="Graphe.gv.png")
	canv = Canvas(frame, width=1100, height=600, scrollregion=(0, 0, photo.width(), photo.height()))

	defilY = Scrollbar(frame, orient='vertical',command=canv.yview)
	defilY.grid(row=0, column=1, sticky='ns')

	defilX = Scrollbar(frame, orient='horizontal',command=canv.xview)
	defilX.grid(row=1, column=0, sticky='ew')

	canv['xscrollcommand'] = defilX.set
	canv['yscrollcommand'] = defilY.set
	canv.create_image(0, 0, anchor=NW, image=photo)
	canv.image = photo
	
	canv.grid(row=0, column=0)

# ======================== GUI =============================

def FenetreMode():
    # Choix du type de graphe
    
	fenetre = Tk()
	fenetre.geometry('500x500')
	
	MODE = LabelFrame(fenetre, text="Mode")
	MODE.pack(side = LEFT)
	mode = StringVar()
	Radiobutton(MODE, text="Ferroviaire",variable = mode, value="Ferroviaire").pack()
	Radiobutton(MODE, text="Routier",variable = mode, value="Routier").pack()
    
	TYPEGRAPHE = LabelFrame(fenetre, text="Type de Graphe")
	TYPEGRAPHE.pack(side = RIGHT)
	typeGraphe = StringVar()
	Radiobutton(TYPEGRAPHE, text="Déterministe Statique",variable = typeGraphe, value="DS").pack()
	Radiobutton(TYPEGRAPHE, text="Stochastique Statique",variable = typeGraphe, value="SS").pack()
	Radiobutton(TYPEGRAPHE, text="Déterministe Dynamique",variable = typeGraphe, value="DD").pack()
	Radiobutton(TYPEGRAPHE, text="Stochastique Dynamique",variable = typeGraphe, value="SD").pack()
	

	#Valider
	def Valider():
		if (mode.get() == "" or typeGraphe.get() == ""):
			raise Exception("Désolé, il manque quelque chose")
		fenetre.destroy()
		FenetreCréation(mode.get(), typeGraphe.get())
		
	
	Button(fenetre, text="Valider", command = Valider).pack(side = BOTTOM)

def FenetreCréation(mode, GrapheType):
	
	global typeGraphe, modeApercu, engine_render, G
	
	typeGraphe = GrapheType
	
	
	fenetre = Tk()
	fenetre.geometry('1000x600')
	fenetre.title("mode : {} avec un type de graphe : {} ".format(mode,typeGraphe))
	
	modeApercu = StringVar()
	engine_render = IntVar()
	
	if typeGraphe == 'DS':
		G = Graphe([],[],Poids)
	elif typeGraphe == 'SS':
		G = Graphe([],[],PSS)
	elif typeGraphe == 'DD':
		G = Graphe([],[],PDD)
	else :
		G = Graphe([],[],PSD)
		
	def reveniraumenu():
		fenetre.destroy()
		FenetreMode()
	
	# Menu
	menubar = Menu(fenetre)

	menu1 = Menu(menubar, tearoff=0)
	menu1.add_command(label="Créer")
	menu1.add_command(label="Importer", command= import_graph)
	menu1.add_command(label="Exporter")
	menu1.add_command(label="Sauvegarder", command=save_graph)
	menu1.add_separator()
	menu1.add_command(label="Revenir au menu", command=reveniraumenu)
	menubar.add_cascade(label="Fichier", menu=menu1)

	menu2 = Menu(menubar, tearoff=0)
	menu2.add_command(label="Couper")
	menu2.add_command(label="Copier")
	menu2.add_command(label="Coller")
	menu2.add_command(label="Effacer", command=clear_graph)
	menubar.add_cascade(label="Edition", menu=menu2)

	menu3 = Menu(menubar, tearoff=0)
	menu3.add_command(label="A propos")
	menubar.add_cascade(label="Aide", menu=menu3)

	fenetre.config(menu=menubar)
	
	# ajout/suppression/modications des noeuds,arcs,poids

	def ajoutNoeuds(modeLigne = False):
		if modeLigne and mode != "Ferroviaire":
			return None
		def rentrerNoeuds(window, nb):
			window.destroy()
			def ajouterlesnoeudsaugraphe(window, entrees):
				for e in entrees:
					G.ajouter_sommet(e.get())
				if modeLigne :
					for k in range(len(G.sommets)-1, len(G.sommets) - nb, -1):
						G.ajouter_arc(G[k],G[k-1],G.randomPoids())
				
				window.destroy()

			fenetre = Tk()
			fenetre.geometry('300x300')
			LesEntrées = []
			for k in range(nb):
				Label(fenetre, text="Noeud n°{}".format(k+1), bg="yellow").pack()
				LesEntrées.append( Entry(fenetre, width=30) )
				LesEntrées[-1].pack()

			Button(fenetre,text="Valider",command = lambda : ajouterlesnoeudsaugraphe(fenetre,LesEntrées)).pack()

		fenetre = Tk()
		fenetre.geometry('500x500')
		nb_noeuds = Label(fenetre, text="Combien de noeuds souhaitez-vous ajouter dans le graphe ?")
		nb_noeuds.place(x = 30 , y = 140)

		ligne_noeuds = Spinbox(fenetre, from_=0, to=30)
		ligne_noeuds.place(x = 0 , y = 0)
		Button(fenetre, text="choisir", command= lambda : rentrerNoeuds(fenetre, int(ligne_noeuds.get()))).pack()
		fenetre.mainloop()
			
	def supprimeNoeuds(listeDesNoeuds):
		CiblanteDeDonnees(listeDesNoeuds, G.supprimer_sommet).mainloop()

	def ajoutArcs(listeDesNoeuds):
		LianteDeDonnees(listeDesNoeuds, setPoids).mainloop()

	def supprimeArcs(listeDesArcs):
		CiblanteDeDonnees(listeDesArcs, G.supprimer_arc).mainloop()

	def modifier(listeDesNoeuds,listeDesArcs):
		def changeSommet(listeDesNoeuds):
			CiblanteDeDonnees(listeDesNoeuds,setName,False).mainloop()

		def changePoidsArc(listeDesArcs):
			CiblanteDeDonnees(listeDesArcs,lambda arcchangé : setPoids(arcchangé[0],arcchangé[1]) ,False).mainloop()

		# menu des modifications
		fenetre = Tk()
		fenetre.geometry('300x300')
		Button(fenetre, text="Modifier un sommet", command = lambda : changeSommet(listeDesNoeuds)).pack()
		Button(fenetre, text="Modifier la valeur d'un poids d'un arc", command = lambda : changePoidsArc(listeDesArcs)).pack()
		fenetre.mainloop()
	
	# PCC
	
	def pcc(frame):
		LianteDeDonnees(G.sommets, (lambda x, y : afficherpcc(x,y,frame) )).mainloop()
	
	# Cadres d'édition et aperçu du graphe

	editeur = LabelFrame(fenetre, text="Editeur", padx=20, pady=20)
	editeur.pack(fill="y", expand="no", side = LEFT)
	apercu = LabelFrame(fenetre, text="Aperçu", padx=20, pady=20)
	apercu.pack(fill="both", expand=True, side = RIGHT)
	
	Button(editeur, text="Ajouter noeuds", bg = "green" , fg = "black", command = ajoutNoeuds).pack()
	Button(editeur, text="Supprimer noeuds", bg = "green" , fg = "black", command = lambda : supprimeNoeuds(G.sommets) ).pack()
	Button(editeur, text="Ajouter arcs", bg = "green" , fg = "black", command = lambda : ajoutArcs(G.sommets)).pack()
	Button(editeur, text="Supprimer arcs", bg = "green" , fg = "black", command = lambda : supprimeArcs(G.arcs)).pack()
	Button(editeur, text="Modifications", bg = "green" , fg = "black", command = lambda : modifier(G.sommets,G.arcs) ).pack()
	Button(editeur, text="PCC", bg = "red" , fg = "white", command = lambda: pcc(apercu)).pack(side = BOTTOM)
	Button(editeur, text="Aperçu", bg = "blue" , fg = "white", command = lambda : previsualiser(apercu) ).pack(side = BOTTOM)
	Button(editeur, text="Créer ligne", bg = "green" , fg = "black", command = lambda : ajoutNoeuds(True)).pack()
	Button(editeur, text="Importer ligne", bg = "green" , fg = "black", command = import_ligne).pack()
	
	engineLabel = LabelFrame(editeur, text = "engine render")
	engineLabel.pack(side = TOP)
	L = [ Radiobutton(engineLabel, text=roadmap[i] ,variable = engine_render, value=i) for i in range(len(roadmap)) ]
	for rb in L:
		rb.pack()
	
	# Cas des graphes Dynamiques

	if typeGraphe[-1] == 'D':
		parametresDynamique = Toplevel()
		parametresDynamique.geometry('400x400')
		Label(parametresDynamique,text = " Définir la durée d'une période ", bg = "black" , fg = "white").pack()
		periodeEntree = Entry(parametresDynamique)
		periodeEntree.pack()
		Label(parametresDynamique,text = " Définir le nombre de période ", bg = "black" , fg = "white").pack()
		nbdeperiodeEntree = Entry(parametresDynamique)
		nbdeperiodeEntree.pack()
		def recupererParametreDynamique():
			global periode, cycle
			periode = int(periodeEntree.get())
			cycle = periode * int(nbdeperiodeEntree.get())
			parametresDynamique.destroy()
			Label(editeur, text = "Dynamique settings : \nPeriode {} u.t / Cycle {} u.t".format(periode,cycle)).pack()
		Button(parametresDynamique, text = "valider", command=recupererParametreDynamique).pack()

	# Cas des graphes Statiques Stochastiques
	
	if typeGraphe == 'SS':
		modeApercuLabel = LabelFrame(editeur, text = "mode Apercu")
		modeApercuLabel.pack(side = TOP)
		Radiobutton(modeApercuLabel, text="Mode détail", variable = modeApercu, value="detail").pack()
		Radiobutton(modeApercuLabel, text="Mode moyenne", variable = modeApercu, value="moyenne").pack()
		Radiobutton(modeApercuLabel, text="Mode fiabilité", variable = modeApercu, value="fiabilite").pack()
	
	fenetre.mainloop()

# =========== Phase de tests ============

FenetreMode()
