import streamlit as st 
from streamlit_folium import folium_static
import pandas as pd
import numpy as np
from numpy import nan
import re
import numpy as np
from datetime import timedelta
import datetime
import time
import plotly.express as px
from bson import ObjectId
import folium
from folium.plugins import MarkerCluster
from folium.plugins import FloatImage

@st.cache
def load_df(url):
    df = pd.read_csv(url)
    return df

# option
st.set_page_config(page_title="Soliguide 2021 - Mise à jour été",
                   page_icon="https://pbs.twimg.com/profile_images/1321098074765361153/F4UFTeix.png",
                   initial_sidebar_state="expanded")

#############
## sidebar ##
############# 
st.sidebar.image("https://s3.us-west-2.amazonaws.com/secure.notion-static.com/caeabe8c-f726-4dfe-ac9e-aaa9c4099e07/Soliguide_RVB_Original_PurpleOrange4x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210921%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210921T140607Z&X-Amz-Expires=86400&X-Amz-Signature=3021703b71b396e5cf7dc4de84318ef5df3c46df80febb9ccea6d44d255bf447&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Soliguide_RVB_Original_PurpleOrange4x.png%22", use_column_width=True)
st.sidebar.title('Soliguide 2021')
st.sidebar.subheader('Mise à jour été')

categorie = st.sidebar.selectbox("Choisissez votre territoire :", ("France",  "Ile-De-France", "Alpes-Maritimes (06)",
                                            "Gironde (33)",
                                            "Loire-Atlantique (44)", "Bas-Rhin (67)", 
                                            "Paris (75)", "Seine-et-Marne (77)","Yvelines (78)",
                                            "Essonne (91)", "Hauts-de-Seine (92)",
                                            "Seine-Saint-Denis (93)","Val-de-Marne (94)",
                                            "Val-d'Oise (95)"))

##########
## DATA ##
##########

# modifier selon la localisation de la BD
# Importation des fichier .csv en pandas

# Données pour cartes :
df_france = pd.read_csv('ressources/df_france.csv')
df_fiches_IDF = pd.read_csv('ressources/df_IDF.csv')
df_fiches_06 = pd.read_csv('ressources/df_fiches_06.csv')
df_fiches_33 = pd.read_csv('ressources/df_fiches_33.csv')
df_fiches_44 = pd.read_csv('ressources/df_fiches_44.csv')
df_fiches_67 = pd.read_csv('ressources/df_fiches_67.csv')
df_fiches_75 = pd.read_csv('ressources/df_fiches_75.csv')
df_fiches_77 = pd.read_csv('ressources/df_fiches_77.csv')
df_fiches_78 = pd.read_csv('ressources/df_fiches_78.csv')
df_fiches_91 = pd.read_csv('ressources/df_fiches_91.csv')
df_fiches_92 = pd.read_csv('ressources/df_fiches_92.csv')
df_fiches_93 = pd.read_csv('ressources/df_fiches_93.csv')
df_fiches_94 = pd.read_csv('ressources/df_fiches_94.csv')
df_fiches_95 = pd.read_csv('ressources/df_fiches_95.csv')


# Données pour le barchart horizontal:
df_comparaison_France = pd.read_csv('ressources/Fig2.csv')
df_comparaison_IDF = pd.read_csv('ressources/Fig2_IDF.csv')
df_comparaison_06 = pd.read_csv('ressources/Fig2_06.csv')
df_comparaison_33 = pd.read_csv('ressources/Fig2_33.csv')
df_comparaison_44 = pd.read_csv('ressources/Fig2_44.csv')
df_comparaison_67 = pd.read_csv('ressources/Fig2_67.csv')
df_comparaison_75 = pd.read_csv('ressources/Fig2_75.csv')
df_comparaison_77 = pd.read_csv('ressources/Fig2_77.csv')
df_comparaison_78 = pd.read_csv('ressources/Fig2_78.csv')
df_comparaison_91 = pd.read_csv('ressources/Fig2_91.csv')
df_comparaison_92 = pd.read_csv('ressources/Fig2_92.csv')
df_comparaison_93 = pd.read_csv('ressources/Fig2_93.csv')
df_comparaison_94 = pd.read_csv('ressources/Fig2_94.csv')
df_comparaison_95 = pd.read_csv('ressources/Fig2_95.csv')

# Données pour le stacked chart:
df_stacked_per_france = pd.read_csv('ressources/Fig3.csv')
df_stacked_per_IDF = pd.read_csv('ressources/Fig3_IDF.csv')
df_stacked_per_06 = pd.read_csv('ressources/Fig3_06.csv')
df_stacked_per_33 = pd.read_csv('ressources/Fig3_33.csv')
df_stacked_per_44 = pd.read_csv('ressources/Fig3_44.csv')
df_stacked_per_67 = pd.read_csv('ressources/Fig3_67.csv')
df_stacked_per_75 = pd.read_csv('ressources/Fig3_75.csv')
df_stacked_per_77 = pd.read_csv('ressources/Fig3_77.csv')
df_stacked_per_78 = pd.read_csv('ressources/Fig3_78.csv')
df_stacked_per_91 = pd.read_csv('ressources/Fig3_91.csv')
df_stacked_per_92 = pd.read_csv('ressources/Fig3_92.csv')
df_stacked_per_93 = pd.read_csv('ressources/Fig3_93.csv')
df_stacked_per_94 = pd.read_csv('ressources/Fig3_94.csv')
df_stacked_per_95 = pd.read_csv('ressources/Fig3_95.csv')

# Données pour le pie chart:
res_france = pd.read_csv('ressources/Fig4.csv')
res_IDF = pd.read_csv('ressources/Fig4_IDF.csv')
res_06 = pd.read_csv('ressources/Fig4_06.csv')
res_33 = pd.read_csv('ressources/Fig4_33.csv')
res_44 = pd.read_csv('ressources/Fig4_44.csv')
res_67 = pd.read_csv('ressources/Fig4_67.csv')
res_75 = pd.read_csv('ressources/Fig4_75.csv')
res_77 = pd.read_csv('ressources/Fig4_77.csv')
res_78 = pd.read_csv('ressources/Fig4_78.csv')
res_91 = pd.read_csv('ressources/Fig4_91.csv')
res_92 = pd.read_csv('ressources/Fig4_92.csv')
res_93 = pd.read_csv('ressources/Fig4_93.csv')
res_94 = pd.read_csv('ressources/Fig4_94.csv')
res_95 = pd.read_csv('ressources/Fig4_95.csv')

###############
##  FRANCE   ##
###############

if categorie == 'France':
    st.markdown("<center><h1> Soliguide - Mise à jour été 2021</h1></center>", unsafe_allow_html=True)
    st.markdown("Chaque été et chaque hiver, l'équipe de Solinum met à jour la totalité de la base de données de Soliguide sur ses territoires d'implantation, afin d'orienter les publics en situation de précarité au mieux dans ces périodes de changement. Retrouvez ici toutes les statistiques de cette mise à jour été !")  
    
    st.markdown("**Attention**, sur certains grands territoires le dashboard peut mettre quelques minutes à charger : profitez-en pour prendre un café ☕, ça arrive tout de suite.")
                
    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>9 626</font><br><font size='2'>structures en ligne sur Soliguide</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>1 955</font><br/><font size='2'>structures ont fermé<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>491</font><br/><font size='2'>structures ont effectué des changements<br>(du 1<sup>er</sup>juillet au 31 août)</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)

    # Création de la carte avec pour centre : le centre d ela France
    mappy = folium.Map(location=[46.227638, 2.213749],zoom_start=5.8)

    marker_cluster = MarkerCluster().add_to(mappy)

    # Ajout des différents markers :
    for en in range(len(df_france['colors'])):
        folium.CircleMarker([df_france.latitude[en], df_france.longitude[en]],
                            fill = True,
                            color = df_france['colors'][en],
                            radius = 5,
                            fill_color = df_france['colors'][en],
                            tooltip=df_france['Fermeture_Estivale'][en], 
                            popup=df_france['name'][en]
                            ).add_to( mappy )

    url = ('https://raw.githubusercontent.com/Antoine-Carre/Soliguide_majete2021/main/ressources/legend_map_ete.png')
    FloatImage(url, bottom=40, left=70).add_to(mappy)
    
    mappy.save('map.html')

    #Affichage de la carte
    folium_static(mappy)

    # Donnéés traitées pour construire graph 2
    df_comparaison_France['Part de service fermé'] = df_comparaison_France['Part de service fermé'].round(1)

    fig = px.bar(df_comparaison_France.sort_values(by='Part de service fermé', ascending=False).head(10), y="catégorie", x=["ouvert", "Service fermé"],orientation='h', 
                 custom_data=['Part de service fermé'], color_discrete_sequence= [ '#7201a8', '#d8576b']) 

    fig.update_layout(title="<b>Quels sont les services qui ferment le plus pendant l'été ?</b>",
                          margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                            yaxis_title="",
                            xaxis_title="Nombre de services",
                            legend_title="Statut",)
    fig.update_traces(hovertemplate='Catégorie de service: %{y}<br> Nbre de service: %{x}  <br>Taux de fermeture :%{customdata}%') 
    st.plotly_chart(fig, use_container_width=True)

    
    # Donnéés traitées pour construire graph 3

    df_stacked_per_france.rename(columns={'Ouvert':'Service ouvert'}, inplace=True)

    fig = px.bar(df_stacked_per_france, x="Categories", y=["Structure fermée", "Changement d'horaire", "Service fermé", "Service ouvert"], custom_data=['value'],
                text='value', color_discrete_sequence= [ '#7201a8', '#bd3786', '#E65A46', '#2896A0'])
    fig.update_layout(title="<b>Quels impacts a l'été sur les services ?</b>",
                        margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                        legend_title="Status",                     
                        xaxis_title="",
                        yaxis_title="",)
    fig.update_traces(hovertemplate='Catégorie de service: %{x}<br> Proportion :%{customdata}%', texttemplate='%{text}%', textposition='inside') 

    st.plotly_chart(fig, use_container_width=True)

    
    # Donnéés traitées pour construire graph 4
    
    res_france.rename(index={0: 'l\équipe Soliguide', 1:'les acteurs'}, inplace=True)
    
    fig = px.pie(res_france, values='status', names=res_france.index, color_discrete_sequence= [ '#3E3A71', '#E65A46'])
    fig.update_traces(textposition='inside', textinfo='percent+label',\
                     hovertemplate = "%{value} structures mises à jour par %{label}")
    fig.update_layout(title="<b>Qui a mis à jour les structures pendant l'été ?</b>",
                      margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,)

    st.plotly_chart(fig, use_container_width=True)

    

    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>6 000</font><br><font size='2'>e-mails et relances envoyées</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>5 678</font><br/><font size='2'>appels effectués<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>100 %</font><br/><font size='2'>de la base de données mise à jour cet été</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)    
    

#####################
##  ILE DE FRANCE  ##
#####################

if categorie == 'Ile-De-France':
    st.markdown("<center><h1> Soliguide - Mise à jour été 2021 en Île-de-France</h1></center>", unsafe_allow_html=True)
    st.markdown("Chaque été et chaque hiver, l'équipe de Solinum met à jour la totalité de la base de données de Soliguide sur ses territoires d'implantation, afin d'orienter les publics en situation de précarité au mieux dans ces périodes de changement. Retrouvez ici toutes les statistiques de cette mise à jour été !")


    st.markdown("**Attention**, sur certains grands territoires le dashboard peut mettre quelques minutes à charger : profitez-en pour prendre un café ☕, ça arrive tout de suite.")
                
    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>7 197</font><br><font size='2'>structures en ligne sur Soliguide</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>1 533</font><br/><font size='2'>structures ont fermé<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>332</font><br/><font size='2'>structures ont effectué des changements<br>(du 1<sup>er</sup>juillet au 31 août)</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)


    # Création de la carte avec pour centre : le centre d ela France
    mappy = folium.Map(location=[df_fiches_IDF.latitude[0], df_fiches_IDF.longitude[0]],zoom_start=8.5)

    marker_cluster = MarkerCluster().add_to(mappy)

    # Ajout des différents markers :
    for en in range(len(df_fiches_IDF['colors'])):
        folium.CircleMarker([df_fiches_IDF.latitude[en], df_fiches_IDF.longitude[en]],
                            fill = True,
                            color = df_fiches_IDF['colors'][en],
                            radius = 5,
                            fill_color = df_fiches_IDF['colors'][en],
                            tooltip=df_fiches_IDF['Fermeture_Estivale'][en], 
                            popup=df_fiches_IDF['name'][en]
                            ).add_to( mappy )

    url = ('https://raw.githubusercontent.com/Antoine-Carre/Soliguide_majete2021/main/ressources/legend_map_ete.png')
    FloatImage(url, bottom=65, left=70).add_to(mappy)

    mappy.save('map.html')

    #Affichage de la carte
    folium_static(mappy)


    # Donnéés traitées pour construire graph 2
    df_comparaison_IDF['Part de service fermé'] = df_comparaison_IDF['Part de service fermé'].round(1)

    fig = px.bar(df_comparaison_IDF.head(10).sort_values(by='Part de service fermé', ascending=True), y="catégorie", x=["ouvert", "Service fermé"],orientation='h', 
                 custom_data=['Part de service fermé'], color_discrete_sequence= [ '#7201a8', '#d8576b']) 

    fig.update_layout(title="<b>Quels sont les services qui ferment le plus pendant l'été ?</b>",
                          margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                            yaxis_title="",
                            xaxis_title="Nombre de services",
                            legend_title="Statut",)
    fig.update_traces(hovertemplate='Catégorie de service: %{y}<br> Nbre de service: %{x}  <br>Taux de fermeture :%{customdata}%') 
    st.plotly_chart(fig, use_container_width=True)
 
   # Donnéés traitées pour construire graph 3

    df_stacked_per_IDF.rename(columns={'Ouvert':'Service ouvert'}, inplace=True)

    fig = px.bar(df_stacked_per_IDF, x="Categories", y=["Structure fermée", "Changement d'horaire", "Service fermé", "Service ouvert"], custom_data=['value'],
                text='value', color_discrete_sequence= [ '#7201a8', '#bd3786', '#E65A46', '#2896A0'])
    fig.update_layout(title="<b>Quels impacts a l'été sur les services ?</b>",
                        margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                        legend_title="Status",                     
                        xaxis_title="",
                        yaxis_title="",)
    fig.update_traces(hovertemplate='Catégorie de service: %{x}<br> Proportion :%{customdata}%', texttemplate='%{text}%', textposition='inside') 

    st.plotly_chart(fig, use_container_width=True)

    # Donnéés traitées pour construire graph 4
    
    res_IDF.rename(index={0: 'l\'équipe Soliguide', 1:'les acteurs'}, inplace=True)
    
    fig = px.pie(res_IDF, values='status', names=res_IDF.index, color_discrete_sequence= [ '#3E3A71', '#E65A46'])
    fig.update_traces(textposition='inside', textinfo='percent+label',\
                     hovertemplate = "%{value} structures mises à jour par %{label}")
    fig.update_layout(title="<b>Qui a mis à jour les structures pendant l'été ?</b>",
                      margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,)

    st.plotly_chart(fig, use_container_width=True)
    

    col1, col2, col3 = st.columns(3)

    html_string = "<center><font color='#3E3A71' face='Helvetica' size='6'>4 351</font><br><font size='2'>e-mails et relances envoyées</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font color='#3E3A71' face='Helvetica' size='6'>4 376</font><br/><font size='2'>appels effectués<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>100 %</font><br/><font size='2'>de la base de données mise à jour cet été</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)    
    

#######################
##  ALPES MARITIMES  ##
#######################

if categorie == 'Alpes-Maritimes (06)':
    st.markdown("<center><h1> Soliguide - Mise à jour été 2021 en Alpes-Maritimes</h1></center>", unsafe_allow_html=True)
    st.markdown("Chaque été et chaque hiver, l'équipe de Solinum met à jour la totalité de la base de données de Soliguide sur ses territoires d'implantation, afin d'orienter les publics en situation de précarité au mieux dans ces périodes de changement. Retrouvez ici toutes les statistiques de cette mise à jour été !")


    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>341</font><br><font size='2'>structures en ligne sur Soliguide</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>17</font><br/><font size='2'>structures ont fermé<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>2</font><br/><font size='2'>structures ont effectué des changements<br>(du 1<sup>er</sup>juillet au 31 août)</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)

    # Création de la carte avec pour centre : le centre d ela France
    mappy = folium.Map(location=[df_fiches_06.latitude[0], df_fiches_06.longitude[0]],zoom_start=8.5)

    marker_cluster = MarkerCluster().add_to(mappy)

    # Ajout des différents markers :
    for en in range(len(df_fiches_06['colors'])):
        folium.CircleMarker([df_fiches_06.latitude[en], df_fiches_06.longitude[en]],
        fill = True,
        color = df_fiches_06['colors'][en],
        radius = 5,
        fill_color = df_fiches_06['colors'][en],
        tooltip=df_fiches_06['Fermeture_Estivale'][en], 
        popup=df_fiches_06['name'][en]
        ).add_to( mappy )
        
    url = ('https://raw.githubusercontent.com/Antoine-Carre/Soliguide_majete2021/main/ressources/legend_map_ete.png')
    FloatImage(url, bottom=65, left=70).add_to(mappy)
        
    mappy.save('map.html')

    #Affichage de la carte
    folium_static(mappy)

    # Donnéés traitées pour construire graph 2
    df_comparaison_06['Part de service fermé'] = df_comparaison_06['Part de service fermé'].round(1)

    fig = px.bar(df_comparaison_06.sort_values(by='Part de service fermé', ascending=False).head(10), y="catégorie", x=["ouvert", "Service fermé"],orientation='h', 
                 custom_data=['Part de service fermé'], color_discrete_sequence= [ '#7201a8', '#d8576b']) 

    fig.update_layout(title="<b>Quels sont les services qui ferment le plus pendant l'été ?</b>",
                          margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                            yaxis_title="",
                            xaxis_title="Nombre de services",
                            legend_title="Statut",)
    fig.update_traces(hovertemplate='Catégorie de service: %{y}<br> Nbre de service: %{x}  <br>Taux de fermeture :%{customdata}%') 
    
    st.plotly_chart(fig, use_container_width=True)
 
    # Donnéés traitées pour construire graph 3

    df_stacked_per_06.rename(columns={'Ouvert':'Service ouvert'}, inplace=True)

    fig = px.bar(df_stacked_per_06, x="Categories", y=["Structure fermée", "Changement d'horaire", "Service fermé", "Service ouvert"], custom_data=['value'],
                text='value', color_discrete_sequence= [ '#7201a8', '#bd3786', '#E65A46', '#2896A0'])
    fig.update_layout(title="<b>Quels impacts a l'été sur les services ?</b>",
                        margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                        legend_title="Status",                     
                        xaxis_title="",
                        yaxis_title="",)
    fig.update_traces(hovertemplate='Catégorie de service: %{x}<br> Proportion :%{customdata}%', texttemplate='%{text}%', textposition='inside') 

    st.plotly_chart(fig, use_container_width=True)
    
    # Donnéés traitées pour construire graph 4
    
    res_06.rename(index={0: 'l\'équipe Soliguide', 1:'les acteurs'}, inplace=True)
    
    fig = px.pie(res_06, values='status', names=res_06.index, color_discrete_sequence= [ '#3E3A71', '#E65A46'])
    fig.update_traces(textposition='inside', textinfo='percent+label',\
                     hovertemplate = "%{value} structures mises à jour par %{label}")
    fig.update_layout(title="<b>Qui a mis à jour les structures pendant l'été ?</b>",
                      margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,)

    st.plotly_chart(fig, use_container_width=True)


    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>418</font><br><font size='2'>e-mails et relances envoyées</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>158</font><br/><font size='2'>appels effectués<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>100 %</font><br/><font size='2'>de la base de données mise à jour cet été</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"
  
    st.markdown(html_string, unsafe_allow_html=True)                                                                                                                              
    
###############
##  GIRONDE  ##
###############

if categorie == 'Gironde (33)':
    st.markdown("<center><h1> Soliguide - Mise à jour été 2021 en Gironde</h1></center>", unsafe_allow_html=True)
    st.markdown("Chaque été et chaque hiver, l'équipe de Solinum met à jour la totalité de la base de données de Soliguide sur ses territoires d'implantation, afin d'orienter les publics en situation de précarité au mieux dans ces périodes de changement. Retrouvez ici toutes les statistiques de cette mise à jour été !")



    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>885</font><br><font size='2'>structures en ligne sur Soliguide</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>212</font><br/><font size='2'>structures ont fermé<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>69</font><br/><font size='2'>structures ont effectué des changements<br>(du 1<sup>er</sup>juillet au 31 août)</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)

    # Création de la carte avec pour centre : le centre d ela France
    mappy = folium.Map(location=[df_fiches_33.latitude[0], df_fiches_33.longitude[0]],zoom_start=8.5)

    marker_cluster = MarkerCluster().add_to(mappy)

    # Ajout des différents markers :
    for en in range(len(df_fiches_33['colors'])):
        folium.CircleMarker([df_fiches_33.latitude[en], df_fiches_33.longitude[en]],
                            fill = True,
                            color = df_fiches_33['colors'][en],
                            radius = 5,
                            fill_color = df_fiches_33['colors'][en],
                            tooltip=df_fiches_33['Fermeture_Estivale'][en], 
                            popup=df_fiches_33['name'][en]
                            ).add_to( mappy )


    url = ('https://raw.githubusercontent.com/Antoine-Carre/Soliguide_majete2021/main/ressources/legend_map_ete.png')
    FloatImage(url, bottom=65, left=70).add_to(mappy)

    mappy.save('map.html')

    #Affichage de la carte
    folium_static(mappy)
    
    # Donnéés traitées pour construire graph 2
    df_comparaison_33['Part de service fermé'] = df_comparaison_33['Part de service fermé'].round(1)

    fig = px.bar(df_comparaison_33.sort_values(by='Part de service fermé', ascending=False).head(10), y="catégorie", x=["ouvert", "Service fermé"],orientation='h', 
                 custom_data=['Part de service fermé'], color_discrete_sequence= [ '#7201a8', '#d8576b']) 

    fig.update_layout(title="<b>Quels sont les services qui ferment le plus pendant l'été ?</b>",
                          margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                            yaxis_title="",
                            xaxis_title="Nombre de services",
                            legend_title="Statut",)
    fig.update_traces(hovertemplate='Catégorie de service: %{y}<br> Nbre de service: %{x}  <br>Taux de fermeture :%{customdata}%') 
    st.plotly_chart(fig, use_container_width=True)
    
    
    # Donnéés traitées pour construire graph 3

    df_stacked_per_33.rename(columns={'Ouvert':'Service ouvert'}, inplace=True)

    fig = px.bar(df_stacked_per_33, x="Categories", y=["Structure fermée", "Changement d'horaire", "Service fermé", "Service ouvert"], custom_data=['value'],
                text='value', color_discrete_sequence= [ '#7201a8', '#bd3786', '#E65A46', '#2896A0'])
    fig.update_layout(title="<b>Quels impacts a l'été sur les services ?</b>",
                        margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                        legend_title="Status",                     
                        xaxis_title="",
                        yaxis_title="",)
    fig.update_traces(hovertemplate='Catégorie de service: %{x}<br> Proportion :%{customdata}%', texttemplate='%{text}%', textposition='inside') 

    st.plotly_chart(fig, use_container_width=True)
    
    # Donnéés traitées pour construire graph 4
    
    res_33.rename(index={0: 'l\'équipe Soliguide', 1:'les acteurs'}, inplace=True)
    
    fig = px.pie(res_33, values='status', names=res_33.index, color_discrete_sequence= [ '#3E3A71', '#E65A46'])
    fig.update_traces(textposition='inside', textinfo='percent+label',\
                     hovertemplate = "%{value} structures mises à jour par %{label}")
    fig.update_layout(title="<b>Qui a mis à jour les structures pendant l'été ?</b>",
                      margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,)

    st.plotly_chart(fig, use_container_width=True)
    
    
    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>597</font><br><font size='2'>e-mails et relances envoyées</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>375</font><br/><font size='2'>appels effectués<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>100 %</font><br/><font size='2'>de la base de données mise à jour cet été</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)  


########################
##  LOIRE ATLANTIQUE  ##
########################

if categorie == 'Loire-Atlantique (44)':
    st.markdown("<center><h1> Soliguide - Mise à jour été 2021 en Loire-Atlantique</h1></center>", unsafe_allow_html=True)
    st.markdown("Chaque été et chaque hiver, l'équipe de Solinum met à jour la totalité de la base de données de Soliguide sur ses territoires d'implantation, afin d'orienter les publics en situation de précarité au mieux dans ces périodes de changement. Retrouvez ici toutes les statistiques de cette mise à jour été !")



    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>921</font><br><font size='2'>structures en ligne sur Soliguide</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>147</font><br/><font size='2'>structures ont fermé<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>58</font><br/><font size='2'>structures ont effectué des changements<br>(du 1<sup>er</sup>juillet au 31 août)</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)

   
    # Création de la carte avec pour centre : le centre d ela France
    mappy = folium.Map(location=[df_fiches_44.latitude[0], df_fiches_44.longitude[0]],zoom_start=8.2)

    marker_cluster = MarkerCluster().add_to(mappy)

    # Ajout des différents markers :
    for en in range(len(df_fiches_33['colors'])):
        folium.CircleMarker([df_fiches_44.latitude[en], df_fiches_44.longitude[en]],
                            fill = True,
                            color = df_fiches_44['colors'][en],
                            radius = 5,
                            fill_color = df_fiches_44['colors'][en],
                            tooltip=df_fiches_44['Fermeture_Estivale'][en], 
                            popup=df_fiches_44['name'][en]
                            ).add_to( mappy )


    url = ('https://raw.githubusercontent.com/Antoine-Carre/Soliguide_majete2021/main/ressources/legend_map_ete.png')
    FloatImage(url, bottom=65, left=70).add_to(mappy)
        
    mappy.save('map.html')

    #Affichage de la carte
    folium_static(mappy)
    
    # Donnéés traitées pour construire graph 2
    df_comparaison_44['Part de service fermé'] = df_comparaison_44['Part de service fermé'].round(1)

    fig = px.bar(df_comparaison_44.sort_values(by='Part de service fermé', ascending=False).head(10), y="catégorie", x=["ouvert", "Service fermé"],orientation='h', 
                 custom_data=['Part de service fermé'], color_discrete_sequence= [ '#7201a8', '#d8576b']) 

    fig.update_layout(title="<b>Quels sont les services qui ferment le plus pendant l'été ?</b>",
                          margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                            yaxis_title="",
                            xaxis_title="Nombre de services",
                            legend_title="Statut",)
    fig.update_traces(hovertemplate='Catégorie de service: %{y}<br> Nbre de service: %{x}  <br>Taux de fermeture :%{customdata}%') 
    st.plotly_chart(fig, use_container_width=True)

    # Donnéés traitées pour construire graph 3

    df_stacked_per_44.rename(columns={'Ouvert':'Service ouvert'}, inplace=True)

    fig = px.bar(df_stacked_per_44, x="Categories", y=["Structure fermée", "Changement d'horaire", "Service fermé", "Service ouvert"], custom_data=['value'],
                text='value', color_discrete_sequence= [ '#7201a8', '#bd3786', '#E65A46', '#2896A0'])
    fig.update_layout(title="<b>Quels impacts a l'été sur les services ?</b>",
                        margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                        legend_title="Status",                     
                        xaxis_title="",
                        yaxis_title="",)
    fig.update_traces(hovertemplate='Catégorie de service: %{x}<br> Proportion :%{customdata}%', texttemplate='%{text}%', textposition='inside') 

    st.plotly_chart(fig, use_container_width=True)

    
    # Donnéés traitées pour construire graph 4
    
    res_44.rename(index={0: 'l\'équipe Soliguide', 1:'les acteurs'}, inplace=True)
    
    fig = px.pie(res_44, values='status', names=res_44.index, color_discrete_sequence= [ '#3E3A71', '#E65A46'])
    fig.update_traces(textposition='inside', textinfo='percent+label',\
                     hovertemplate = "%{value} structures mises à jour par %{label}")
        
    fig.update_layout(title="<b>Qui a mis à jour les structures pendant l'été ?</b>",
                      margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,)

    st.plotly_chart(fig, use_container_width=True)
    
      
    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>767</font><br><font size='2'>e-mails et relances envoyées</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>215</font><br/><font size='2'>appels effectués<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>100 %</font><br/><font size='2'>de la base de données mise à jour cet été</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)  


################
##  BAS-RHIN  ##
################

if categorie == 'Bas-Rhin (67)':
    st.markdown("<center><h1> Soliguide - Mise à jour été 2021 dans le Bas-Rhin</h1></center>", unsafe_allow_html=True)
    st.markdown("Chaque été et chaque hiver, l'équipe de Solinum met à jour la totalité de la base de données de Soliguide sur ses territoires d'implantation, afin d'orienter les publics en situation de précarité au mieux dans ces périodes de changement. Retrouvez ici toutes les statistiques de cette mise à jour été !")


    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)


    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>252</font><br><font size='2'>structures en ligne sur Soliguide</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>46</font><br/><font size='2'>structures ont fermé<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>30</font><br/><font size='2'>structures ont effectué des changements<br>(du 1<sup>er</sup>juillet au 31 août)</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)

 
    # Création de la carte avec pour centre : le centre d ela France
    mappy = folium.Map(location=[df_fiches_67.latitude[0], df_fiches_67.longitude[0]],zoom_start=11)

    marker_cluster = MarkerCluster().add_to(mappy)

    # Ajout des différents markers :
    for en in range(len(df_fiches_67['colors'])):
        folium.CircleMarker([df_fiches_67.latitude[en], df_fiches_67.longitude[en]],
                            fill = True,
                            color = df_fiches_67['colors'][en],
                            radius = 5,
                            fill_color = df_fiches_67['colors'][en],
                            tooltip=df_fiches_67['Fermeture_Estivale'][en], 
                            popup=df_fiches_67['name'][en]
                            ).add_to( mappy )

    url = ('https://raw.githubusercontent.com/Antoine-Carre/Soliguide_majete2021/main/ressources/legend_map_ete.png')
    FloatImage(url, bottom=65, left=70).add_to(mappy)
        
    mappy.save('map.html')

    #Affichage de la carte
    folium_static(mappy)

     # Donnéés traitées pour construire graph 2
    df_comparaison_67['Part de service fermé'] = df_comparaison_67['Part de service fermé'].round(1)

    fig = px.bar(df_comparaison_67.sort_values(by='Part de service fermé', ascending=False).head(10), y="catégorie", x=["ouvert", "Service fermé"],orientation='h', 
                 custom_data=['Part de service fermé'], color_discrete_sequence= [ '#7201a8', '#d8576b']) 

    fig.update_layout(title="<b>Quels sont les services qui ferment le plus pendant l'été ?</b>",
                          margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                            yaxis_title="",
                            xaxis_title="Nombre de services",
                            legend_title="Statut",)
    fig.update_traces(hovertemplate='Catégorie de service: %{y}<br> Nbre de service: %{x}  <br>Taux de fermeture :%{customdata}%') 
    
    st.plotly_chart(fig, use_container_width=True)

    # Donnéés traitées pour construire graph 3

    df_stacked_per_67.rename(columns={'Ouvert':'Service ouvert'}, inplace=True)

    fig = px.bar(df_stacked_per_67, x="Categories", y=["Structure fermée", "Changement d'horaire", "Service fermé", "Service ouvert"], custom_data=['value'],
                text='value', color_discrete_sequence= [ '#7201a8', '#bd3786', '#E65A46', '#2896A0'])
    fig.update_layout(title="<b>Quels impacts a l'été sur les services ?</b>",
                        margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                        legend_title="Status",                     
                        xaxis_title="",
                        yaxis_title="",)
    fig.update_traces(hovertemplate='Catégorie de service: %{x}<br> Proportion :%{customdata}%', texttemplate='%{text}%', textposition='inside') 

    st.plotly_chart(fig, use_container_width=True)

    # Donnéés traitées pour construire graph 4
    
    res_67.rename(index={0: 'l\'équipe Soliguide', 1:'les acteurs'}, inplace=True)
    
    fig = px.pie(res_67, values='status', names=res_67.index, color_discrete_sequence= [ '#3E3A71', '#E65A46'])
    fig.update_traces(textposition='inside', textinfo='percent+label',\
                     hovertemplate = "%{value} structures mises à jour par %{label}")
    fig.update_layout(title="<b>Qui a mis à jour les structures pendant l'été ?</b>",
                      margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,)

    st.plotly_chart(fig, use_container_width=True)
    

    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>245</font><br><font size='2'>e-mails et relances envoyées</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>176</font><br/><font size='2'>appels effectués<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>100 %</font><br/><font size='2'>de la base de données mise à jour cet été</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)  

    
################
##  PARIS  ##
################

if categorie == 'Paris (75)':
    st.markdown("<center><h1> Soliguide - Mise à jour été 2021 à Paris</h1></center>", unsafe_allow_html=True)
    st.markdown("Chaque été et chaque hiver, l'équipe de Solinum met à jour la totalité de la base de données de Soliguide sur ses territoires d'implantation, afin d'orienter les publics en situation de précarité au mieux dans ces périodes de changement. Retrouvez ici toutes les statistiques de cette mise à jour été !")



    st.markdown("**Attention**, sur certains grands territoires le dashboard peut mettre quelques minutes à charger : profitez-en pour prendre un café ☕, ça arrive tout de suite.")
                
    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>2 448</font><br><font size='2'>structures en ligne sur Soliguide</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>361</font><br/><font size='2'>structures ont fermé<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>46</font><br/><font size='2'>structures ont effectué des changements<br>(du 1<sup>er</sup>juillet au 31 août)</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)

  
    # Création de la carte avec pour centre : le centre d ela France
    mappy = folium.Map(location=[48.856614, 2.3522219],zoom_start=12.1)

    marker_cluster = MarkerCluster().add_to(mappy)

    # Ajout des différents markers :
    for en in range(len(df_fiches_75['colors'])):
        folium.CircleMarker([df_fiches_75.latitude[en], df_fiches_75.longitude[en]],
                            fill = True,
                            color = df_fiches_75['colors'][en],
                            radius = 5,
                            fill_color = df_fiches_75['colors'][en],
                            tooltip=df_fiches_75['Fermeture_Estivale'][en], 
                            popup=df_fiches_75['name'][en]
                            ).add_to( mappy )


    url = ('https://raw.githubusercontent.com/Antoine-Carre/Soliguide_majete2021/main/ressources/legend_map_ete.png')
    FloatImage(url, bottom=65, left=70).add_to(mappy)
 
    mappy.save('map.html')

    #Affichage de la carte
    folium_static(mappy)

     # Donnéés traitées pour construire graph 2
    df_comparaison_75['Part de service fermé'] = df_comparaison_75['Part de service fermé'].round(1)

    fig = px.bar(df_comparaison_75.sort_values(by='Part de service fermé', ascending=False).head(10), y="catégorie", x=["ouvert", "Service fermé"],orientation='h', 
                 custom_data=['Part de service fermé'], color_discrete_sequence= [ '#7201a8', '#d8576b']) 

    fig.update_layout(title="<b>Quels sont les services qui ferment le plus pendant l'été ?</b>",
                          margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                            yaxis_title="",
                            xaxis_title="Nombre de services",
                            legend_title="Statut",)
    fig.update_traces(hovertemplate='Catégorie de service: %{y}<br> Nbre de service: %{x}  <br>Taux de fermeture :%{customdata}%') 
    st.plotly_chart(fig, use_container_width=True)

    # Donnéés traitées pour construire graph 3

    df_stacked_per_75.rename(columns={'Ouvert':'Service ouvert'}, inplace=True)

    fig = px.bar(df_stacked_per_75, x="Categories", y=["Structure fermée", "Changement d'horaire", "Service fermé", "Service ouvert"], custom_data=['value'],
                text='value', color_discrete_sequence= [ '#7201a8', '#bd3786', '#E65A46', '#2896A0'])
    fig.update_layout(title="<b>Quels impacts a l'été sur les services ?</b>",
                        margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                        legend_title="Status",                     
                        xaxis_title="",
                        yaxis_title="",)
    fig.update_traces(hovertemplate='Catégorie de service: %{x}<br> Proportion :%{customdata}%', texttemplate='%{text}%', textposition='inside') 

    st.plotly_chart(fig, use_container_width=True)

    
    # Donnéés traitées pour construire graph 4
    
    res_75.rename(index={0: 'l\'équipe Soliguide', 1:'les acteurs'}, inplace=True)
    
    fig = px.pie(res_75, values='status', names=res_75.index, color_discrete_sequence= [ '#3E3A71', '#E65A46'])
    fig.update_traces(textposition='inside', textinfo='percent+label',\
                     hovertemplate = "%{value} structures mises à jour par %{label}")
    fig.update_layout(title="<b>Qui a mis à jour les structures pendant l'été ?</b>",
                      margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,)

    st.plotly_chart(fig, use_container_width=True)

    
    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>1 259</font><br><font size='2'>e-mails et relances envoyées</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>1 365</font><br/><font size='2'>appels effectués<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>100 %</font><br/><font size='2'>de la base de données mise à jour cet été</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)  



######################
##  SEINE-ET-MARNE  ##
######################

if categorie == 'Seine-et-Marne (77)':
    st.markdown("<center><h1> Soliguide - Mise à jour été 2021 en Seine-et-Marne</h1></center>", unsafe_allow_html=True)
    st.markdown("Chaque été et chaque hiver, l'équipe de Solinum met à jour la totalité de la base de données de Soliguide sur ses territoires d'implantation, afin d'orienter les publics en situation de précarité au mieux dans ces périodes de changement. Retrouvez ici toutes les statistiques de cette mise à jour été !")



    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)


    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>127</font><br><font size='2'>structures en ligne sur Soliguide</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>5</font><br/><font size='2'>structures ont fermé<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>5</font><br/><font size='2'>structures ont effectué des changements<br>(du 1<sup>er</sup>juillet au 31 août)</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)
   
    # Création de la carte avec pour centre : le centre d ela France
    mappy = folium.Map(location=[df_fiches_77.latitude[0], df_fiches_77.longitude[0]],zoom_start=8.2)

    marker_cluster = MarkerCluster().add_to(mappy)

    # Ajout des différents markers :
    for en in range(len(df_fiches_77['colors'])):
        folium.CircleMarker([df_fiches_77.latitude[en], df_fiches_77.longitude[en]],
                            fill = True,
                            color = df_fiches_77['colors'][en],
                            radius = 5,
                            fill_color = df_fiches_77['colors'][en],
                            tooltip=df_fiches_77['Fermeture_Estivale'][en], 
                            popup=df_fiches_77['name'][en]
                            ).add_to( mappy )


    url = ('https://raw.githubusercontent.com/Antoine-Carre/Soliguide_majete2021/main/ressources/legend_map_ete.png')
    FloatImage(url, bottom=65, left=70).add_to(mappy)
 
    mappy.save('map.html')

    #Affichage de la carte
    folium_static(mappy)

     # Donnéés traitées pour construire graph 2
    df_comparaison_77['Part de service fermé'] = df_comparaison_77['Part de service fermé'].round(1)

    fig = px.bar(df_comparaison_77.sort_values(by='Part de service fermé', ascending=False).head(10), y="catégorie", x=["ouvert", "Service fermé"],orientation='h', 
                 custom_data=['Part de service fermé'], color_discrete_sequence= [ '#7201a8', '#d8576b']) 

    fig.update_layout(title="<b>Quels sont les services qui ferment le plus pendant l'été ?</b>",
                          margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                            yaxis_title="",
                            xaxis_title="Nombre de services",
                            legend_title="Statut",)
    fig.update_traces(hovertemplate='Catégorie de service: %{y}<br> Nbre de service: %{x}  <br>Taux de fermeture :%{customdata}%') 
    st.plotly_chart(fig, use_container_width=True)



    # Donnéés traitées pour construire graph 3

    df_stacked_per_77.rename(columns={'Ouvert':'Service ouvert'}, inplace=True)

    fig = px.bar(df_stacked_per_77, x="Categories", y=["Structure fermée", "Changement d'horaire", "Service fermé", "Service ouvert"], custom_data=['value'],
                text='value', color_discrete_sequence= [ '#7201a8', '#bd3786', '#E65A46', '#2896A0'])
    fig.update_layout(title="<b>Quels impacts a l'été sur les services ?</b>",
                        margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                        legend_title="Status",                     
                        xaxis_title="",
                        yaxis_title="",)
    fig.update_traces(hovertemplate='Catégorie de service: %{x}<br> Proportion :%{customdata}%', texttemplate='%{text}%', textposition='inside') 

    st.plotly_chart(fig, use_container_width=True)

       
    # Donnéés traitées pour construire graph 3
    res_77.rename(index={0: 'l\'équipe Soliguide', 1:'les acteurs'}, inplace=True)
    
    fig = px.pie(res_77, values='status', names=res_77.index, color_discrete_sequence= [ '#3E3A71', '#E65A46'])
    fig.update_traces(textposition='inside', textinfo='percent+label',\
                     hovertemplate = "%{value} structures mises à jour par %{label}")
    fig.update_layout(title="<b>Qui a mis à jour les structures pendant l'été ?</b>",
                      margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,)

    st.plotly_chart(fig, use_container_width=True)

 
    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>11</font><br><font size='2'>e-mails et relances envoyées</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>403</font><br/><font size='2'>appels effectués<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>100 %</font><br/><font size='2'>de la base de données mise à jour cet été</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)  

    
################
##  YVELINES  ##
################

if categorie == 'Yvelines (78)':
    st.markdown("<center><h1> Soliguide - Mise à jour été 2021 dans les Yvelines</h1></center>", unsafe_allow_html=True)
    st.markdown("Chaque été et chaque hiver, l'équipe de Solinum met à jour la totalité de la base de données de Soliguide sur ses territoires d'implantation, afin d'orienter les publics en situation de précarité au mieux dans ces périodes de changement. Retrouvez ici toutes les statistiques de cette mise à jour été !")



    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>829</font><br><font size='2'>structures en ligne sur Soliguide</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>174</font><br/><font size='2'>structures ont fermé<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>31</font><br/><font size='2'>structures ont effectué des changements<br>(du 1<sup>er</sup>juillet au 31 août)</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)
 
    # Création de la carte avec pour centre : le centre d ela France
    mappy = folium.Map(location=[df_fiches_78.latitude[0], df_fiches_78.longitude[0]],zoom_start=8.5)

    marker_cluster = MarkerCluster().add_to(mappy)

    # Ajout des différents markers :
    for en in range(len(df_fiches_78['colors'])):
        folium.CircleMarker([df_fiches_78.latitude[en], df_fiches_78.longitude[en]],
                            fill = True,
                            color = df_fiches_78['colors'][en],
                            radius = 5,
                            fill_color = df_fiches_78['colors'][en],
                            tooltip=df_fiches_78['Fermeture_Estivale'][en], 
                            popup=df_fiches_78['name'][en]
                            ).add_to( mappy )

    url = ('https://raw.githubusercontent.com/Antoine-Carre/Soliguide_majete2021/main/ressources/legend_map_ete.png')
    FloatImage(url, bottom=65, left=70).add_to(mappy)

    mappy.save('map.html')

    #Affichage de la carte
    folium_static(mappy)


     # Donnéés traitées pour construire graph 2
    df_comparaison_78['Part de service fermé'] = df_comparaison_78['Part de service fermé'].round(1)

    fig = px.bar(df_comparaison_78.sort_values(by='Part de service fermé', ascending=False).head(10), y="catégorie", x=["ouvert", "Service fermé"],orientation='h', 
                 custom_data=['Part de service fermé'], color_discrete_sequence= [ '#7201a8', '#d8576b']) 

    fig.update_layout(title="<b>Quels sont les services qui ferment le plus pendant l'été ?</b>",
                          margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                            yaxis_title="",
                            xaxis_title="Nombre de services",
                            legend_title="Statut",)
    fig.update_traces(hovertemplate='Catégorie de service: %{y}<br> Nbre de service: %{x}  <br>Taux de fermeture :%{customdata}%') 
    st.plotly_chart(fig, use_container_width=True)



    # Donnéés traitées pour construire graph 3

    df_stacked_per_78.rename(columns={'Ouvert':'Service ouvert'}, inplace=True)

    fig = px.bar(df_stacked_per_78, x="Categories", y=["Structure fermée", "Changement d'horaire", "Service fermé", "Service ouvert"], custom_data=['value'],
                text='value', color_discrete_sequence= [ '#7201a8', '#bd3786', '#E65A46', '#2896A0'])
    fig.update_layout(title="<b>Quels impacts a l'été sur les services ?</b>",
                        margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                        legend_title="Status",                     
                        xaxis_title="",
                        yaxis_title="",)
    fig.update_traces(hovertemplate='Catégorie de service: %{x}<br> Proportion :%{customdata}%', texttemplate='%{text}%', textposition='inside') 

    st.plotly_chart(fig, use_container_width=True)
       
    # Donnéés traitées pour construire graph 4
    res_78.rename(index={0: 'l\'équipe Soliguide', 1:'les acteurs'}, inplace=True)
    
    fig = px.pie(res_78, values='status', names=res_78.index, color_discrete_sequence= [ '#3E3A71', '#E65A46'])
    fig.update_traces(textposition='inside', textinfo='percent+label',\
                     hovertemplate = "%{value} structures mises à jour par %{label}")
    fig.update_layout(title="<b>Qui a mis à jour les structures pendant l'été ?</b>",
                      margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,)

    st.plotly_chart(fig, use_container_width=True)



    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>677</font><br><font size='2'>e-mails et relances envoyées</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>331</font><br/><font size='2'>appels effectués<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>100 %</font><br/><font size='2'>de la base de données mise à jour cet été</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)      
                                                                                                                                                   
################
##  ESSONNE  ##
################

if categorie == 'Essonne (91)':
    st.markdown("<center><h1> Soliguide - Mise à jour été 2021 dans l'Essonne</h1></center>", unsafe_allow_html=True)
    st.markdown("Chaque été et chaque hiver, l'équipe de Solinum met à jour la totalité de la base de données de Soliguide sur ses territoires d'implantation, afin d'orienter les publics en situation de précarité au mieux dans ces périodes de changement. Retrouvez ici toutes les statistiques de cette mise à jour été !")



    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>194</font><br><font size='2'>structures en ligne sur Soliguide</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>36</font><br/><font size='2'>structures ont fermé<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>10</font><br/><font size='2'>structures ont effectué des changements<br>(du 1<sup>er</sup>juillet au 31 août)</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)
 
    # Création de la carte avec pour centre : le centre d ela France
    mappy = folium.Map(location=[df_fiches_91.latitude[0], df_fiches_91.longitude[0]],zoom_start=9.5)

    marker_cluster = MarkerCluster().add_to(mappy)

    # Ajout des différents markers :
    for en in range(len(df_fiches_91['colors'])):
        folium.CircleMarker([df_fiches_91.latitude[en], df_fiches_91.longitude[en]],
                            fill = True,
                            color = df_fiches_91['colors'][en],
                            radius = 5,
                            fill_color = df_fiches_91['colors'][en],
                            tooltip=df_fiches_91['Fermeture_Estivale'][en], 
                            popup=df_fiches_91['name'][en]
                            ).add_to( mappy )

    url = ('https://raw.githubusercontent.com/Antoine-Carre/Soliguide_majete2021/main/ressources/legend_map_ete.png')
    FloatImage(url, bottom=65, left=70).add_to(mappy)
 
    mappy.save('map.html')

    #Affichage de la carte
    folium_static(mappy)

     # Donnéés traitées pour construire graph 2
    df_comparaison_91['Part de service fermé'] = df_comparaison_91['Part de service fermé'].round(1)

    fig = px.bar(df_comparaison_91.sort_values(by='Part de service fermé', ascending=False).head(10), y="catégorie", x=["ouvert", "Service fermé"],orientation='h', 
                 custom_data=['Part de service fermé'], color_discrete_sequence= [ '#7201a8', '#d8576b']) 

    fig.update_layout(title="<b>Quels sont les services qui ferment le plus pendant l'été ?</b>",
                          margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                            yaxis_title="",
                            xaxis_title="Nombre de services",
                            legend_title="Statut",)
    fig.update_traces(hovertemplate='Catégorie de service: %{y}<br> Nbre de service: %{x}  <br>Taux de fermeture :%{customdata}%') 
    st.plotly_chart(fig, use_container_width=True)


    # Donnéés traitées pour construire graph 3

    df_stacked_per_91.rename(columns={'Ouvert':'Service ouvert'}, inplace=True)

    fig = px.bar(df_stacked_per_91, x="Categories", y=["Structure fermée", "Changement d'horaire", "Service fermé", "Service ouvert"], custom_data=['value'],
                text='value', color_discrete_sequence= [ '#7201a8', '#bd3786', '#E65A46', '#2896A0'])
    fig.update_layout(title="<b>Quels impacts a l'été sur les services ?</b>",
                        margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                        legend_title="Status",                     
                        xaxis_title="",
                        yaxis_title="",)
    fig.update_traces(hovertemplate='Catégorie de service: %{x}<br> Proportion :%{customdata}%', texttemplate='%{text}%', textposition='inside') 

    st.plotly_chart(fig, use_container_width=True)

       
    # Donnéés traitées pour construire graph 4
    res_91.rename(index={0: 'l\'équipe Soliguide', 1:'les acteurs'}, inplace=True)
    
    fig = px.pie(res_91, values='status', names=res_91.index, color_discrete_sequence= [ '#3E3A71', '#E65A46'])
    fig.update_traces(textposition='inside', textinfo='percent+label',\
                     hovertemplate = "%{value} structures mises à jour par %{label}")
    fig.update_layout(title="<b>Qui a mis à jour les structures pendant l'été ?</b>",
                      margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,)

    st.plotly_chart(fig, use_container_width=True)

    
    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>4</font><br><font size='2'>e-mails et relances envoyées</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>478</font><br/><font size='2'>appels effectués<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>3 499</font><br/><font size='2'>recherches réalisées sur Soliguide</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)        
                                                                                                                                                
######################
##  HAUTS-DE-SEINE  ##
######################

if categorie == 'Hauts-de-Seine (92)':
    st.markdown("<center><h1> Soliguide - Mise à jour été 2021 dans les Hauts-de-Seine</h1></center>", unsafe_allow_html=True)
    st.markdown("Chaque été et chaque hiver, l'équipe de Solinum met à jour la totalité de la base de données de Soliguide sur ses territoires d'implantation, afin d'orienter les publics en situation de précarité au mieux dans ces périodes de changement. Retrouvez ici toutes les statistiques de cette mise à jour été !")



    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>1 155</font><br><font size='2'>structures en ligne sur Soliguide</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>311</font><br/><font size='2'>structures ont fermé<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>32</font><br/><font size='2'>structures ont effectué des changements<br>(du 1<sup>er</sup>juillet au 31 août)</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)
   
    # Création de la carte avec pour centre : le centre d ela France
    mappy = folium.Map(location=[48.828508, 2.2188068],zoom_start=11)

    marker_cluster = MarkerCluster().add_to(mappy)
 
    # Création de la carte avec pour centre : le centre d ela France
    mappy = folium.Map(location=[48.828508, 2.2188068],zoom_start=11)

    marker_cluster = MarkerCluster().add_to(mappy)

    # Ajout des différents markers :
    for en in range(len(df_fiches_92['colors'])):
        folium.CircleMarker([df_fiches_92.latitude[en], df_fiches_92.longitude[en]],
                            fill = True,
                            color = df_fiches_92['colors'][en],
                            radius = 5,
                            fill_color = df_fiches_92['colors'][en],
                            tooltip=df_fiches_92['Fermeture_Estivale'][en], 
                            popup=df_fiches_92['name'][en]
                            ).add_to( mappy )

    url = ('https://raw.githubusercontent.com/Antoine-Carre/Soliguide_majete2021/main/ressources/legend_map_ete.png')
    FloatImage(url, bottom=65, left=70).add_to(mappy)

    mappy.save('map.html')

    #Affichage de la carte
    folium_static(mappy)

     # Donnéés traitées pour construire graph 2
    df_comparaison_92['Part de service fermé'] = df_comparaison_92['Part de service fermé'].round(1)

    fig = px.bar(df_comparaison_92.sort_values(by='Part de service fermé', ascending=False).head(10), y="catégorie", x=["ouvert", "Service fermé"],orientation='h', 
                 custom_data=['Part de service fermé'], color_discrete_sequence= [ '#7201a8', '#d8576b']) 

    fig.update_layout(title="<b>Quels sont les services qui ferment le plus pendant l'été ?</b>",
                          margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                            yaxis_title="",
                            xaxis_title="Nombre de services",
                            legend_title="Statut",)
    fig.update_traces(hovertemplate='Catégorie de service: %{y}<br> Nbre de service: %{x}  <br>Taux de fermeture :%{customdata}%') 
    st.plotly_chart(fig, use_container_width=True)

    # Donnéés traitées pour construire graph 3

    df_stacked_per_92.rename(columns={'Ouvert':'Service ouvert'}, inplace=True)

    fig = px.bar(df_stacked_per_92, x="Categories", y=["Structure fermée", "Changement d'horaire", "Service fermé", "Service ouvert"], custom_data=['value'],
                text='value', color_discrete_sequence= [ '#7201a8', '#bd3786', '#E65A46', '#2896A0'])
    fig.update_layout(title="<b>Quels impacts a l'été sur les services ?</b>",
                        margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                        legend_title="Status",                     
                        xaxis_title="",
                        yaxis_title="",)
    fig.update_traces(hovertemplate='Catégorie de service: %{x}<br> Proportion :%{customdata}%', texttemplate='%{text}%', textposition='inside') 

    st.plotly_chart(fig, use_container_width=True)

    # Donnéés traitées pour construire graph 4
    res_92.rename(index={0: 'l\'équipe Soliguide', 1:'les acteurs'}, inplace=True)
    
    fig = px.pie(res_92, values='status', names=res_92.index, color_discrete_sequence= [ '#3E3A71', '#E65A46'])
    fig.update_traces(textposition='inside', textinfo='percent+label',\
                     hovertemplate = "%{value} structures mises à jour par %{label}")
    fig.update_layout(title="<b>Qui a mis à jour les structures pendant l'été ?</b>",
                      margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,)

    st.plotly_chart(fig, use_container_width=True)

 
    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>774</font><br><font size='2'>e-mails et relances envoyées</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>138</font><br/><font size='2'>appels effectués<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>100 %</font><br/><font size='2'>de la base de données mise à jour cet été</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)         

                                                                                                                                               
#########################
##  SEINE-SAINT-DENIS  ##
#########################

if categorie == 'Seine-Saint-Denis (93)':
    st.markdown("<center><h1> Soliguide - Mise à jour été 2021 en Seine-Saint-Denis</h1></center>", unsafe_allow_html=True)
    st.markdown("Chaque été et chaque hiver, l'équipe de Solinum met à jour la totalité de la base de données de Soliguide sur ses territoires d'implantation, afin d'orienter les publics en situation de précarité au mieux dans ces périodes de changement. Retrouvez ici toutes les statistiques de cette mise à jour été !")



    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>925</font><br><font size='2'>structures en ligne sur Soliguide</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>243</font><br/><font size='2'>structures ont fermé<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>56</font><br/><font size='2'>structures ont effectué des changements<br>(du 1<sup>er</sup>juillet au 31 août)</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)

    # Création de la carte avec pour centre : le centre d ela France
    mappy = folium.Map(location=[df_fiches_93.latitude[0], df_fiches_93.longitude[0]],zoom_start=11)

    marker_cluster = MarkerCluster().add_to(mappy)

    # Ajout des différents markers :
    for en in range(len(df_fiches_93['colors'])):
        folium.CircleMarker([df_fiches_93.latitude[en], df_fiches_93.longitude[en]],
                            fill = True,
                            color = df_fiches_93['colors'][en],
                            radius = 5,
                            fill_color = df_fiches_93['colors'][en],
                            tooltip=df_fiches_93['Fermeture_Estivale'][en], 
                            popup=df_fiches_93['name'][en]
                            ).add_to( mappy )

    url = ('https://raw.githubusercontent.com/Antoine-Carre/Soliguide_majete2021/main/ressources/legend_map_ete.png')
    FloatImage(url, bottom=65, left=70).add_to(mappy)

    mappy.save('map.html')

    #Affichage de la carte
    folium_static(mappy)

     # Donnéés traitées pour construire graph 2
    df_comparaison_93['Part de service fermé'] = df_comparaison_93['Part de service fermé'].round(1)

    fig = px.bar(df_comparaison_93.sort_values(by='Part de service fermé', ascending=False).head(10), y="catégorie", x=["ouvert", "Service fermé"],orientation='h', 
                 custom_data=['Part de service fermé'], color_discrete_sequence= [ '#7201a8', '#d8576b']) 

    fig.update_layout(title="<b>Quels sont les services qui ferment le plus pendant l'été ?</b>",
                          margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                            yaxis_title="",
                            xaxis_title="Nombre de services",
                            legend_title="Statut",)
    fig.update_traces(hovertemplate='Catégorie de service: %{y}<br> Nbre de service: %{x}  <br>Taux de fermeture :%{customdata}%') 
    st.plotly_chart(fig, use_container_width=True)

    # Donnéés traitées pour construire graph 3

    df_stacked_per_93.rename(columns={'Ouvert':'Service ouvert'}, inplace=True)

    fig = px.bar(df_stacked_per_93, x="Categories", y=["Structure fermée", "Changement d'horaire", "Service fermé", "Service ouvert"], custom_data=['value'], text='value', color_discrete_sequence= [ '#7201a8', '#bd3786', '#E65A46', '#2896A0'])
    fig.update_layout(title="<b>Quels impacts a l'été sur les services ?</b>",
                        margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                        legend_title="Status",                     
                        xaxis_title="",
                        yaxis_title="",)
    fig.update_traces(hovertemplate='Catégorie de service: %{x}<br> Proportion :%{customdata}%', texttemplate='%{text}%', textposition='inside') 

    st.plotly_chart(fig, use_container_width=True)

    # Donnéés traitées pour construire graph 4
    res_93.rename(index={0: 'l\'équipe Soliguide', 1:'les acteurs'}, inplace=True)
    
    fig = px.pie(res_93, values='status', names=res_93.index, color_discrete_sequence= [ '#3E3A71', '#E65A46'])
    fig.update_traces(textposition='inside', textinfo='percent+label',\
                     hovertemplate = "%{value} structures mises à jour par %{label}")
    fig.update_layout(title="<b>Qui a mis à jour les structures pendant l'été ?</b>",
                      margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,)

    st.plotly_chart(fig, use_container_width=True)

 
    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>777</font><br><font size='2'>e-mails et relances envoyées</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>258</font><br/><font size='2'>appels effectués<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>100 %</font><br/><font size='2'>de la base de données mise à jour cet été</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)        
    
####################
##  VAL-DE-MARNE  ##
####################

if categorie == 'Val-de-Marne (94)':
    st.markdown("<center><h1> Soliguide - Mise à jour été 2021 dans le Val-de-Marne</h1></center>", unsafe_allow_html=True)
    st.markdown("Chaque été et chaque hiver, l'équipe de Solinum met à jour la totalité de la base de données de Soliguide sur ses territoires d'implantation, afin d'orienter les publics en situation de précarité au mieux dans ces périodes de changement. Retrouvez ici toutes les statistiques de cette mise à jour été !")


    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)


    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>944</font><br><font size='2'>structures en ligne sur Soliguide</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>260</font><br/><font size='2'>structures ont fermé<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>138</font><br/><font size='2'>structures ont effectué des changements<br>(du 1<sup>er</sup>juillet au 31 août)</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)
   
    # Création de la carte avec pour centre : le centre d ela France
    mappy = folium.Map(location=[df_fiches_94.latitude[0], df_fiches_94.longitude[0]],zoom_start=11)

    marker_cluster = MarkerCluster().add_to(mappy)

    # Ajout des différents markers :
    for en in range(len(df_fiches_94['colors'])):
        folium.CircleMarker([df_fiches_94.latitude[en], df_fiches_94.longitude[en]],
                            fill = True,
                            color = df_fiches_94['colors'][en],
                            radius = 5,
                            fill_color = df_fiches_94['colors'][en],
                            tooltip=df_fiches_94['Fermeture_Estivale'][en], 
                            popup=df_fiches_94['name'][en]
                            ).add_to( mappy )

    url = ('https://raw.githubusercontent.com/Antoine-Carre/Soliguide_majete2021/main/ressources/legend_map_ete.png')
    FloatImage(url, bottom=65, left=70).add_to(mappy)

    mappy.save('map.html')

    #Affichage de la carte
    folium_static(mappy)

     # Donnéés traitées pour construire graph 2
    df_comparaison_94['Part de service fermé'] = df_comparaison_94['Part de service fermé'].round(1)

    fig = px.bar(df_comparaison_94.sort_values(by='Part de service fermé', ascending=False).head(10), y="catégorie", x=["ouvert", "Service fermé"],orientation='h', 
                 custom_data=['Part de service fermé'], color_discrete_sequence= [ '#7201a8', '#d8576b']) 

    fig.update_layout(title="<b>Quels sont les services qui ferment le plus pendant l'été ?</b>",
                          margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                            yaxis_title="",
                            xaxis_title="Nombre de services",
                            legend_title="Statut",)
    fig.update_traces(hovertemplate='Catégorie de service: %{y}<br> Nbre de service: %{x}  <br>Taux de fermeture :%{customdata}%') 
    st.plotly_chart(fig, use_container_width=True)

    # Donnéés traitées pour construire graph 3

    df_stacked_per_94.rename(columns={'Ouvert':'Service ouvert'}, inplace=True)

    fig = px.bar(df_stacked_per_94, x="Categories", y=["Structure fermée", "Changement d'horaire", "Service fermé", "Service ouvert"], custom_data=['value'],
                text='value', color_discrete_sequence= [ '#7201a8', '#bd3786', '#E65A46', '#2896A0'])
    fig.update_layout(title="<b>Quels impacts a l'été sur les services ?</b>",
                        margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                        legend_title="Status",                     
                        xaxis_title="",
                        yaxis_title="",)
    fig.update_traces(hovertemplate='Catégorie de service: %{x}<br> Proportion :%{customdata}%', texttemplate='%{text}%', textposition='inside') 

    st.plotly_chart(fig, use_container_width=True)

    # Donnéés traitées pour construire graph 4
    res_94.rename(index={0: 'l\'équipe Soliguide', 1:'les acteurs'}, inplace=True)
    
    fig = px.pie(res_94, values='status', names=res_94.index, color_discrete_sequence= [ '#3E3A71', '#E65A46'])
    fig.update_traces(textposition='inside', textinfo='percent+label',\
                     hovertemplate = "%{value} structures mises à jour par %{label}")
    fig.update_layout(title="<b>Qui a mis à jour les structures pendant l'été ?</b>",
                      margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,)

    st.plotly_chart(fig, use_container_width=True)


    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>704</font><br><font size='2'>e-mails et relances envoyées</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>110</font><br/><font size='2'>appels effectués<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>100 %</font><br/><font size='2'>de la base de données mise à jour cet été</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)

                                                                                                                                                  
####################
##  VAL-D'OISE  ##
####################

if categorie == 'Val-d\'Oise (95)':
    st.markdown("<center><h1> Soliguide - Mise à jour été 2021 dans le Val d'Oise</h1></center>", unsafe_allow_html=True)
    st.markdown("Chaque été et chaque hiver, l'équipe de Solinum met à jour la totalité de la base de données de Soliguide sur ses territoires d'implantation, afin d'orienter les publics en situation de précarité au mieux dans ces périodes de changement. Retrouvez ici toutes les statistiques de cette mise à jour été !")


    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>431</font><br><font size='2'>structures en ligne sur Soliguide</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>99</font><br/><font size='2'>structures ont fermé<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>11</font><br/><font size='2'>structures ont effectué des changements<br>(du 1<sup>er</sup>juillet au 31 août)</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)

    # Création de la carte avec pour centre 
    mappy = folium.Map(location=[df_fiches_95.latitude[0], df_fiches_95.longitude[0]],zoom_start=9.5)

    marker_cluster = MarkerCluster().add_to(mappy)

    # Ajout des différents markers :
    for en in range(len(df_fiches_95['colors'])):
        folium.CircleMarker([df_fiches_95.latitude[en], df_fiches_95.longitude[en]],
                            fill = True,
                            color = df_fiches_95['colors'][en],
                            radius = 5,
                            fill_color = df_fiches_95['colors'][en],
                            tooltip=df_fiches_95['Fermeture_Estivale'][en], 
                            popup=df_fiches_95['name'][en]
                            ).add_to( mappy )

    url = ('https://raw.githubusercontent.com/Antoine-Carre/Soliguide_majete2021/main/ressources/legend_map_ete.png')
    FloatImage(url, bottom=65, left=70).add_to(mappy)

    mappy.save('map.html')

    #Affichage de la carte
    folium_static(mappy)

    
     # Donnéés traitées pour construire graph 2
    df_comparaison_95['Part de service fermé'] = df_comparaison_95['Part de service fermé'].round(1)

    fig = px.bar(df_comparaison_95.sort_values(by='Part de service fermé', ascending=False).head(10), y="catégorie", x=["ouvert", "Service fermé"],orientation='h', 
                 custom_data=['Part de service fermé'], color_discrete_sequence= [ '#7201a8', '#d8576b']) 

    fig.update_layout(title="<b>Quels sont les services qui ferment le plus pendant l'été ?</b>",
                          margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                            yaxis_title="",
                            xaxis_title="Nombre de services",
                            legend_title="Statut",)
    fig.update_traces(hovertemplate='Catégorie de service: %{y}<br> Nbre de service: %{x}  <br>Taux de fermeture :%{customdata}%') 
    st.plotly_chart(fig, use_container_width=True)

    # Donnéés traitées pour construire graph 3

    df_stacked_per_95.rename(columns={'Ouvert':'Service ouvert'}, inplace=True)

    fig = px.bar(df_stacked_per_95, x="Categories", y=["Structure fermée", "Changement d'horaire", "Service fermé", "Service ouvert"], custom_data=['value'],
                text='value', color_discrete_sequence= [ '#7201a8', '#bd3786', '#E65A46', '#2896A0'])
    fig.update_layout(title="<b>Quels impacts a l'été sur les services ?</b>",
                        margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,
                        legend_title="Status",                     
                        xaxis_title="",
                        yaxis_title="",)
    fig.update_traces(hovertemplate='Catégorie de service: %{x}<br> Proportion :%{customdata}%', texttemplate='%{text}%', textposition='inside') 

    st.plotly_chart(fig, use_container_width=True)


    # Donnéés traitées pour construire graph 4
    res_95.rename(index={0: 'l\'équipe Soliguide', 1:'les acteurs'}, inplace=True)
    
    fig = px.pie(res_95, values='status', names=res_95.index, color_discrete_sequence= [ '#3E3A71', '#E65A46'])
    fig.update_traces(textposition='inside', textinfo='percent+label',\
                     hovertemplate = "%{value} structures mises à jour par %{label}")
    fig.update_layout(title="<b>Qui a mis à jour les structures pendant l'été ?</b>",
                      margin=dict(l=10, r=10, b=10, t=40), title_x=0.5,)

    st.plotly_chart(fig, use_container_width=True)


   

    col1, col2, col3 = st.columns(3)

    html_string = "<center><font face='Helvetica' size='6'>145</font><br><font size='2'>e-mails et relances envoyées</font></center>"

    col1.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>907</font><br/><font size='2'>appels effectués<br></font></center>"

    col2.markdown(html_string, unsafe_allow_html=True)

    html_string = "<center><font face='Helvetica' size='6'>100 %</font><br/><font size='2'>de la base de données mise à jour cet été</font></center>"

    col3.markdown(html_string, unsafe_allow_html=True)

    html_string = "<br>"

    st.markdown(html_string, unsafe_allow_html=True)
            
