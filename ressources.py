from random import *
from math import *
from graphviz import Graph

# Une chose qui m'a posé problème sans que je ne le remarque
# la fonction add n'était pas adapté pour ajouter des poids nuls
# et que l'ordre dans lequel on addtionnait comptait dans ce cas partculier

Alphabet = [ chr(65+i) for i in range(50) ]

def Annuaire():
    A = {}
    for i in range(50):
        A[chr(65 + i)] = i
    return A

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

def Antidoublons(L):
	B = sorted(L)
	A = [B[0]]
	for k in range(1,len(B)):
		if B[k][0] == A[-1][0]:
			A[-1] = (B[k][0],round(A[-1][1]+B[k][1], 2))
		else:
			A.append(B[k])
	return A

class Poids:

	def __init__(self, COUPLES):
		self.couples = ([])

		for (c,p) in Antidoublons(COUPLES):
			self.couples.append((c,p))

		self.valeur = self.Esperance()
		self.incertitude = self.Ecart_type()

	# Surcharge des operateurs

	def __add__(self, w):
		if w.valeur == 0:
			return self
		elif self.valeur == 0:
			return w
		COUPLES = []
		for (cs,ps) in self.couples:
			for (cw,pw) in w.couples:
				COUPLES.append((cs+cw, ps*pw))
		return Poids(COUPLES)

	def __iadd__(self, w):
		return self + w

	def __str__(self):
		s = ""
		for c,p in self.couples:
			s += " | {} : {} ".format(c,p) + '\n'
		return s

	def __lt__(self, w):
		if isinf(w):
			return True
		elif isnan(w):
			return False
		return self.valeur < w.valeur

	def __eq__(self, w):
		if isnan(w):
			return False
		return self.valeur == w.valeur

	def __le__(self,w):
		return self < w or self == w

	def __gt__(self,w):
		return not (self <= w)

	def __ge__(self,w):
		return not (self < w)

	def __float__(self):
		return float(self.valeur)

	## Fonctions propre

	def Esperance(self) :
		E = 0
		for (c,p) in self.couples:
			E += c * p
		return round(E,2)
		
	def Variance(self) :
		ex2 = 0
		for (c,p) in self.couples:
			ex2 += (c ** 2) * p
		ex2 = round(ex2, 2)
		
		return ex2 - (self.valeur ** 2)
		
	def Ecart_type(self) :
		return round(sqrt(self.Variance()),2)


def subAlea(x,L):
    if len(L) == 2 or x <= 0.2:
        L.append(round(1-sum(L), 2))
        return L
    L.append(round(uniform(0,x), 2))
    return subAlea( x - L[-1], L)

def P():
	plist = subAlea(1,[])
	clist = [randint(1,4) for k in range(len(plist))]
	return Poids(zip(clist,plist))

ZERO = Poids([(0,0)])
INF = inf

Ville = [
('A', [('B', P()),('C', P()), ('D', P())]),
('D', [('B', P()),('C', P())])
]

Pays = [
('A',[('B',P()),('E',P())]),
('B',[('D',P())]),
('C',[('B',P()),('D',P()),('E',P())]),
('F',[('D',P()),('E',P())])
]

###################
## PHASE DE TEST ##
###################
