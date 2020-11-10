import xlrd
import matplotlib.pyplot as plt

Adresse = 'M:\Feuille.xlsx'
document = xlrd.open_workbook(Adresse)
 
 
Feuille_VillesDS = document.sheet_by_index(0) #Villes et DS
Feuille_SS = document.sheet_by_index(1) # (Poids,Proba) SS
Feuille_DD = document.sheet_by_index(2) # Poids en fonction de l'heure DD


cols1 = Feuille_VillesDS.ncols
rows1 = Feuille_VillesDS.nrows

def RécupVilles():
    ListeVilles = []
    for r in range(1, rows1):
        ListeVilles += [Feuille_VillesDS.cell_value(rowx=r, colx=0)]
    return ListeVilles
    
def CréerMatriceDéterministeStatique(): #AKA DS (poids)
    Matrice = [[ None for i in range(rows1 -1) ] for i in range (cols1 - 1)]
    for i in range(1,rows1):
        Matrice[i-1][i-1] = 0
        j = i + 1 
        while j < cols1:
            Matrice[i-1][j-1] = Feuille_VillesDS.cell_value(rowx=i,colx=j)
            Matrice[j-1][i-1] = Matrice[i-1][j-1] #Matrice symétrique DONC ne fonctionne pas en orienté
            j += 1
    return Matrice
    
    
cols2 = Feuille_SS.ncols
rows2 = Feuille_SS.nrows

def CréerMatriceStochastiqueStatique(): #AKA SS (poids + proba)
    Matrice = [[ None for i in range(cols1 - 1)] for i in range(rows1 - 1)] ; a = 0 ; b = 1 # a numéro de ligne ; b numéro de colonne
    for k in range(len(Matrice)):
        Matrice[k][k] = None
    for j in range (0,(cols1 - 1) * ( cols1 - 2) // 2, 2): #Pas de 2 car poids + proba codé sur 2 colonnes 
        i = 0 ; Poids = []
        while Feuille_SS.cell_value(rowx=i,colx=j) != 0:  #On s'arrête avant out of range
            Poids.append((Feuille_SS.cell_value(rowx=i,colx=j) , Feuille_SS.cell_value(rowx=i,colx=j+1)))
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
    
    
