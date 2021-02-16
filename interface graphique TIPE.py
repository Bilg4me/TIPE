from tkinter import *
from Algorithme import *
from PIL import ImageTk

# Graphe

G = Graphe([],[],Poids)

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
			for k in range(nb):
				Spinbox(probas, from_=0, to=1, increment=0.1).pack()
				Spinbox(valeurs, from_=0, to=10).pack()
			Button(fenetre, text="Valider").pack()

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

def setPoids(window, A,B):
	
	if not (A in G and B in G):
		raise Exception("Désolé, cet arc ne peut être construit")
	
	if typeGraphe == 'DS':
		define_poids_statique(A,B,False)
	elif typeGraphe == 'DD':
		define_poids_dynamique(cycle,periode, False)
	elif typeGraphe == 'SD':
		define_poids_dynamique(cycle,periode)
	else: # typeGraphe == 'SS':
		define_poids_statique()
		
		
	
	window.destroy()

def setName(window, sommet):
	window.destroy()
	fenetre = Toplevel()
	fenetre.geometry('300x300')
	Label(fenetre, text="Nouveau nom : ").pack()
	nouveauNom = Entry(fenetre)
	nouveauNom.pack()
	def modifiersommetdugraphe():
		G.modifier_sommet(sommet.get(), nouveauNom.get())
		fenetre.destroy()

	Button(fenetre, text="valider", command = modifiersommetdugraphe).pack()

def FenetreMode():
	fenetre = Tk()
	fenetre.geometry('800x600')
	Button(fenetre, text="Routier", bg = "green" , fg = "black", command = lambda : FenetreTypeGraphe("Routier", fenetre)).pack(side=TOP, padx=5, pady=5)
	Button(fenetre, text="Ferro", bg = "green" , fg = "black", command = lambda : FenetreTypeGraphe("Ferro", fenetre)).pack(side=BOTTOM, padx=5, pady=5)
	fenetre.mainloop()

def FenetreTypeGraphe(mode, window):
    #Choix du type de graphe
    window.destroy()
    fenetre = Tk()
    fenetre.geometry('800x600')
    var_choix = StringVar()

    choix_DS = Radiobutton(fenetre, text="Déterministe Statique", bg = "violet", variable = var_choix, value="DS")
    choix_SS = Radiobutton(fenetre, text="Stochastique Statique", bg = "violet", variable = var_choix, value="SS")
    choix_DD = Radiobutton(fenetre, text="Déterministe Dynamique", bg = "violet", variable = var_choix, value="DD")
    choix_SD = Radiobutton(fenetre, text="Stochastique Dynamique", bg = "violet", variable = var_choix, value="SD")

    TitreChoix = Label(fenetre,text = "Choisissez le type de modélisation : en mode " + mode , relief=RAISED , bg = "black" , fg = "white")

    TitreChoix.place(x = 0, y = 5)
    choix_DS.place(x = 0 , y = 25)
    choix_SS.place(x = 0 , y = 45)
    choix_DD.place(x = 0 , y = 65)
    choix_SD.place(x = 0 , y = 85)

    #Valider
    def Valider():
        fenetre.destroy()
        FenetreModelisation(mode, var_choix.get())

    bouton_valider = Button(fenetre, text="Valider", bg = "green" , fg = "black", command = Valider)
    bouton_valider.place(x = 150 , y = 180)

def FenetreModelisation(mode, typedeGraphe):
	fenetre = Tk()
	fenetre.geometry('800x600')
	global typeGraphe
	typeGraphe = typedeGraphe
	
	def alert():
		return None
	
	# Menu
	menubar = Menu(fenetre)

	menu1 = Menu(menubar, tearoff=0)
	menu1.add_command(label="Créer", command=alert)
	menu1.add_command(label="Importer", command=alert)
	menu1.add_command(label="Exporter", command=alert)
	menu1.add_command(label="Sauvegarder", command=alert)
	menu1.add_separator()
	menu1.add_command(label="Quitter", command=fenetre.quit)
	menubar.add_cascade(label="Fichier", menu=menu1)

	menu2 = Menu(menubar, tearoff=0)
	menu2.add_command(label="Couper", command=alert)
	menu2.add_command(label="Copier", command=alert)
	menu2.add_command(label="Coller", command=alert)
	menubar.add_cascade(label="Edition", menu=menu2)

	menu3 = Menu(menubar, tearoff=0)
	menu3.add_command(label="A propos", command=alert)
	menubar.add_cascade(label="Aide", menu=menu3)

	fenetre.config(menu=menubar)

	# previsualisation du graphe

	def previsualiser(frame):
		for widget in frame.winfo_children():
			widget.destroy()
		
		G.Visualisation()
		photo = ImageTk.PhotoImage(file="Graphe.gv.png")
		canvas = Canvas(apercu,width=100, height=500)
		canvas.create_image(0, 0, anchor=NW, image=photo)
		canvas.image = photo
		canvas.pack(fill="both", expand=True)
	
	def pcc(frame):
		n = len(G.sommets)
		fenetre = Toplevel()
		fenetre.geometry('300x300')

		cadresDesDéparts = LabelFrame(fenetre, text="depart")
		cadresDesDéparts.pack(side = LEFT)

		depart = StringVar()
		pointsdeparts = [ Radiobutton(cadresDesDéparts, text=G[i], variable=depart, value=G[i]) for i in range(n) ]
		for rb in pointsdeparts:
			rb.pack()

		cadresDesArrives = LabelFrame(fenetre, text="arrive")
		cadresDesArrives.pack(side = RIGHT)

		arrive = StringVar()
		pointsarrives = [ Radiobutton(cadresDesArrives, text=G[i], variable=arrive, value=G[i]) for i in range(n) ]
		for rb in pointsarrives:
			rb.pack()

		Button(fenetre, text="Calculer le PCC", command = lambda : afficherpcc(depart.get(), arrive.get(),G,frame)).pack()

		fenetre.mainloop()
	
	def afficherpcc(A,B,G,frame):
		for widget in frame.winfo_children():
			widget.destroy()
		
		Visualiser(A,B,G)
		photo = ImageTk.PhotoImage(file="Graphe.gv.png")
		canvas = Canvas(apercu,width=100, height=500)
		canvas.create_image(0, 0, anchor=NW, image=photo)
		canvas.image = photo
		canvas.pack(fill="both", expand=True)

	# ajout/suppression de noeuds et arc

	def ajoutNoeuds(modeLigne = False):
		def rentrerNoeuds(window, nb):
			window.destroy()
			def ajouterlesnoeudsaugraphe(window, entrees):
				for e in entrees:
					G.ajouter_sommet(e.get())
				if modeLigne :
					for k in range(len(G.sommets)-1, len(G.sommets) - nb, -1):
						G.ajouter_arc(G[k],G[k-1],Poids(1))
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
		fenetre = Toplevel()
		# askip le probleme venait du fait qu'on ne peux cumuler plusieurs instance de Tk() donc pour le résoudre on utilise un toplevel
		fenetre.geometry('300x300')
		n = len(listeDesNoeuds)
		V = [IntVar() for i in range(n)]
		L = [Checkbutton(fenetre, text=str(listeDesNoeuds[i]), variable = V[i], onvalue=1, offvalue=0) for i in range(n)]
		for cb in L:
			cb.pack()
		def recupNonVoulus():
			NonVoulus = [ G[i] for i in range(n) if V[i].get() == 1 ]
			for s in NonVoulus:
				G.supprimer_sommet(s)
			fenetre.destroy()

		Button(fenetre, text="Supprimer", bg = "red" , fg = "white", command = recupNonVoulus).pack(side = BOTTOM)
		fenetre.mainloop()

	# Ajouts, suppression arcs

	def ajoutArcs(listeDesNoeuds):
		n = len(listeDesNoeuds)
		fenetre = Toplevel()
		fenetre.geometry('300x300')

		cadresDesDéparts = LabelFrame(fenetre, text="depart")
		cadresDesDéparts.pack(side = LEFT)

		depart = StringVar()
		pointsdeparts = [ Radiobutton(cadresDesDéparts, text=G[i], variable=depart, value=G[i]) for i in range(n) ]
		for rb in pointsdeparts:
			rb.pack()

		cadresDesArrives = LabelFrame(fenetre, text="arrive")
		cadresDesArrives.pack(side = RIGHT)

		arrive = StringVar()
		pointsarrives = [ Radiobutton(cadresDesArrives, text=G[i], variable=arrive, value=G[i]) for i in range(n) ]
		for rb in pointsarrives:
			rb.pack()

		Button(fenetre, text="Set poids", command= lambda : setPoids(fenetre, depart.get(), arrive.get())).pack()

		fenetre.mainloop()

	def supprimeArcs(listeDesArcs):
		fenetre = Toplevel()
		# askip le probleme venait du fait qu'on ne peux cumuler plusieurs instance de Tk() donc pour le résoudre on utilise un toplevel
		fenetre.geometry('300x300')
		n = len(listeDesArcs)
		V = [IntVar() for i in range(n)]
		L = [Checkbutton(fenetre, text=str(listeDesArcs[i]), variable = V[i], onvalue=1, offvalue=0) for i in range(n)]
		
		for cb in L:
			cb.pack()
		def recupNonVoulus():
			NonVoulus = [ G.arcs[i] for i in range(n) if V[i].get() == 1 ]
			for a in NonVoulus:
				G.supprimer_arc(a)
			fenetre.destroy()

		Button(fenetre, text="Supprimer", bg = "red" , fg = "white", command = recupNonVoulus).pack(side = BOTTOM)
		fenetre.mainloop()

	def modifier(listeDesNoeuds,listeDesArcs):
		def changeSommet(listeDesNoeuds):
			fenetre2 = Toplevel()
			fenetre2.geometry('300x300')
			n = len(listeDesNoeuds)

			sommetchangé = StringVar()
			pointsdeparts = [ Radiobutton(fenetre2, text=G[i], variable=sommetchangé, value=G[i]) for i in range(n) ]

			for rb in pointsdeparts:
				rb.pack()

			Button(fenetre2, text="Modifier le nom du sommet", command = lambda : setName(fenetre2, sommetchangé)).pack()

		def changePoidsArc(listeDesArcs):
			
			fenetre2 = Toplevel()
			fenetre2.geometry('300x300')
			n = len(listeDesArcs)

			arcchangé = StringVar()
			arcsModifiables = [Radiobutton(fenetre2, text=G.arcs[i], variable=arcchangé, value=str(G.arcs[i])) for i in range(n)]

			for rb in arcsModifiables:
				rb.pack()

			Button(fenetre2, text="Modifier le poids de cet arc", command = setPoids(fenetre2, arcchangé.get()[0], arcchangé.get()[-1])).pack()

		# menu des modifications
		fenetre = Tk()
		fenetre.geometry('300x300')
		Button(fenetre, text="Modifier un sommet", command = lambda : changeSommet(listeDesNoeuds)).pack()
		Button(fenetre, text="Modifier la valeur d'un poids d'un arc", command = lambda : changePoidsArc(listeDesArcs)).pack()
		fenetre.mainloop()



	# Cadre d'édition de graphe

	editeur = LabelFrame(fenetre, text="Editeur", padx=20, pady=20)
	editeur.pack(fill="y", expand="no", side = LEFT)

	fenetre.title("mode : {} avec un type de graphe : {} ".format(mode,typeGraphe))

	# cas des graphes Dynamiques

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
			Label(editeur, text = "Dynamique settings : Periode {} u.t / Cycle {} u.t".format(periode,cycle)).pack()
		Button(parametresDynamique, text = "valider", command=recupererParametreDynamique).pack()

	Button(editeur, text="Ajouter noeuds", bg = "green" , fg = "black", command = ajoutNoeuds).pack()
	Button(editeur, text="Supprimer noeuds", bg = "green" , fg = "black", command = lambda : supprimeNoeuds(G.sommets) ).pack()
	Button(editeur, text="Ajouter arcs", bg = "green" , fg = "black", command = lambda : ajoutArcs(G.sommets)).pack()
	Button(editeur, text="Supprimer arcs", bg = "green" , fg = "black", command = lambda : supprimeArcs(G.arcs)).pack()
	Button(editeur, text="Modifications", bg = "green" , fg = "black", command = lambda : modifier(G.sommets,G.arcs) ).pack()

	if mode == "Ferro":
		def ligne_ferroviaire():
			ajoutNoeuds(modeLigne = True)
		Button(editeur, text="Créer ligne", bg = "green" , fg = "black", command = ligne_ferroviaire).pack()

	# Cadre aperçu du graphe

	apercu = LabelFrame(fenetre, text="Aperçu", padx=20, pady=20)
	apercu.pack(fill="both", expand=True, side = RIGHT)
	# Boutons d'aperçu et de PCC
	
	Button(editeur, text="PCC", bg = "red" , fg = "white", command = lambda: pcc(apercu) ).pack(side = BOTTOM)
	Button(editeur, text="Aperçu", bg = "blue" , fg = "white", command = lambda : previsualiser(apercu) ).pack(side = BOTTOM)

	fenetre.mainloop()

# Phase de tests

FenetreMode()
