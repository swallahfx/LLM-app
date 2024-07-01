# Setting Up the Project

**Step 1: Set Up Environment Variables**

`
    OPENAI_API_KEY=open-api_key

    POSTGRES_DB=openai_db
    POSTGRES_USER=user
    POSTGRES_PASSWORD=password
    DB_USER=user
    DB_PASSWORD=password
    DB_SERVER=db
    DB_NAME=openai_db
    DATABASE_URL=postgresql://user:password@db:5432/openai_db
    FLASK_ENV=development

`

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