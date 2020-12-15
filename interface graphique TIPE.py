from tkinter import *

fenetre = Tk()
fenetre.geometry('350x200')



def FenêtreInitiale():
#Choix du type de graphe
    var_choix = StringVar()
    
    choix_DS = Radiobutton(fenetre, text="Déterministe Statique", bg = "violet", variable = var_choix, value="DS")
    choix_DS.place (x= 175 , y = 180)
    choix_SS = Radiobutton(fenetre, text="Stochastique Statique", bg = "violet", variable = var_choix, value="SS")
    choix_DD = Radiobutton(fenetre, text="Déterministe Dynamique", bg = "violet", variable = var_choix, value="DD")
    choix_SD = Radiobutton(fenetre, text="Stochastique Dynamique", bg = "violet", variable = var_choix, value="SD")
    
    TitreChoix = Label(fenetre,text = "Choisissez le type de modélisation" , relief=RAISED , bg = "black" , fg = "white")
    
    TitreChoix.place(x = 0, y = 5)
    choix_DS.place(x = 0 , y = 25)
    choix_SS.place(x = 0 , y = 45)
    choix_DD.place(x = 0 , y = 65)
    choix_SD.place(x = 0 , y = 85)
    
    #Nombre de noeuds dans le graphe
    nb_noeuds = Label(fenetre, text="Combien de noeuds souhaitez-vous dans le graphe ?")
    nb_noeuds.place(x = 30 , y = 140)
    
    var_noeuds = StringVar()
    ligne_noeuds = Entry(fenetre, textvariable = var_noeuds, width = 30)
    ligne_noeuds.place(x = 80 , y = 160)
    
    #Valider
    def Valider():
        global NombreNoeuds , TypeMatrice
        NombreNoeuds = int(var_noeuds.get()) ; TypeMatrice = var_choix.get()
        fenetre.destroy()
        Fenetre(NombreNoeuds,TypeMatrice)
        FenêtreModélisation(var_choix)
    
    bouton_valider = Button(fenetre, text="Valider", bg = "green" , fg = "black", command = Valider)
    bouton_valider.place(x = 150 , y = 180)
    
    
    
    fenetre.mainloop()
    
def FenêtreModélisation(modèle):
        fenetre2 = Tk()
        fenetre2.geometry('350x200')

#Turbo support: https://likegeeks.com/python-gui-examples-tkinter-tutorial/
