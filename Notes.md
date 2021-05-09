# Notes

## Thèses - Hizem (Optimisation d'itinéraires dans les réseaux routiers)

Optimisation monocritère
---
 - Méthode deterministes : Algorithme du Simplexe (Type Dijkstra), Algorithme de Séparation évaluation
 - Méthode Stochastique : Recuit simulé, Algorithmes évolutionnistes (Type A*)

Optimisation multicrière
---
 - Approche par agregation de critère : Somme pondérée, Intégrale de Choquet
 - Approche par Pareto dominance

Les Différents types de graphes
---
- Graphe statique determnistes : poids constants et fixés
- Graphe statique stochastique : calcul de l'esperance mathématique du poids de chaque arc pour se ramener au cas précédant
- Graphe dynamique deterministes : poids est un fonction escalier du temps avec pas régulier
Arc FIFO (modelisation d'une voie simple)
Dans le cas d'un graphe FIFO on peut adapter Dijkstra au cas des graphes dynamiques
- Graphe dynamique stochastiques
- Graphe statique avec intervalle : un scenario nous permet de nous ramener au cas des GSD

Prise de décision dans un environnement incertain
---
**Critère Quantitatifs**
- Laplace : cas de situation equiprobable
- MaxiMin : le meilleure du pire (pour les pessimistes)
- MaxiMax : le meilleure du meilleure (pour les optimistes)
- Hurwitz : Mix ou plutôt généralisation  des deux critères précédent avec l'introduction d'un coefficient d'optimisme
- MiniMax : critère qui minimise le manque à gagner et donc le regret

**Critère Probabilistes**
- Pascal : esperance
- Markowitz : rajoute le critere de dispersion à la méthode de pas**


## Interface Graphique

**Amélioration du code**
- Faire un classe de Poids générale dont PSS,PDD,PDS héritent les uns des autres (2/4)
- Mode visualisation : ajouter le choix de l'engine roadmap visualizer
- Liante et Ciblante de données : ajouter des scrollbars (pour les grands graphes)
- Empecher de pouvoir accéder à l'editeur si le type de graphe n'a pas été renseigné
-Affichage du pcc : n'afficher que la direction concernée et pas les deux fleches en vert

**Débuggage**

- Le pcc ne fonctionne pas pour tous les chemin d'un graphe non fortement connexe (pb propres aux graphes orienté) => soit modifier dijkstra soit imposer des graphes avec des doubles voies partout
Le code erreur : `File "/home/brome/Documents/TIPE/Algorithme.py", line 15, in Autour
    return G.liste[G.sommets.index(S)][1]
ValueError: None is not in list`

- Les pcc ne fonctionnent pas dans tous les cas : `Placer(M,V,acc)
  File "/home/brome/Documents/TIPE/Algorithme.py", line 64, in Placer
    elif P == M and Lignes[-1][G.sommets.index(M)] == G.INF:
  File "/home/brome/Documents/TIPE/Poids.py", line 21, in __eq__
    return self.valeur == w.valeur
AttributeError: 'NoneType' object has no attribute 'valeur'`

**Actuellement**
- Premiere page : mode (ferroviaire,routier) et type de graphe (PSS,PDD,PDS)
- Option : Importer/Sauvegarder (format gbin avec pickle)
- Mode edition : ajout,supression de noeud, importation de lignes (depuis fichier .txt )
- Mode (aperçu et pcc) : detail, fiabilité, temps moyen

## Idées
- Parser/Exporter de données json/gtfs pour lignes de metros
- PCC sans/avec contrainte
- Choix de l'algorithme de PCC
