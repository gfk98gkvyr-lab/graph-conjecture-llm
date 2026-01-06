# Génération et réfutation automatique de conjectures en théorie des graphes

## Objectif du projet
L’objectif de ce projet n’est pas de démontrer formellement des conjectures en théorie des graphes,
mais de développer un outil expérimental permettant d’explorer automatiquement des espaces de graphes
trop vastes pour une analyse exhaustive.

L’outil génère des conjectures candidates, explore des graphes à l’aide de méthodes heuristiques,
et tente de produire des contre-exemples ou d’observer des tendances empiriques.

## Description
Ce projet propose une approche expérimentale inspirée de l’outil **GraphiTy**.
Le programme génère des graphes, calcule différents invariants (densité, degré moyen,
degré maximal, diamètre), formule des conjectures de type **IF / THEN**,
et recherche automatiquement des graphes qui invalident ces conjectures.

L’absence de contre-exemple ne constitue pas une preuve, mais une validation expérimentale
limitée par les paramètres et le budget de calcul.

## Fonctionnalités
- Génération de graphes aléatoires
- Calcul d’invariants de graphes
- Recherche heuristique de graphes extrêmes (approche GraphiTy)
- Génération automatique de conjectures
- Recherche automatique de contre-exemples
- Sauvegarde des résultats expérimentaux
- Visualisation de graphes

## Organisation du projet
- `graph_utils.py` : outils et calcul d’invariants
- `graphity.py` : recherche locale de graphes extrêmes
- `conjecture_schema.py` : structure des conjectures
- `evaluator.py` : évaluation logique des conjectures
- `conjecture_generator.py` : génération automatique de conjectures
- `counterexample_search.py` : recherche de contre-exemples
- `main.py` : point d’entrée pour exécuter les expériences

## Installation
Python ≥ 3.10 est requis.

Installer les dépendances :
```bash
pip install networkx matplotlib
