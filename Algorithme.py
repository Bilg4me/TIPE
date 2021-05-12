from Graphes import *

# ================== Algorithme ==================== #

def Taille(M):
    return len(M)
    
def Noeuds(G):
	return list(G.sommets)

def GrapheVersMat(G):
    return G.matrice_adjacence()

def Autour(M, G):
	return G.liste[G.sommets.index(M)][1]

def PlusProche(Lignes,G):
	M,m = None,G.INF
	for k in range(len(Lignes[-1])) :
		if type(Lignes[-1][k]) == tuple and Lignes[-1][k][1] < m:
			M,m = G[k],Lignes[-1][k][1]		
	return M,m

def Retirer(P, Points):
	for k in range(len(Points)):
		if P == Points[k]:
			Points.pop(k)
			break

def Init(M, G):
	A = G.matrice_adjacence()
	T = [(M,G.ZERO)]
	R = Noeuds(G)
	LL = []
	L = [Noeuds(G)]
	for P in R:
		if P == M:
			LL.append(G.ZERO)
		else:
			LL.append(G.INF)
	L.append(LL)
	return L, T, R, A

def Tableau(M, G):
	
	Lignes ,Trouve, Recherche, Adj = Init(M,G)
	
	def Placer(O,Voisins,acc):
		L = []
		PointsTrouves = [P for P,poids in Trouve]
		PointsVoisins = [P for P,poids in Voisins]
		Noeuds = Lignes[0]

		for M in Noeuds:
			if M in PointsTrouves:
				L.append(None)
			elif M in PointsVoisins:
				for P,poids in Voisins:
					if P == M and type(Lignes[-1][G.sommets.index(M)]) == tuple:
						if Lignes[-1][G.sommets.index(M)][1] < acc + poids:
							L.append((Lignes[-1][G.sommets.index(M)]))
						else:
							L.append((O, acc + poids))
					elif P == M and Lignes[-1][G.sommets.index(M)] == G.INF:
						L.append((O, acc + poids))
						
			else:
				L.append(Lignes[-1][G.sommets.index(M)])
				
		Lignes.append(L)
		Trouve.append(PlusProche(Lignes,G))
		Retirer(O, Recherche)

	
	while len(Recherche) > 1:
		M = Trouve[-1][0]
		acc = Trouve[-1][1]
		V = Autour(M, G)
		# print(V)
		# print("je pars de",M,"accumulateur",acc)
		Placer(M,V,acc)	
		
	return Lignes, Trouve

def Suivis(A,B,L):
	for k in range(len(L)-1):
		if ( L[k] == A and L[k+1] == B ):
			return True
	return False

def Visualiser(A,B,G,modeApercu,modelView = 0):
	# par défaut le mode d'optimisation pour un PSS se fait en moyenne
	if modeApercu == 'fiabilite':
		G.typePoids.mode = 1
	if modeApercu == 'moyenne':
		G.typePoids.mode = 0
		
	print("plus court chemin entre {} et {} {}".format(A,B,modeApercu))

	Adj = GrapheVersMat(G)
	g = Digraph(engine=roadmap[modelView], format = 'png')
	PCC1 = Chemin(A,B,G)
	for i in range(len(Adj)):
		for j in range(len(Adj)):
			if Adj[i][j] < G.INF :
				if Suivis(G[i],G[j],PCC1) :
					g.edge(G[i] ,G[j] ,label = Adj[i][j].display(modeApercu) , color='green', penwidth='1')
				else:
					g.edge(G[i] ,G[j] ,label = Adj[i][j].display(modeApercu) , color='black')
					
	g.render("Graphe.gv")
			
def min_of(L,G):
	M,m = None,G.INF
	for k in L:
		if type(k) == tuple and k[1] < m:
			M,m = k
	return M
	
def Chemin(A,B,G):
	Optimal = [B]
	Lignes,Trouve = Tableau(A,G)
	while B != A:
		for k in range(len(Trouve)):
			if Trouve[k][0] == B :
				B = min_of(Lignes[k+1],G)
				Optimal = [B] + Optimal
	return Optimal
