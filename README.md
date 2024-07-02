# Setting Up the Project


**Step 1: Set Up Environment Variables**

create an `.env` file to the project, copy the contents in `example.env`
and paste in the .env file
NB: update the .env file by adding a value for `OPENAI_API_KEY`: you can get this from OPENAI



**Step 2: Build and Run the Docker Containers**

Run the below command to build and start your Docker containers:

`docker-compose up --build`

This command will spin up Docker containers and prepare all the necessary dependencies




**Step 3: Make a POST Request to the API**

You can now make a POST request to the API endpoint to ask a question to the LLM (Large Language Model).

Endpoint: `http://127.0.0.1:5002/api/ask`

Example request body:

```
    {
    "question": "anything you want to ask the llm"
}

```

You can use tools like curl or Postman to make this request. Here's an example using curl:

`
    curl -X POST http://127.0.0.1:5002/api/ask -H "Content-Type: application/json" -d '{"question": "anything you want to ask the llm"}'
`



**Step 4: Run Tests**

To run tests for your project, use the following command:

  `docker-compose run test`







# Flask Application with Alembic, SQLAlchemy, and PostgreSQL

## Introduction

This is a Flask application that uses Alembic for database migrations, SQLAlchemy for ORM, and PostgreSQL as the database. The application is designed to be robust and scalable, and it runs within Docker containers.

## Features

- Flask-based web application
- SQLAlchemy for ORM
- Alembic for database migrations
- PostgreSQL database
- Docker support for containerization

## Prerequisites

Before you begin, make you have met the following requirements:

- Docker
- Git

## Installation

1. **Clone the repository**

   `
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   `

2. **Build the Docker images**

   `
   docker-compose build
   `

## Configuration

Create a `.env` file in the root directory of your project and add the following environment variables:

`
    OPENAI_API_KEY=open-api_key

    POSTGRES_DB=DB_NAME
    POSTGRES_USER=DB_USER
    POSTGRES_PASSWORD=DB_PASSWORD
    DB_USER=DB_USER
    DB_PASSWORD=DB_PASSWORD
    DB_SERVER=DB_SERVER
    DB_NAME=DB_NAME
    DATABASE_URL=postgresql://DB_USER:DB_PASSWORD@db:5432/DB_NAME
    FLASK_ENV=development

`

## Database Setup

**Start the Docker containers**

   `
   docker-compose up -d
   `

## Running the Application

The application will automatically start and create migration
when you run:

`
docker-compose up
`

The application will be available at `http://127.0.0.1:5000`.

Example request body:

`
    {
    "question": "< PROMPT >"
    }

`

You can use tools like curl or Postman to make this request. Here's an example using curl:

`
    curl -X POST http://127.0.0.1:5002/api/ask -H "Content-Type: application/json" -d '{"question": "anything you want to ask the llm"}'
`


## Testing

To run tests, use the following command:

`
docker-compose exec web pytest
`

