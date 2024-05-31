from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure
import pandas as pd

# Lire le dataset
file_path = r'C:\Users\Dell\Downloads\africa-millennium-development-goals.xlsx'
df = pd.read_excel(file_path)

# Afficher les colonnes disponibles pour vérifier les noms
print(df.columns)

# Utiliser des noms de colonnes corrects
x_column = 'Date'
y_column = 'Value'

# Créer une source de données pour Bokeh
source = ColumnDataSource(df)

# Créer des graphiques de base
p1 = figure(title="Graphique 1", x_axis_label='Date', y_axis_label='Valeur', x_axis_type='datetime')
p1.line(x=x_column, y=y_column, source=source, line_width=2)

p2 = figure(title="Graphique 2", x_axis_label='Date', y_axis_label='Valeur', x_axis_type='datetime')
p2.line(x=x_column, y=y_column, source=source, line_width=2, color="green")

# Créer une sélection pour l'interactivité
select = Select(title="Sélectionner une colonne", options=list(df.columns), value=y_column)

# Mettre à jour la source de données en fonction de la sélection
def update(attr, old, new):
    selected_column = select.value
    source.data = {x_column: df[x_column], 'y': df[selected_column]}
    p1.title.text = "Graphique de base - " + selected_column

select.on_change('value', update)

# Disposer les éléments du tableau de bord
layout = column(select, p1)

# Ajouter le layout au document Bokeh
curdoc().add_root(layout)
curdoc().title = "Application de visualisation de données"
