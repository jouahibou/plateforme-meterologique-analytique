import sys
import requests
import json


API_KEY = "fc2b9961c3b715f04390f7f5c8705510"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


sys.stdout.reconfigure(encoding='utf-8')


with open("city.list.json", "r", encoding="utf-8") as file:
    cities = json.load(file)

# Méteo France
def get_weather_data(Paris):
    params = {
        "q": Paris,
        "appid": API_KEY,
        "units": "metric",  
        "lang": "fr"        
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status() 

        
        data = response.json()

    
        weather_info = {
            "city": data.get("name"),
            "temperature": data["main"].get("temp"),
            "description": data["weather"][0].get("description"),
            "humidity": data["main"].get("humidity"),
            "wind_speed": data["wind"].get("speed")
        }

        return weather_info

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des données pour {Paris}: {e}")
        return None

# les villes Françaises
def process_all_french_cities():
    for city in cities:
        if city.get("country") == "FR":  
            city_name = city.get("name")
            weather_data = get_weather_data(city_name)
            
            if weather_data:
                print(f"Météo pour {weather_data['city']}:")
                print(f"Température: {weather_data['temperature']}°C")
                print(f"Description: {weather_data['description']}")
                print(f"Humidité: {weather_data['humidity']}%")
                print(f"Vitesse du vent: {weather_data['wind_speed']} m/s")
                print("-" * 40)  
            else:
                print(f"Aucune donnée disponible pour {city_name}.")

if __name__ == "__main__":
    process_all_french_cities()
