## Voici les notes que nous prenons suites à nos lectures.

# Thèses - Hizem (Optimisation d'itinéraires dans les réseaux routiers)

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
Critère Quantitatifs:
- Laplace : cas de situation equiprobable
- MaxiMin : le meilleure du pire (pour les pessimistes)
- MaxiMax : le meilleure du meilleure (pour les optimistes)
- Hurwitz : Mix ou plutôt généralisation  des deux critères précédent avec l'introduction d'un coefficient d'optimisme
- MiniMax : critère qui minimise le manque à gagner et donc le regret
Critère Probabilistes:
- Pascal : esperance
- Markowitz : rajoute le critere de dispersion à la méthode de pascal
