FROM python:3.10-slim

RUN apt-get update && apt-get install -y build-essential libpq-dev curl \
 && pip install --no-cache-dir mlflow psycopg2-binary \
 && apt-get clean

WORKDIR /mlflow