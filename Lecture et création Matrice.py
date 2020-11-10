import xlrd
import matplotlib.pyplot as plt

Adresse = 'M:\Feuille.xlsx'
document = xlrd.open_workbook(Adresse)
AdresseDD = 'M:\TIPE-master\Tableur SS.xlsx'
 
 
Feuille_VillesDS = document.sheet_by_index(0) #Villes et DS
Feuille_SS = document.sheet_by_index(1) # (Poids,Proba) SS


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

    Classeur_DD = xlrd.open_workbook(AdresseDD)
    n = len(Classeur_DD.sheet_names) - 1
    Feuille_Base = Classeur_DD.sheet_by_index(0)

    Matrice = [[ None for i in range(cols)] for i in range(ligne)] ; a = 0 ; b = 1 # a numéro de ligne ; b numéro de colonne
    
    for M in range(1,n+1):
        Feuille = Classeur_DD.sheet_by_index(M)
        col = Feuille.ncols - 1 ; ligne = Feuille.nrows - 1
        
        
        for j in range (0,(col) * ( col - 1) // 2, 2): #Pas de 2 car poids + proba codé sur 2 colonnes 
            i = 0 ; Poids = []
            while Feuille.cell_value(rowx=i,colx=j) != 0:  #On s'arrête avant out of range
                Poids.append((Feuille.cell_value(rowx=i+1,colx=j+1) , Feuille.cell_value(rowx=i+1,colx=j+2)))
                i += 1
            M[a][b] = Poids
            M[b][a] = M[a][b]
            b += 1
        a += 1
    return Matrice
        
        

def CréerMatriceDéterministeDynamique(): #AKA DD (poids + heures)
    ListeListePoids = []
    
    
