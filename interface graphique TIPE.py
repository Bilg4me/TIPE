from tkinter import *
from PIL import ImageTk

# Graphe

G = [[],[]]

def setPoids():
	#se charge d'affecter un poids à un arc en fonction du type de graphe choisi
	return None

def setName():
	#se charge d'affecter un poids à un arc en fonction du type de graphe choisi
	return None

def FenetreMode():
	global fenetre
	fenetre = Tk()
	fenetre.geometry('800x600')
	Button(fenetre, text="Routier", bg = "green" , fg = "black", command = lambda : FenetreTypeGraphe("Routier")).pack(side=TOP, padx=5, pady=5)
	Button(fenetre, text="Ferro", bg = "green" , fg = "black", command = lambda : FenetreTypeGraphe("Ferro")).pack(side=BOTTOM, padx=5, pady=5)
	fenetre.mainloop()

def FenetreTypeGraphe(mode):

    #Choix du type de graphe
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


def FenetreModelisation(mode, typeGraphe):
	fenetre = Tk()
	fenetre.geometry('800x600')

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

	def previsualiser():
		photo = ImageTk.PhotoImage(file="Graphe.jpeg")
		canvas = Canvas(apercu,width=100, height=500)
		canvas.create_image(0, 0, anchor=NW, image=photo)
		canvas.image = photo
		canvas.pack(fill="both", expand=True)

	# ajout/suppression de noeuds et arc

	def ajoutNoeuds():
		def rentrerNoeuds(nb):
			def ajouterlesnoeudsaugraphe(entrees):
				for v in entrees:
					G[0].append(v.get())
			
			fenetre = Tk()
			fenetre.geometry('300x300')
			LesEntrées = []
			for k in range(nb):
				Label(fenetre, text="Noueud n°{}".format(k+1), bg="yellow").pack()
				LesEntrées.append( Entry(fenetre, width=30) )
				LesEntrées[-1].pack()
				
			Button(fenetre,text="Valider",command = lambda : ajouterlesnoeudsaugraphe(LesEntrées)).pack()
				
			
		fenetre = Tk()
		fenetre.geometry('300x300')
		nb_noeuds = Label(fenetre, text="Combien de noeuds souhaitez-vous ajouter dans le graphe ?")
		nb_noeuds.place(x = 30 , y = 140)
		
		ligne_noeuds = Spinbox(fenetre, from_=0, to=30)
		ligne_noeuds.place(x = 0 , y = 0)
		Button(fenetre, text="choisir", command= lambda : rentrerNoeuds(int(ligne_noeuds.get())) ).pack()
		fenetre.mainloop()

	def supprimeNoeuds(listeDesNoeuds):
		fenetre = Tk()
		fenetre.geometry('300x300')
		listeDesBoutons = [ Checkbutton(fenetre, text= noeuds) for noeuds in listeDesNoeuds ]
		for checkbox in listeDesBoutons:
			checkbox.pack()

		Button(fenetre, text="Supprimer", bg = "red" , fg = "white", command = alert).pack(side = BOTTOM)
		fenetre.mainloop()

	def ajoutArcs(listeDesNoeuds):
		fenetre = Tk()
		fenetre.geometry('300x300')

		départ = LabelFrame(fenetre, text="Départ", padx=20, pady=20)
		départ.pack(fill="y", expand="yes", side = LEFT)

		listeDesDeparts = Listbox(départ)
		for noeuds in listeDesNoeuds:
			listeDesDeparts.insert(1,noeuds)

		listeDesDeparts.pack()

		arrivée = LabelFrame(fenetre, text="Arrivée", padx=20, pady=20)
		arrivée.pack(fill="y", expand="yes", side = RIGHT)

		listeDesArrivées = Listbox(arrivée)
		for noeuds in listeDesNoeuds:
			listeDesArrivées.insert(1,noeuds)

		listeDesArrivées.pack()

		Button(fenetre, text="Set poids", command= setPoids).pack()

		fenetre.mainloop()

	def supprimeArcs(listeDesArcs):
		fenetre = Tk()
		fenetre.geometry('300x300')
		listeDesBoutons = [ Checkbutton(fenetre, text=arcs) for arcs in listeDesArcs ]
		for checkbox in listeDesBoutons:
			checkbox.pack()

		Button(fenetre, text="Supprimer", bg = "red" , fg = "white", command = alert).pack(side = BOTTOM)
		fenetre.mainloop()

	def modifierArc(listeDesNoeuds,listeDesArcs):
		def changeSommet(listeDesNoeuds):
			fenetre2 = Tk()
			fenetre2.geometry('300x300')
			liste = Listbox(fenetre2)
			for noeuds in listeDesNoeuds:
				liste.insert(1,noeuds)
			liste.pack()
			Button(fenetre2, text="Modifier le nom du sommet", command=setName).pack()


		def changePoidsArc(listeDesArcs):
			fenetre2 = Tk()
			fenetre2.geometry('300x300')
			liste = Listbox(fenetre2)
			for arc in listeDesArcs:
				liste.insert(1,arc)
			liste.pack()

			Button(fenetre2, text="Modifier le poids de cet arc", command=setPoids).pack()

		# menu des modifications
		fenetre = Tk()
		fenetre.geometry('300x300')
		Button(fenetre, text="Modifier un sommet", command = lambda : changeSommet(listeDesNoeuds)).pack()
		Button(fenetre, text="Modifier la valeur d'un poids d'un arc", command = lambda : changePoidsArc(listeDesArcs)).pack()
		fenetre.mainloop()



	# Cadre d'édition de graphe

	editeur = LabelFrame(fenetre, text="Editeur", padx=20, pady=20)
	editeur.pack(fill="y", expand="no", side = LEFT)

	Label(editeur, text = "mode : {} avec un type de graphe : {} ".format(mode,typeGraphe) ).pack()

	Button(editeur, text="Ajouter noeuds", bg = "green" , fg = "black", command = ajoutNoeuds).pack()
	Button(editeur, text="Supprimer noeuds", bg = "green" , fg = "black", command = lambda : supprimeNoeuds(['a','b','c','d','e']) ).pack()
	Button(editeur, text="Ajouter arcs", bg = "green" , fg = "black", command = lambda : ajoutArcs(['a','b','c','d','e'])).pack()
	Button(editeur, text="Supprimer arcs", bg = "green" , fg = "black", command = lambda : supprimeArcs([ 'a-b', 'a-c', 'a-d', 'b-c', 'b-d'])).pack()
	Button(editeur, text="Modifier arc", bg = "green" , fg = "black", command = lambda : modifierArc(['a','b','c','d','e'],[ 'a-b', 'a-c', 'a-d', 'b-c', 'b-d']) ).pack()
	Button(editeur, text="Aperçu", bg = "blue" , fg = "white", command = previsualiser).pack(side = BOTTOM)

	if mode == "Ferro":
		Button(editeur, text="Créer ligne", bg = "green" , fg = "black", command = alert).pack()

	# Cadre aperçu du graphe

	apercu = LabelFrame(fenetre, text="Aperçu", padx=20, pady=20)
	apercu.pack(fill="both", expand=True, side = RIGHT)

	fenetre.mainloop()


# Phase de tests

FenetreMode()
