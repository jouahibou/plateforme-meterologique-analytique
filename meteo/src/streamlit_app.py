import streamlit as st
import pandas as pd
from cassandra.cluster import Cluster
import time

def fetch_weather_data_from_cassandra():
    cluster = Cluster(['cassandra'])
    session = None
    retries = 5
    while retries > 0:
        try:
            session = cluster.connect('weather_key')
            break
        except Exception as e:
            st.error(f"Error connecting to Cassandra: {e}. Retrying...")
            time.sleep(5)
            retries -= 1
    if session is None:
        raise ConnectionError("Unable to connect to Cassandra after several retries.")
    
    try:
        rows = session.execute("SELECT * FROM weather_data")
        return rows
    except Exception as e:
        st.error(f"Error executing query: {e}")
        return []

st.title('Visualisation des données météorologiques')

try:
    weather_data = fetch_weather_data_from_cassandra()
    
    if not weather_data:
        st.write("No data found.")
    else:
        
        cities = []
        temperatures = []
        humidities = []
        wind_speeds = []
        
        for data in weather_data:
            cities.append(data.city_name)
            temperatures.append(data.temperature)
            humidities.append(data.humidity)
            wind_speeds.append(data.wind_speed)
        
        
        lengths = {len(cities), len(temperatures), len(humidities), len(wind_speeds)}
        if len(lengths) > 1:
            st.error("Data arrays have different lengths.")
            st.write(f"Lengths: Cities: {len(cities)}, Temperatures: {len(temperatures)}, Humidities: {len(humidities)}, Wind Speeds: {len(wind_speeds)}")
        else:
           
            data_dict = {
                "City": cities,
                "Temperature (°C)": temperatures,
                "Humidity (%)": humidities,
                "Wind Speed (m/s)": wind_speeds
            }
            
            df = pd.DataFrame(data_dict)

            
            st.subheader('Tableau des données ')
            st.dataframe(df)

            
            st.subheader('Température au-dessus de la ville')
            st.line_chart(df.set_index('City')['Temperature (°C)'])

except Exception as e:
    st.error(f"An error occurred: {e}")
