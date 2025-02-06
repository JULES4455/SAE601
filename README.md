"# Projet Jupyter Notebook Description" 

Le but du projet est de réaliser une application permettant de visualiser le salaire
Pour ce faire, nous avions un jeu de données de plus de 3000 individus avec plusieurs variables :

- work_year : Année durant laquelle le salaire de l'individu a été enregistré.
- experience_level : Niveau d'expérience de l'individu. Exemple :  "SE" = "Senior".
- employment_type : Type de contrat. Exemple "FT" = "Full-Time".
- job_title : Intitulé du poste occupé par l'individu.
- salary : Salaire brut annuel exprimé dans la devise locale.
- salary_currency : Devise du salaire, ici en euros (€).
- salary_in_usd : Salaire converti en dollars américains (USD) pour standardisation.
- employee_residence  : Pays de résidence de l'individu. Exemple "ES" = "Espagne".
- remote_ratio : Pourcentage de travail effectué à distance. "100" = télétravail total (full remote).
- company_location : Pays où est située l'entreprise.
- company_size : Taille de l'entreprise. "L" = "Large" (grande entreprise).


Pour réaliser cette visualisation, nous avons besoin de plusieurs bibliothèques Python. Chacune joue un rôle spécifique dans le traitement des données, leur analyse et leur affichage interactif. Voici une explication détaillée des bibliothèques utilisées :

1. Bibliothèque os
Cette bibliothèque permet d’interagir avec le système d’exploitation.
Elle est utile pour gérer les fichiers et répertoires, comme le chargement des données depuis un fichier stocké localement.

3. Bibliothèque pandas
Pandas est une bibliothèque essentielle pour la manipulation et l'analyse de données.
Celle-ci permet de lire, transformer, nettoyer et explorer des ensembles de données sous forme de DataFrame, une structure de tableau optimisée pour l'analyse.

4. Bibliothèque numpy
NumPy est utilisée pour les calculs numériques avancés.
Elle permet de manipuler des tableaux (arrays) multidimensionnels et propose des fonctions mathématiques optimisées pour les opérations sur des ensembles de données.

5. Bibliothèque matplotlib.pyplot
Matplotlib est la bibliothèque de base pour la visualisation en Python.
Le module pyplot fournit des fonctions similaires à celles de MATLAB, permettant de tracer des graphiques (histogrammes, courbes, nuages de points, etc.).

6. Bibliothèque seaborn
Seaborn est une extension de Matplotlib qui simplifie la création de graphiques statistiques.
Elle est particulièrement utile pour les visualisations plus esthétiques et détaillées, comme les heatmaps et les boxplots.

8. Bibliothèque streamlit
Streamlit est une bibliothèque qui permet de créer facilement des applications web interactives pour la visualisation et l’analyse des données.
Cette bibliothèque est idéale pour transformer rapidement un script Python en une interface utilisateur accessible via un navigateur.

10. Bibliothèque plotly.express
Plotly est une bibliothèque de visualisation interactive.
Le module plotly.express permet de générer des graphiques dynamiques avec des fonctionnalités comme le zoom, le survol d’informations et les mises à jour en temps réel.

En combinant toutes ces bibliothèques, nous pouvons charger des données, les analyser et les représenter sous forme de visualisations interactives dans une application web intuitive avec Streamlit.
