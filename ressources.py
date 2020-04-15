from random import *
from math import *

# TODO: Gerer les inf avec la methode isinf() et isnan()

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

	# Surcharge des operateurs

	def __add__(self, w):
		COUPLES = []
		for cs,ps in self.couples:
			for cw,pw in w.couples:
				COUPLES.append((cs+cw, ps*pw))
		return Poids(COUPLES)

	def __iadd__(self, w):
		return self + w

	def __str__(self):
		return " couples {}, valeur {}".format(self.couples, self.valeur)

	def __lt__(self, w):
		if isinf(w):
			return True
		return self.valeur < w.valeur

	def __eq__(self, w):
		if isinf(w):
			return False
		return self.valeur == w.valeur

	def __le__(self,w):
		return self < w or self == w

	def __gt__(self,w):
		return not (self <= w)

	def __ge__(self,w):
		return not (self < w)

	def __float__(self):
		return self.valeur

	## Fonctions propre

	def Esperance(self) :
		E = 0
		for (c,p) in self.couples:
			E += c * p
		return E


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

GSS = [
('A', [('B', P()),('C', P()), ('D', P())]),
('D', [('B', P()),('C', P())])
]

###################
## PHASE DE TEST ##
###################
