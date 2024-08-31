# Script Python pour récupérer les données météo et les insérer dans Cassandra
import requests
import json
from cassandra_connector import connect_cassandra, insert_weather_data  # Importez les fonctions nécessaires
import streamlit as st  # Pour la publication dans Streamlit

API_KEY = '9e37b665b3fa80d58bdff03181f2f65c'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def fetch_weather_data(lat, lon):
    url = f"{BASE_URL}?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error retrieving weather data: {response.status_code}")

if __name__ == "__main__":
    session = connect_cassandra()  # Connexion à Cassandra
    
    with open('city.list.json') as f:
        cities = json.load(f)
    
    for city in cities:
        coords = city['coord']
        
        # Filtrer pour récuperer les villes francaises
        french_cities = [city for city in cities if city.get('country') == 'FR']
        
        for city in french_cities:
            coords = city['coord']
            data = fetch_weather_data(coords['lat'], coords['lon'])
            # Extraction des données 
            city_name = city['name']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
        
            # Insertion dans Cassandra
            insert_weather_data(session, city_name,temperature, humidity, wind_speed)
        
            # Publication dans Streamlit s'il est en cours d'exécution
            st.write(f"City: {city_name}, Temperature: {temperature}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} m/s")
