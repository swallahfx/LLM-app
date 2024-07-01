# Dockerfile for Flask App
FROM python:3.9

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=main.py

CMD ["flask", "run", "--host=0.0.0.0"]
