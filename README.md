# Application-de-visualisation-de-données-sur-un-ensemble-de-données-marocaines
## Description du projet
Le but de ce projet, qui doit être achevé en mai 2024, est de concevoir une application interactive pour visualiser des données en utilisant un ensemble de données marocaines. L'application est développée en utilisant Bokeh, un outil performant qui offre la possibilité de concevoir des applications de visualisation de données interactives en Python. 
## Comment fonctionne l'application
L'application fait appel au serveur Bokeh pour relier Python au navigateur où elle est hébergée. Le serveur Bokeh assure la gestion de toutes les configurations requises afin de garantir un transfert de données adéquat entre le serveur et le client. Le backend crée et remplit les documents avec des mises à jour, puis les sérialise en format JSON à l'aide du backend Bokeh. Par la suite, le client BokehJS envoie et affiche ces documents, offrant ainsi aux utilisateurs la possibilité de consulter l'application dans leur navigateur.
## Comment utiliser l'application
1. Choisissez un ensemble de données marocaines dans le domaine de votre choix (économie, santé, éducation, réseaux sociaux, etc.).
2. Utilisez Pandas ou un autre outil d'exploration de données pour lire et explorer l'ensemble de données. Décrivez l'ensemble de données dans un notebook Jupyter.
3. Créez l'application de visualisation de données avec Bokeh sous forme d'un tableau de bord, en incluant plusieurs graphiques et interactions.
## Dataset
Le dataset utilisé dans cette application provient des objectifs du millénaire pour le développement en Afrique et contient les colonnes suivantes :
- CountryName
- Country
- GoalName
- Goal
- IndicatorName
- Indicator
- Social GroupName
- Social Group
- Units
- Scale
- Frequency
- Date
- Value

## Prérequis
- Python 3.x
- Les bibliothèques Python suivantes :
  - pandas
  - bokeh
