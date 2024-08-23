#!/bin/bash

# Produire des messages dans le sujet Kafka
kafka-console-producer --broker-list kafka:9092 --topic weather_data