import xlrd
import matplotlib.pyplot as plt

Adresse = '/Users/mathieutanre/Documents/TIPE/Feuille.xlsx'
document = xlrd.open_workbook(Adresse)
AdresseDD = '/Users/mathieutanre/Documents/Tableur SS.xlsx'
AdresseSD ='/Users/mathieutanre/Documents/Classeur SD.xlsx'


Feuille_VillesDS = document.sheet_by_index(0) #Villes et DS
Feuille_SS = document.sheet_by_index(1) # (Poids,Proba) SS
Feuille_DD = document.sheet_by_index(2) # Dynamique DD


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

n= cols1 - 1

def CréerMatriceStochastiqueStatique1(): #AKA SS (poids + proba)
    Matrice = [[ None for i in range(n)] for i in range(n)] ; a = 0 ; b = 1 # a numéro de ligne ; b numéro de colonne
    for k in range(n):
        Matrice[k][k] = [(0,1)]
    for j in range (0, n * (n-1) , 2): #Pas de 2 car poids + proba codé sur 2 colonnes
        i = 0 ; Poids = []
        while Feuille_SS.cell_value(rowx=i,colx=j) != 0:  #On s'arrête avant out of range
            Poids.append((Feuille_SS.cell_value(rowx=i,colx=j) , Feuille_SS.cell_value(rowx=i,colx=j+1)))
            i += 1
        Matrice[a][b] = Poids
        Matrice[b][a] = Matrice[a][b]
        if b < n-1:
            b += 1
        else:
            a += 1
            b = a + 1
    return Matrice

def CréerMatriceStochastiqueStatique2(): #AKA SS (poids + proba)

    Classeur_DD = xlrd.open_workbook(AdresseDD)
    n = len(Classeur_DD.sheet_names()) - 1
    Feuille_Base = Classeur_DD.sheet_by_index(0)

    Matrice = [[ None for i in range(Feuille_Base.nrows - 1)] for i in range(Feuille_Base.nrows - 1)] ; a = 0 ; b = 1 # a numéro de ligne ; b numéro de colonne

    for M in range(1,n+1):
        Feuille = Classeur_DD.sheet_by_index(M)
        col = Feuille.ncols - 1

        for j in range (0, col - 1 , 2): #Pas de 2 car poids + proba codé sur 2 colonnes
            i = 0 ; Poids = []
            while Feuille.cell_value(rowx=i+1,colx=j+1) != 0:  #On s'arrête avant out of range
                Poids.append((Feuille.cell_value(rowx=i+1,colx=j+1) , Feuille.cell_value(rowx=i+1,colx=j+2)))
                i += 1
            Matrice[a][b] = Poids
            Matrice[b][a] = Matrice[a][b]
            b += 1
        a += 1 ; b = a + 1
    return Matrice




cols3 = Feuille_DD.ncols
rows3 = Feuille_DD.nrows

def CréerMatriceDéterministeDynamique(): #AKA DD (poids + heures)
    Matrice = [[ None for i in range(n)] for i in range(n)] ; a=0 ; b=1
    for k in range(n) :
        Matrice[k][k] = [0 for i in range(rows3)]
    for j in range (cols3): #Pas de 2 car poids + proba codé sur 2 colonnes
        Poids = []
        for i in range (rows3):  #On s'arrête avant out of range
            Poids.append(Feuille_DD.cell_value(rowx=i,colx=j))
        Matrice[a][b] = Poids
        Matrice[b][a] = Matrice[a][b]
        if b < n-1:
            b += 1
        else:
            a += 1
            b = a + 1
    return Matrice


def CréerMatriceStochastiqueDynamique(): #AKA SD (le must)

    Classeur_SD = xlrd.open_workbook(AdresseSD)
    p = len(Classeur_SD.sheet_names()) - 1
    Feuille_Base = Classeur_SD.sheet_by_index(0)
    n = Feuille_Base.nrows - 1

    Matrice = [[[ None for i in range(p)] for i in range(n)] for i in range(n)] ; a = 0 ; b = 1 # a numéro de ligne ; b numéro de colonne

    for M in range(1,p+1):
        Feuille = Classeur_SD.sheet_by_index(M)
        col = Feuille.ncols - 1

        for j in range (0, col , 2): #Pas de 2 car poids + proba codé sur 2 colonnes
            i = 0 ; Poids = []
            while Feuille.cell_value(rowx=i+1,colx=j+1) != 0:  #On s'arrête avant out of range
                Poids.append((Feuille.cell_value(rowx=i+1,colx=j+1) , Feuille.cell_value(rowx=i+1,colx=j+2)))
                i += 1
            Matrice[a][b][M] = Poids
            Matrice[b][a][M] = Matrice[a][b][M]
            if b < n - 1:
                b += 1
            else:
                a += 1
                b = a + 1
    return Matrice

