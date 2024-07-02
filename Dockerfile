FROM python:3.12.0-slim-bookworm

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir pip setuptools wheel && pip install -r requirements.txt

ENV FLASK_APP=main.py
