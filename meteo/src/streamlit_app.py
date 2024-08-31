import streamlit as st
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

st.title('Weather Data')

try:
    weather_data = fetch_weather_data_from_cassandra()
    if not weather_data:
        st.write("No data found.")
    else:
        for data in weather_data:
            st.write(f"City: {data.city_name}, City: {data.city_name},Temperature: {data.temperature}°C, Humidity: {data.humidity}%, Wind Speed: {data.wind_speed} m/s")
except Exception as e:
    st.error(f"An error occurred: {e}")
