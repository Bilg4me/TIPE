from math import *
from random import *

# ================ Classe des Poids ================ #

class Poids:

	def __init__(self, valeur):
		self.valeur = valeur

	def __add__(self, w):
		return Poids(self.valeur + w.valeur)

	def __iadd__(self, w):
		return self + w

	def __lt__(self,w):
		return  self.valeur < w.valeur

	def __eq__(self,w):
		return self.valeur == w.valeur

	def __str__(self):
		return "{0}".format(self.valeur)
	
	def display(self, modeAffichage = None):
		return str(self)
	
	# Fonction de classe
		
	def ZERO():
		return Poids(0)
		
	def INF():
		return Poids(inf)
		
	def RANDOM():
		return Poids(randint(1,6))

class PSS(Poids):
	# attribut de classe
	mode = 0
	
	def __init__(self, COUPLES):
		
		self.couples = ([])

		for (c,p) in self.Antidoublons(COUPLES):
			self.couples.append((c,p))
		
		self.norme = self.Esperance()
		self.incertitude = self.Ecart_type()
		self.valeur = (self.norme , self.incertitude)[PSS.mode]
	
	def setvaleur(self):
		self.valeur = (self.norme , self.incertitude)[PSS.mode]
		
	def display(self, modeAffichage):
		if modeAffichage == 'moyenne':
			return str(self.norme)
		elif modeAffichage == 'fiabilite':
			return str(self.incertitude)
		else: # détail
			return str(self)
			
		
	# Fonction de classe
	
	def ZERO():
		return PSS([(0,1)])
		
	def INF():
		return PSS([(inf,1)])
	
	def RANDOM():
		def subAlea(x,L):
			if len(L) == 2 or x <= 0.2:
				L.append(round(1-sum(L), 2))
				return L
			L.append(round(uniform(0,x), 2))
			return subAlea( x - L[-1], L)

		plist = subAlea(1,[])
		clist = [randint(1,4) for k in range(len(plist))]
		return PSS(zip(clist,plist))
		
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
		return PSS(COUPLES)

	def __str__(self):
		s = ""
		for c,p in self.couples:
			s += " | {} : {} ".format(c,p) + '\n'
		return s
		
	## Fonctions propre
	
	def Antidoublons(self,L):
		B = sorted(L)
		A = [B[0]]
		for k in range(1,len(B)):
			if B[k][0] == A[-1][0]:
				A[-1] = (B[k][0],round(A[-1][1]+B[k][1], 2))
			else:
				A.append(B[k])
		return A

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
		
		return ex2 - (self.Esperance() ** 2)
		
	def Ecart_type(self) :
		return round(sqrt(self.Variance()),2)

# TODO : Construire les poids en les faisant hériter de cette structure
