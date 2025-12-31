# Génération et réfutation automatique de conjectures en théorie des graphes

## Description
Ce projet a pour objectif d’explorer automatiquement des conjectures en théorie des graphes
et de rechercher des contre-exemples à l’aide d’algorithmes heuristiques inspirés de GraphiTy.

Le programme génère des graphes, calcule différents invariants
(densité, degré moyen, degré maximal, diamètre),
formule des conjectures de type IF / THEN
et cherche automatiquement des graphes qui invalident ces conjectures.

## Fonctionnalités
- Génération de graphes aléatoires
- Calcul d’invariants de graphes
- Recherche de graphes extrêmes (approche GraphiTy)
- Génération automatique de conjectures
- Recherche automatique de contre-exemples

## Organisation du projet
- `graph_utils.py` : outils et invariants sur les graphes
- `graphity.py` : recherche locale de graphes extrêmes
- `conjecture_schema.py` : structure des conjectures
- `evaluator.py` : évaluation logique des conjectures
- `conjecture_generator.py` : génération automatique de conjectures
- `counterexample_search.py` : recherche de contre-exemples
- `main.py` : exécution des expériences

## Exécution
Depuis le dossier `src`, exécuter :
```bash
python main.py

Translated: # Generation and automatic refutation of conjectures in graph theory

## Description

This project aims to automatically explore conjectures in graph theory

And to search for counter-examples using heuristic algorithms inspired by GraphiTy.

The program generates graphs, calculates different invariants

(Density, average degree, maximum degree, diameter),

Formula of IF / THEN type conjectures

And automatically searches for graphs that invalidate these conjectures.

## Features

- Generation of random graphs

- Calculation of graph invariants

- Search for extreme graphs (GraphiTy approach)

- Automatic generation of conjectures

- Automatic search for counter-examples

## Project organization

- `graph_utils.py`: tools and invariants on graphs

- `graphity.py`: local search for extreme graphs

- `conjecture_schema.py`: structure of conjectures

- `evaluator.py`: logical evaluation of conjectures

- `conjecture_generator.py`: automatic generation of conjectures

- `counterexample_search.py`: search for counterexamples

- `main.py`: execution of experiments

## Execution

From the `src` folder, execute:

```bash

Python main.py
test
