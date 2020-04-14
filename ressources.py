from math import inf
from random import randint
from graphviz import Graph, Source

class Poids:
	
	λ = None
	
	def __init__(self, time, dist):
		self.temps = time
		self.distance = dist
	
	def __add__(self, w):
		p = Poids(0,0)
		p.distance = self.distance + w.distance
		p.temps = self.temps + w.temps
		return p
	
	def __iadd__(self, w):
		return self + w
		
	def __lt__(self,w):
		if w.temps == inf:
			return True 
		return  Poids.λ * self.temps + (1-Poids.λ) * self.distance < Poids.λ * w.temps + (1-Poids.λ) * w.distance
	
	def __eq__(self,w):
		if w.temps == inf and self.temps == inf:
			return True
		elif w.temps == inf and self.temps != inf:
			return False
		else:
			 return Poids.λ * self.temps + (1-Poids.λ) * self.distance == Poids.λ * w.temps + (1-Poids.λ) * w.distance
		
	def __le__(self,w):
		return self < w or self == w
		
	def __gt__(self,w):
		return not (self <= w)
	
	def __ge__(self,w):
		return not (self < w)
	
	def __str__(self):
		return "(t{0},d{1})".format(self.temps, self.distance)

ZERO = Poids(0,0)
INF = Poids(inf,inf)

Alphabet = [ chr(65+i) for i in range(50) ]

def Annuaire():
    A = {}
    for i in range(50):
        A[chr(65 + i)] = i
    return A
    
P = lambda : Poids(randint(1,6),randint(1,6))

Pays = [
('A',[('B',P()),('E',P())]),
('B',[('D',P())]),
('C',[('B',P()),('D',P()),('E',P())]),
('F',[('D',P()),('E',P())])
]


Ville = [
('A', [('B', P()),('C', P()), ('D', P())]),
('D', [('B', P()),('C', P())])
]

def Normaliser(s):
	g = ""
	build = ""
	for k in range(len(s)):
		
		if s[k].isnumeric():
			build += s[k]
		elif build != "":
			if int(build) > 15:
				g += str(randint(0,15)) + s[k]
			else:
				g+= build + s[k]
			build = ""
		else:
			g += s[k]
	return g

def Lettrifier(s):
	g = ""
	build = ""
	for k in range(len(s)):
		if s[k].isnumeric():
			build += s[k]
		elif build != "":
			g += Alphabet[int(build)] + s[k]
			build = ""
		else:
			g += s[k]
	return g

def DotVersGraphe(content):
	G = []
	L = content.split('\n\t')
	L = L[1:-1]
	for l in Alphabet:
		Points = []
		for t in L:
			if t[0] == l:
				Points.append((t[-1],P()))
		if Points != []:
			G.append( (l,Points) )
	return G

path = 'Graphe/abstract.gv'
dot = Source.from_file(path)	
dot.source = Lettrifier(Normaliser(dot.source))
Abstrait = DotVersGraphe(dot.source)




