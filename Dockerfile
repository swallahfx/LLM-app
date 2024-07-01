# Dockerfile for Flask App
FROM python:latest

WORKDIR /code

COPY requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir pip setuptools wheel && pip install -r requirements.txt

ENV FLASK_APP=main.py

CMD ["flask", "run", "--host=0.0.0.0"]

