# Dockerfile pour l'application Python
FROM python:3.9

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY src/ /app/src
COPY city.list.json /app/city.list.json

CMD ["python", "/app/src/weather_scraper.py"]
