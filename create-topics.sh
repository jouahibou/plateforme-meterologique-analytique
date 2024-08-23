#!/bin/bash

# Créer les sujets Kafka
kafka-topics --create --bootstrap-server kafka:9092 --replication-factor 1 --partitions 1 --topic weather_data