# Script Python pour envoyer les données à Kafka
from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='kafka:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def send_weather_data(topic, data):
    producer.send(topic, data)
    producer.flush()

if __name__ == "__main__":
    weather_data = {"city": "Paris", "temperature": 20.0, "humidity": 60, "wind_speed": 5.0}
    send_weather_data('weather_topic', weather_data)
