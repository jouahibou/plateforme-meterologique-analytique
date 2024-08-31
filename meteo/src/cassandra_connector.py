# Script Python pour se connecter et insérer les données dans Cassandra
import time
from cassandra.cluster import Cluster

def connect_cassandra(retries=5, delay=10):
    cluster = Cluster(['cassandra'])  # Nom du service Cassandra dans Docker Compose
    session = None
    while retries > 0:
        try:
            session = cluster.connect()
            # Créez le keyspace et la table si nécessaire
            session.execute("""
            CREATE KEYSPACE IF NOT EXISTS weather_key 
            WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}
            """)
            session.execute("""
            CREATE TABLE IF NOT EXISTS weather_key.weather_data (
                city_name TEXT PRIMARY KEY,
                temperature FLOAT,
                humidity INT,
                wind_speed FLOAT
            )
            """)
            session.set_keyspace('weather_key')  
            break
        except Exception as e:
            print(f"Error connecting to Cassandra: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
            retries -= 1
    if session is None:
        raise ConnectionError("Unable to connect to Cassandra after several retries.")
  
            
    return session

def insert_weather_data(session, city_name, temperature, humidity, wind_speed):
    query = """
    INSERT INTO weather_data (city_name, temperature, humidity, wind_speed)
    VALUES (%s, %s, %s, %s)
    """
    session.execute(query, (city_name, temperature, humidity, wind_speed))


