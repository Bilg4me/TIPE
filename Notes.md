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
- les nom de graphes à plus de deux lettres posent 2 problemes : la modification de poids entre deux noeuds et le calcul de pcc

**Actuellement**
- Premiere page : mode (ferroviaire,routier) et type de graphe (PSS,PDD,PDS)
- Option : Importer/Sauvegarder (format gbin avec pickle)
- Mode edition : ajout,supression de noeud, importation de lignes (depuis fichier .txt )
- Mode (aperçu et pcc) : detail, fiabilité, temps moyen

## Idées
- Parser/Exporter de données json pour lignes de metros
- PCC sans/avec contrainte
- Choix de l'algorithme de PCC
