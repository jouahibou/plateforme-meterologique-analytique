import requests
import datetime
import json
import os
from kafka import KafkaProducer

with open('city.list.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

api_key = os.getenv("API_KEY")

today = datetime.date.today().strftime("%Y-%m-%d")

# Configurez le producteur Kafka
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda x: json.dumps(x).encode('utf-8'))

for city in data:
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={city['coord']['lat']}&lon={city['coord']['lon']}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Extraire les informations pertinentes
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Créer un dictionnaire avec les données météorologiques
        weather_data = {
            "city": city['name'],
            "date": today,
            "weather": weather,
            "temperature": temperature,
            "humidity": humidity,
            "wind_speed": wind_speed
        }

        # Envoyer les données météorologiques à Kafka au format JSON
        producer.send('weather-data', value=weather_data)
        print(f"Envoyé les données météorologiques pour {city['name']}")
    else:
        print(f"Erreur lors de la récupération des données météorologiques pour {city['name']} : {response.status_code}")

# Fermez le producteur Kafka
producer.close()