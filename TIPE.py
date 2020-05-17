from ressources import *

def Autour(S, Adj):
    S_ = Annuaire()[S]
    Autour = []
    Points = Adj[S_]
    for i,poids in enumerate(Points):
        if poids > ZERO :
            Autour.append((Alphabet[i], poids))
    return Autour

def PlusProche(Lignes):
	M,m = None,INF
	for k in range(len(Lignes[-1])) :
		if type(Lignes[-1][k]) == tuple and Lignes[-1][k][1] < m:
			M,m = Alphabet[k],Lignes[-1][k][1]
	return M,m

def Retirer(P, Points):
	for k in range(len(Points)):
		if P == Points[k]:
			Points.pop(k)
			break

def Init(M, G):
	A = GrapheVersMat(G)
	T = [(M,ZERO)]
	R = Noeuds(G)
	LL = []
	L = [Noeuds(G)]
	for P in R:
		if P == M:
			LL.append(ZERO)
		else:
			LL.append(INF)
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
					if P == M and type(Lignes[-1][Annuaire()[M]]) == tuple:
						if Lignes[-1][Annuaire()[M]][1] < acc + poids:
							L.append((Lignes[-1][Annuaire()[M]]))
						else:
							L.append((O, acc + poids)) # attention la loi + pour les poids n'est pas commutative
					elif P == M and Lignes[-1][Annuaire()[M]] == INF:
						L.append((O, acc + poids))
						

			else:
				L.append(Lignes[-1][Annuaire()[M]])

		Lignes.append(L)
		Trouve.append(PlusProche(Lignes))
		Retirer(O, Recherche)


	while len(Recherche) > 1:
		M = Trouve[-1][0]
		acc = Trouve[-1][1]
		print("je me trouve en",M,"j'ai accumule",acc, "->" , acc.valeur)
		V = Autour(M, Adj)
		Placer(M,V,acc)

	return Lignes,Trouve

def Suivis(A,B,L):
	for k in range(len(L)-1):
		if ( L[k] == A and L[k+1] == B ) or ( L[k] == B and L[k+1] == A ):
			return True
	return False


def Visualiser(A,B,G):
	print("plus court chemin entre {} et {}".format(A,B))
	Adj = GrapheVersMat(G)
	g = Graph(engine='sfdp')
	PCC1 = Chemin(A,B,G)
	for i in range(len(Adj)):
		for j in range(i+1,len(Adj)):
			if Adj[i][j] > ZERO:
				if Suivis(Alphabet[j],Alphabet[i],PCC1) :
					g.edge( Alphabet[j] , Alphabet[i] ,label = str(Adj[i][j]), color='green', penwidth='2')
				else:
					g.edge( Alphabet[j] , Alphabet[i] ,label = str(Adj[i][j]) , color='black')
	g.view("Graphe.gv", "Graphe")
    

def min_of(L):
	M,m = None,INF
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
				B = min_of(Lignes[k+1])
				Optimal = [B] + Optimal
	return Optimal

###################
## PHASE DE TEST ##
###################

Visualiser('A','F', Pays)
