from graphviz import Digraph
from Poids import *

# =============== Roadmap ========================== #

roadmap = ['dot', 'neato', 'fdp', 'sfdp', 'twopi', 'circo' ]

# =============== Classe des Graphes =============== #

class Arc:

	def __init__(self, A, B, p):
		self.origine = A
		self.destination = B
		self.poids = p
		
	def __getitem__(self, index):
		return [self.origine,self.destination][index]
	
	def __str__(self):
		return self.origine + "->" + self.destination + "->" + str(self.poids)

class Graphe:
	# V des sommets et E une liste d'arcs

	def __init__(self, V, E, PoidsType):
		self.sommets = V
		self.arcs = E
		
		self.typePoids = PoidsType
		self.ZERO = PoidsType.ZERO()
		self.INF = PoidsType.INF()

		self.liste = self.liste_adjacence()
		self.matrice = self.matrice_adjacence()
		
	def __getitem__(self, index):
		return self.sommets[index]

	""" Méthodes """
	
	def randomPoids(self):
		return self.typePoids.RANDOM()

	def voisins(self, S):
		return [s for s,p in self.liste[self.sommets.index(S)][1] ]

	def ajouter_sommet(self, S):
		if not (S in self.sommets):
			self.sommets.append(S)
			self.recharger()

	def supprimer_sommet(self, S):
		self.sommets.remove(S)
		for arc in self.arcs:
			if S in arc:
				self.supprimer_arc(arc)
	
	def modifier_sommet(self, old, new):
		
		# on suppose que old est dans les sommets du graphe
		
		i = self.sommets.index(old)
		self.sommets[i] = new
		
		#on remplace old par new dans tous les arcs ou il est impliqué
		
		for arc in self.arcs:
			if old == arc.origine:
				i = self.arcs.index(arc)
				self.arcs[i].origine = new
			elif old == arc.destination:
				i = self.arcs.index(arc)
				self.arcs[i].destination = new
		
		self.recharger()
			

	def ajouter_arc(self, O,D,p):
		if not (Arc(O,D,p) in self.arcs):	
			self.arcs.append(Arc(O,D,p))
			self.recharger()

	def supprimer_arc(self, A):
		self.arcs.remove(A)
		self.recharger()

	def modifier_poids(self, A, p):
		i = self.arcs.index(A)
		self.arcs[i].poids = p

	def recharger(self):
		self.liste = self.liste_adjacence()
		self.matrice = self.matrice_adjacence()

	def liste_adjacence(self):
		V = self.sommets
		E = self.arcs
		Liste = [ [S,[] ] for S in V]
		for [S,voisins] in Liste:
			for arc in E:
				if S == arc.origine:
					voisins.append((arc.destination,arc.poids))
		return Liste

	def matrice_adjacence(self):
		n = len(self.sommets)
		Matrice = [[self.INF for j in range(n)] for i in range(n)]
		for [S, voisins] in self.liste:
			i = self.sommets.index(S)
			for point,poids in voisins:
				j = self.sommets.index(point)
				Matrice[i][j] = poids
				
		return Matrice
	
	def Visualisation(self , modeApercu = None ,modelView = 0):
		Adj = self.matrice
		g = Digraph(engine=roadmap[modelView], format = 'png')
		for i in range(len(Adj)):
			for j in range(len(Adj)):
				if Adj[i][j] != self.INF:
					g.edge(self.sommets[i] , self.sommets[j] ,label = Adj[i][j].display(modeApercu) , color='black')

		g.render("Graphe.gv")
	
