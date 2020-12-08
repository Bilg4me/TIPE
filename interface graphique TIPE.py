from tkinter import *

fenetre = Tk()


#Choix du type de graphe
var_choix = StringVar()

choix_DS = Radiobutton(fenetre, text="Déterministe Statique", variable=var_choix, value="DS")
choix_SS = Radiobutton(fenetre, text="Stochastique Statique", variable=var_choix, value="SS")
choix_DD = Radiobutton(fenetre, text="Déterministe Dynamique", variable=var_choix, value="DD")
choix_SD = Radiobutton(fenetre, text="Stochastique Dynamique", variable=var_choix, value="SD")

choix_DS.pack()
choix_SS.pack()
choix_DD.pack()
choix_SD.pack()

#Nombre de noeuds dans le graphe
nb_noeuds = Label(fenetre, text="Combien de noeuds souhaitez-vous dans le graphe ?")
nb_noeuds.pack()

var_noeuds = StringVar()
ligne_noeuds = Entry(fenetre, textvariable = var_noeuds, width = 30)
ligne_noeuds.pack()

#Valider
bouton_valider = Button(fenetre, text="Valider")
bouton_valider.pack()

fenetre.mainloop()

#Turbo support: https://likegeeks.com/python-gui-examples-tkinter-tutorial/
