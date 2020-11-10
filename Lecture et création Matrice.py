import xlrd
import matplotlib.pyplot as plt

Adresse = 'M:\Feuille.xlsx'
document = xlrd.open_workbook(Adresse)
 
 
feuille_1 = document.sheet_by_index(0) #Villes et DS
feuille_2 = document.sheet_by_index(1) # (Poids,Proba) SS
feuille_3 = document.sheet_by_index(2) # Poids en fonction de l'heure DD


cols1 = feuille_1.ncols
rows1 = feuille_1.nrows

def RécupVilles():
    ListeVilles = []
    for r in range(1, rows1):
        ListeVilles += [feuille_1.cell_value(rowx=r, colx=0)]
    return ListeVilles
    
def CréerMatriceDéterministeStatique(): #AKA DS (poids)
    Matrice = [[ None for i in range(rows1 -1) ] for i in range (cols1 - 1)]
    for i in range(1,rows1):
        Matrice[i-1][i-1] = 0
        j = i + 1 
        while j < cols1:
            Matrice[i-1][j-1] = feuille_1.cell_value(rowx=i,colx=j)
            Matrice[j-1][i-1] = Matrice[i-1][j-1] #Matrice symétrique DONC ne fonctionne pas en orienté
            j += 1
    return Matrice
    
    
cols2 = feuille_2.ncols
rows2 = feuille_2.nrows

def CréerMatriceStochastiqueStatique(): #AKA SS (poids + proba)
    Matrice = [[ None for i in range(cols1 - 1)] for i in range(rows1 - 1)] ; a = 0 ; b = 1 # a numéro de ligne ; b numéro de colonne
    for k in range(len(Matrice)):
        Matrice[k][k] = None
    for j in range (0,(cols1 - 1) * ( cols1 - 2) // 2, 2): #Pas de 2 car poids + proba codé sur 2 colonnes 
        i = 0 ; Poids = []
        while feuille_2.cell_value(rowx=i,colx=j) != 0:  #On s'arrête avant out of range
            Poids.append((feuille_2.cell_value(rowx=i,colx=j) , feuille_2.cell_value(rowx=i,colx=j+1)))
            i += 1
        Matrice[a][b] = Poids
        Matrice[b][a] = Matrice[a][b]
        if b == cols1 :
            a += 1
            b = a + 1
        else:
            b += 1
    return Matrice
        
        

def CréerMatriceDéterministeDynamique(): #AKA DD (poids + heures)
    ListeListePoids = []
    
    
