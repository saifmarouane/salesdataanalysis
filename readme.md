# Analyse des Ventes

Ce projet consiste en une analyse des données de vente d'une entreprise pour une période donnée. L'objectif est de comprendre le comportement des ventes, d'identifier les produits les plus vendus, et d'extraire des insights basés sur les mois de l'année.

## Table des matières
- [Contexte](#contexte)
- [Fonctionnalités](#fonctionnalités)
- [Technologies Utilisées](#technologies-utilisées)
- [Installation](#installation)
- [Exécution](#exécution)
- [Résultats](#résultats)

## Contexte

L'entreprise souhaite analyser les ventes mensuelles pour comprendre la variation des ventes de produits sur une année complète. Le fichier de données utilisé contient des informations détaillées sur les produits, les quantités vendues, les prix, et les dates des transactions.

## Fonctionnalités

- Nettoyage et préparation des données pour l'analyse.
- Analyse des ventes par mois pour identifier les tendances saisonnières.
- Analyse descriptive des prix par produit.
- Calcul du chiffre d'affaires par mois.
- Visualisation du chiffre d'affaires et des quantités de produits vendus.

## Technologies Utilisées

- Python
- Pandas
- NumPy
- Matplotlib

## Installation


1. Installez les dépendances nécessaires :
    ```bash
    pip install pandas numpy matplotlib
    ```

## Exécution

1. Placez le fichier de données CSV dans le dossier approprié.
2. Exécutez le script Python `analysis.py` pour lancer l'analyse.

    ```bash
    python salesanalysis.py
    ```

## Résultats

L'analyse permet de dégager plusieurs insights intéressants, notamment :

- **Janvier** est le mois avec le plus grand nombre de ventes de produits X.
- Le **prix moyen** des produits est plus élevé en novembre et décembre, probablement en raison des fêtes de fin d'année.
- Le **chiffre d'affaires** maximal a été atteint au mois de décembre.

Les résultats sont visualisés dans des graphiques qui montrent la tendance des ventes sur l'année.

## Auteurs

Ce projet a été développé par saif.

