#!/bin/bash

# Consommer les messages du sujet Kafka
kafka-console-consumer --bootstrap-server kafka:9092 --topic weather_data --from-beginning