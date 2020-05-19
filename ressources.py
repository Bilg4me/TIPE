from math import inf
from random import randint, sample
from graphviz import Graph, Source

## Collection : Liste
## Variable de classe : Cycle, Periode, NBelement
# Un cycle (ex : une journée) correspond a Nb.element * Periode
# la loi + n'est pas commutative et s'ecrit sous la forme acc + poids pour etre conforme avec l'associativité sous python

def Mat(n):
    return [[ZERO for j in range(n)] for i in range(n)]

def Taille(M):
    return len(M)

def Noeuds(G):
	N = []
	for P,Points in G:
		if not P in N:
			N.append(P)
		for M,poids in Points:
			if not M in N:
				N.append(M)
	return [Alphabet[i] for i in range(len(N))]

def GrapheVersMat(G):
    A = Annuaire()
    N = Noeuds(G)
    Adj = Mat(len(N))
    for (P,Points) in G:
        for (s,l) in Points:
            Adj[A[P]][A[s]] = l
            Adj[A[s]][A[P]] = l
    return Adj

class Poids:
	
	# Variable de classe
	NBelement = 3
	Cycle = 12
	Periode = Cycle // NBelement
	
	def __init__(self, liste_temps):
		self.collection = liste_temps
		self.horloge = 0
		self.index = (self.horloge // Poids.Periode) % Poids.NBelement
		self.valeur = self.collection[self.index]
		
	def sethorloge(self, h):
		self.horloge = h
		self.index = (self.horloge // Poids.Periode) % Poids.NBelement
		self.valeur = self.collection[self.index]
		
	def __getitem__(self, index):
		return self.collection[index]

	def __add__(self, poids):
		# ici self est un accumulateur de sorte qu'on défini ici une loi + de la forme acc + poids
		
		if self == Poids([0,0,0]):
			return poids
		
		collectionSomme = []

		for valeur in self:
			v = (self.horloge % Poids.Cycle) + valeur
			index = (v // Poids.Periode) % Poids.NBelement
			collectionSomme.append(v + poids[index])
				
		P = Poids(collectionSomme)
		P.sethorloge(self.horloge)
		return P

	def __iadd__(self, w):
		return self + w

	def __lt__(self,w):
		return  self.valeur < w.valeur

	def __eq__(self,w):
		return self.valeur == w.valeur

	def __le__(self,w):
		return self < w or self == w

	def __gt__(self,w):
		return not (self <= w)

	def __ge__(self,w):
		return not (self < w)

	def __str__(self):
		return "{}".format(self.collection)

ZERO = Poids([0,0,0])
INF = Poids([inf,inf,inf])

Alphabet = [ chr(65+i) for i in range(50) ]

def Annuaire():
    A = {}
    for i in range(50):
        A[chr(65 + i)] = i
    return A

P = lambda : Poids([ randint(1,6) for _ in range(3) ])

Ville = [
('A', [('B', P()),('C', P()), ('D', P())]),
('D', [('B', P()),('C', P())])
]

Pays = [
('A',[('B',P()),('E',P())]),
('B',[('D',P())]),
('C',[('E',P()),('B',P()),('D',P()),('G',P())]),
('F',[('D',P()),('G',P())]),
('G',[('E', P())])
]

## TEST

