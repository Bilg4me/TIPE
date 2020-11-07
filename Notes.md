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

**Idées**
- Premiere page : Mode (ferroviaire,routier)
- Deuxieme page : Type de graphe (PSS,PDD,PDS)
- Option : (Importer/Exporter format excel, Mode edition (ajout,supression de noeud), Mode visualisation (PCC sans/avec contrainte) )

**Actuellement**
- Première ouverture de fenêtre qui demande le type de graphique souhaité et le nombre de villes
- Deuxième ouverture de fenêtre qui demande le nom des villes (Ou alors on le fait dans le tableur de la troisième ouverture)
- Crée / lit un fichier excel à remplir à la main (ouais c'est chiant)
OU ALORS
On passe directement du fichier excel au graphe (on doit quand même le remplir)

## Amélioration du code
- Faire un classe de Poids générale dont PSS,PDD,PDS héritent les uns des autres
- Utiliser un module d'explotation de données gtfs pour les exporter dans un excel afin de ne pas à remplir un graphe à main nue

