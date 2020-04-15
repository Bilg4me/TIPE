from ressources import *

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
							L.append((O, acc + poids))
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
		V = Autour(M, Adj)
		Placer(M,V,acc)
		# print("je pars de",M,"accumulateur",acc)

	return Lignes, Trouve

def BienAfficher(L):
	disp = ""
	for l in L:
		disp += str(l) + '\n'

	print(disp)

def Suivis(A,B,L):
	for k in range(len(L)-1):
		if ( L[k] == A and L[k+1] == B ) or ( L[k] == B and L[k+1] == A ):
			return True
	return False

def Visualiser(A,B,G,barycentre):
	print("plus court chemin entre {} et {}".format(A,B))
	print("Conditions de PCC1 sont t : {0} et d: {1} en vert".format(barycentre ,1 - barycentre))
	print("Conditions du PCC2 sont t : {0} et d: {1} en rouge".format(1 - barycentre, barycentre))
	Adj = GrapheVersMat(G)
	g = Graph(engine='circo')
	PCC1,PCC2 = Chemin(A,B,G,barycentre),Chemin(A,B,G,1 - barycentre)
	for i in range(len(Adj)):
		for j in range(i+1,len(Adj)):
			if Adj[i][j] > ZERO:
				if Suivis(Alphabet[j],Alphabet[i],PCC1) :
					g.edge( Alphabet[j] , Alphabet[i] ,label = str(Adj[i][j]) + "PCC1" , color='green', penwidth='2')
				elif Suivis(Alphabet[j],Alphabet[i],PCC2) :
					g.edge( Alphabet[j] , Alphabet[i] ,label = str(Adj[i][j]) + "PCC2" , color='red', penwidth='2')
				else:
					g.edge( Alphabet[j] , Alphabet[i] ,label = str(Adj[i][j]) , color='black')

	g.view("Graphe.gv", "Graphe")

def min_of(L):
	M,m = None,INF
	for k in L:
		if type(k) == tuple and k[1] < m:
			M,m = k
	return M

def Chemin(A,B,G,barycentre):
	Poids.λ = barycentre
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

oui = 1
while oui:
	Visualiser('A',chr(65+randint(1,13)),Abstrait,1)
	oui = int(input("continuer ?"))
