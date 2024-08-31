


# plateforme-meterologique-analytique

## Introduction

Cette documentation décrit le projet de collecte et de traitement de données météorologiques en utilisant l'API OpenWeather, Kafka, et une base de données Cassandra. Elle couvre les étapes de mise en œuvre, l'architecture du système, et les instructions d'utilisation.

## Architecture du Système

![Logo](https://github.com/jouahibou/plateforme-meterologique-analytique/blob/main/meteo/services.png)



  - ### API OpenWeather : Fournit des données météorologiques en temps réel
  - ### Kafka : Utilisé pour le streaming des données entre le producteur et le consommateur
  - ### Cassandra : Base de données pour le stockage des données historisées
  - ### Streamlit : Outil pour créer un dashboard en temps réel.

## Etape e Mise en Oeuvre 

  - ### API utilisée :  OpenWeatherMap
    
  - ### Technologies requises :
     - Docker
     - Docker Compose
     - Python (avec les bibliothèques requests, kafka-python, pymongo ou cassandra-driver)
       
  - ### Conception de la Base de Donnnées
    La structure de notre base de données est assez simple et adaptée pour stocker les données météo des villes. Chaque enregistrement comprend des informations essentielles comme le nom de la ville, la température, l'humidité et la vitesse du vent. On a choisi 
    d'organiser les données par ville pour pouvoir les retrouver facilement. En gros, cette structure nous aide à gérer facilement toutes les données météo en temps réel et à les consulter sans complications

  - ### Développement d’un Dashboard
    Utilisation de Streamlit pour afficher les données en temps réel

   ![Logo]( https://github.com/jouahibou/plateforme-meterologique-analytique/blob/main/meteo/streamlit.png )

## Instructions d'Utilisation 
  - ### Cloner le repo : git clone https://github.com/jouahibou/plateforme-meterologique-analytique.git
  - ### Lancer Docker Compose : Exécutez docker-compose up pour démarrer tous les services
  - ### Accéder au Dashboard : Ouvrez un navigateur et visitez http://localhost:8501

## NB : Il y a un délai d'environ 1 à 2 minutes dans le chargement des données.
    
# Participants 
  - ### Ndeye Aida Ndour
  - ### Siré Ba
  - ### Mamadou Baldé
  - ### Seydina Jouahibou DIAME
  - ### Aliou Amar
