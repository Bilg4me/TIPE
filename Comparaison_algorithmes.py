from numpy import *
import time
import math

def generer_matrice_adjacence(n, d, poids_max):
    matrice = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        c = 0
        while n*d > c :
            matrice[random.randint(0,n-1)][i] = random.randint(1,poids_max)
            c += 1
    for i in range(n):
        matrice[i][i] = 0

    return matrice

def FloydWarshallAvecReconstruction(matrice):

    n = len(matrice)

    distances, suivants = [[0 for _ in range(n)] for _ in range(n)], [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            distances[i][j] = matrice[i][j]
            suivants[i][j] = j

    for i in range(n):
        distances[i][i] = 0
        suivants[i][i] = i

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                    suivants[i][j] = suivants[i][k]

    return suivants


def FloydWarshallChemin(prochain_sommets, poids_max, depart, arrivee):

    if prochain_sommets[depart][arrivee] == 0:
        return []

    chemin = [depart]

    position = depart

    while position != arrivee:
        position = prochain_sommets[position][arrivee]
        chemin.append(position)

    return chemin


def mat_vers_arcs(M): #Renvoie les arcs d'un graphe à partir de sa matrice d'adjacence
    L = [] ; n = len(M)
    for i in range(n):
        for j in range(n):
            if M[i][j] != 0:
                L.append((j,i))
    return L


class Graphe():

    def __init__(self, noeuds):
        self.matriceAdj = noeuds.copy()


    def bellmanFord(self, src, ordre):

        dist = [math.inf] * len(self.matriceAdj)
        precedence = [-1] * len(self.matriceAdj)
        dist[src-1] = 0
        precedence[src-1] = src-1
        relax = True

        iteration = 0

        while (iteration < len(self.matriceAdj)-1) and relax == True:
            relax = False
            # relaxation des sommets
            for elm in ordre:
                # chaque éleéent elm est un tuple (u,v)
                if (dist[elm[1]-1] > dist[elm[0]-1]+self.matriceAdj[elm[0]-1][elm[1]-1]):
                    dist[elm[1]-1] = dist[elm[0]-1]+self.matriceAdj[elm[0]-1][elm[1]-1]
                    precedence[elm[1]-1] = elm[0]-1
                    relax = True
            iteration += 1

        self.Afficher(src, dist)

    def minDistance(self, dist, S, T):

        # Initialiser la distance minimale pour le nœud
        min = math.inf
        min_index = -1

        for v in T:
            if dist[v-1] < min:
                min = dist[v-1]
                min_index = v-1

        # supprimer de T et ajouter dans S
        T.remove(min_index+1)
        S.append(min_index+1)
        return min_index

    def dijkstra(self, src):
        t1 = time.perf_counter()

        dist = [math.inf] * len(self.matriceAdj)
        precedence = [-1] * len(self.matriceAdj)
        dist[src-1] = 0
        precedence[src-1] = src-1
        S = []
        T = [(i+1) for i in range(len(self.matriceAdj))]

        while len(S) < len(self.matriceAdj):

            # Choisir un sommet u qui n'est pas dans l'ensemble S et
            # qui a une valeur de distance minimale
            u = self.minDistance(dist, S, T)

            # relaxation des sommets
            for v in range(len(self.matriceAdj)):
                if (self.matriceAdj[u][v] > 0) and (dist[v] > (dist[u] + self.matriceAdj[u][v])):
                    dist[v] = dist[u] + self.matriceAdj[u][v]
                    precedence[v] = u

        self.Afficher(src, dist)
