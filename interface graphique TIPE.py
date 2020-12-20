from tkinter import *

def ModeRoutier():
	FenetreTypeGraphe("Routier")

def ModeFerroviaire():
	FenetreTypeGraphe("Ferro")

def FenetreMode():
	global fenetre
	fenetre = Tk()
	fenetre.geometry('800x600')
	Button(fenetre, text="Routier", bg = "green" , fg = "black", command = ModeRoutier).pack(side=TOP, padx=5, pady=5)
	Button(fenetre, text="Ferro", bg = "green" , fg = "black", command = ModeFerroviaire).pack(side=BOTTOM, padx=5, pady=5)

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
	fenetre2 = Tk()
	fenetre2.geometry('350x200')
	TitreChoix2 = Label(fenetre2,text = "mode : {} avec un type de graphe : {} ".format(mode,typeGraphe) , relief=RAISED , bg = "black" , fg = "white")
	TitreChoix2.place(x = 0, y = 5)
	# #Nombre de noeuds dans le graphe
    # nb_noeuds = Label(fenetre2, text="Combien de noeuds souhaitez-vous dans le graphe ?")
    # nb_noeuds.place(x = 30 , y = 140)
    
    # var_noeuds = StringVar()
    # ligne_noeuds = Spinbox(fenetre2, from_=0, to=10, variable = var_noeuds)
    # ligne_noeuds.place(x = 80 , y = 160)


#Turbo support: https://likegeeks.com/python-gui-examples-tkinter-tutorial/

FenetreMode()
fenetre.mainloop()
