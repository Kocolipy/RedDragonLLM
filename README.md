# FastAPI Dockerized Application

This is a Dockerized TinyLlama LLM model delivered using FastAPI that can be easily deployed using Docker containers.

## Prerequisites

Make sure you have Docker installed on your machine.

- [Docker Installation Guide](https://docs.docker.com/get-docker/)

## Getting Started

Follow these steps to set up and run the FastAPI application in a Docker container.

### 1. Build the Docker Image

Open a terminal in the project directory and run the following command to build the Docker image.

```bash
docker build -t my-fastapi-app .
```

### 2. Run the Docker Container

Once the image is built, run the Docker container using the following command:

```bash
docker run -p 4000:80 my-fastapi-app
```

This command maps port 4000 on your host machine to port 80 on the Docker container. Adjust the ports as needed.

### 3. Ask the LLM anything.

Insert your query into the request payload using a different shell/terminal.

```bash
curl --location 'http://127.0.0.1:4000/query' \
--header 'Content-Type: application/json' \
--data '{
    "content": "<query here>"
}'
```
