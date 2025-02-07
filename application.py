"""
📝 **Instructions** :
- Installez toutes les bibliothèques nécessaires en fonction des imports présents dans le code, utilisez la commande suivante :conda create -n projet python pandas numpy ..........
- Complétez les sections en écrivant votre code où c’est indiqué.
- Ajoutez des commentaires clairs pour expliquer vos choix.
- Utilisez des emoji avec windows + ;
- Interprétez les résultats de vos visualisations (quelques phrases).
"""

### 1. Importation des librairies et chargement des données
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

# Chargement des données
      
df = pd.read_csv("H:/S6/SAE 601/archive/ds_salaries.csv")  #création d'un dataframe avec panda
   
df.head(10) #on affiche les 10 premières lignes



### 2. Exploration visuelle des données
#votre code 
st.title("📊 Visualisation des Salaires en Data Science")
st.markdown("Explorez les tendances des salaires à travers différentes visualisations interactives.")


#if st.checkbox("Afficher un aperçu des données"):
    #st.write(df.....)
# Affichage des premières lignes
df_display = st.checkbox("Afficher un aperçu des données")
if df_display:
    st.write(df.head(10))
    

#Statistique générales avec describe pandas 
#votre code 
st.subheader("📌 Statistiques générales")
st.write(df.describe())

### 3. Distribution des salaires en France par rôle et niveau d'expérience, uilisant px.box et st.plotly_chart
#votre code 
st.subheader("📈 Distribution des salaires en France")
df_france = df[df['company_location'] == 'FR']
fig_box = px.box(df_france, x='experience_level', y='salary_in_usd', color='job_title',
                 title="Distribution des salaires en France par rôle et expérience")
st.plotly_chart(fig_box)

### 4. Analyse des tendances de salaires :
#### Salaire moyen par catégorie : en choisisant une des : ['experience_level', 'employment_type', 'job_title', 'company_location'], utilisant px.bar et st.selectbox 
# Salaire moyen par catégorie
st.subheader("📊 Salaire moyen par catégorie")
option = st.selectbox("Sélectionnez une catégorie", ['experience_level', 'employment_type', 'job_title', 'company_location'])
df_avg = df.groupby(option)['salary_in_usd'].mean().reset_index()
fig_bar = px.bar(df_avg, x=option, y='salary_in_usd', title=f"Salaire moyen par {option}", color=option)
st.plotly_chart(fig_bar)


### 5. Corrélation entre variables
# Sélectionner uniquement les colonnes numériques pour la corrélation
#votre code 

st.subheader("🔗 Corrélations entre variables numériques")
corr_matrix = df[['salary_in_usd', 'remote_ratio', 'work_year']].corr()
fig, ax = plt.subplots()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Calcul de la matrice de corrélation
#votre code


# Affichage du heatmap avec sns.heatmap
#votre code 
st.subheader("🔗 Corrélations entre variables numériques")

### 6. Analyse interactive des variations de salaire
# Une évolution des salaires pour les 10 postes les plus courants
# count of job titles pour selectionner les postes
# calcule du salaire moyen par an
#utilisez px.line
#votre code 
st.subheader("📈 Évolution des salaires des postes les plus courants")
top_jobs = df['job_title'].value_counts().head(10).index
df_top_jobs = df[df['job_title'].isin(top_jobs)]
fig_line = px.line(df_top_jobs, x='work_year', y='salary_in_usd', color='job_title',
                    title="Évolution des salaires des 10 postes les plus courants",
                    markers=True)
fig_line.update_layout(xaxis=dict(tickmode='linear', dtick=1))
st.markdown("<div style='border:2px solid #003366; padding:10px;'>", unsafe_allow_html=True)
st.plotly_chart(fig_line)
st.markdown("</div>", unsafe_allow_html=True)
st.write("Le graphique en ligne est le meilleur pour montrer des évolutions. Celui-ci permet de mettre en évidence des tendance.")

### 7. Salaire médian par expérience et taille d'entreprise
# utilisez median(), px.bar
#votre code 
st.subheader("📊 Salaire médian par expérience et taille d'entreprise")
df_median = df.groupby(['experience_level', 'company_size'])['salary_in_usd'].median().reset_index()
fig_median = px.bar(df_median, x='experience_level', y='salary_in_usd', color='company_size',
                     title="Salaire médian par expérience et taille d'entreprise", barmode='group')
st.markdown("<div style='border:2px solid #003366; padding:10px;'>", unsafe_allow_html=True)
st.plotly_chart(fig_median)
st.markdown("</div>", unsafe_allow_html=True)
st.write("Le graphique en barres groupées permet de comparer facilement les salaires médians en fonction de l'expérience et de la taille de l'entreprise, mettant en évidence les différences entre les groupes.")

#Notre choix:
#Le graphique en barres groupées permet de comparer facilement les salaires médians en fonction de l expérience et de la taille de l entreprise, mettant en évidence les différences entre les groupes.

#Analyse du graphique:
#Sur ce graphqiue, on voit clairement que c'est dans une taille d'entreprise "M" que les salaires médians sont les meilleurs.


### 8. Ajout de filtres dynamiques
#Filtrer les données par salaire utilisant st.slider pour selectionner les plages 
#votre code 

st.subheader("🎚️ Filtrer les données par salaire")
salary_range = st.slider("Sélectionnez la plage de salaire en USD", int(df['salary_in_usd'].min()), int(df['salary_in_usd'].max()), (50000, 150000))
df_filtered = df[(df['salary_in_usd'] >= salary_range[0]) & (df['salary_in_usd'] <= salary_range[1])]
st.write(df_filtered)




### 9.  Impact du télétravail sur le salaire selon le pays
st.subheader("🏠 Impact du télétravail sur le salaire selon le pays")
fig_remote = px.scatter(df, x='company_location', y='salary_in_usd', color='remote_ratio',
                        size='salary_in_usd', title="Impact du télétravail sur le salaire selon le pays")
st.markdown("<div style='border:2px solid #003366; padding:10px;'>", unsafe_allow_html=True)
st.plotly_chart(fig_remote)
st.markdown("</div>", unsafe_allow_html=True)

#Notre choix:
#Le graphique en dispersion permet de visualiser l'impact du télétravail sur les salaires par pays en mettant en évidence la distribution et la concentration des données.

#Analyse du graphique:
#Nos voyons une grosse dispersion notammenment aux Etats-Unis, si nous analysons uniquement ce pays on remarque clairement que les personnes étant en teletravail payent mieux. Ce n'est pas le cas dans tous les pays.



### 10. Filtrage avancé des données avec deux st.multiselect, un qui indique "Sélectionnez le niveau d'expérience" et l'autre "Sélectionnez la taille d'entreprise"
#votre code 

st.subheader("🔍 Filtrage avancé des données")
experience_selected = st.multiselect("Sélectionnez le niveau d'expérience", df['experience_level'].unique())
company_size_selected = st.multiselect("Sélectionnez la taille d'entreprise", df['company_size'].unique())

if experience_selected and company_size_selected:
    df_filtered_advanced = df[(df['experience_level'].isin(experience_selected)) & (df['company_size'].isin(company_size_selected))]
    st.write(df_filtered_advanced)

