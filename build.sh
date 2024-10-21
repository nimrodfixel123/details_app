#!/bin/bash

APP_VERSION=${1:-'0.0.1'}

# Build the Docker image
docker build . -t details_app

# Start the containers with Docker Compose
docker-compose up -d

# Wait for 5 seconds, printing a message each second
for i in {1..5}; do
    echo "Waiting for database to start... $i"
    sleep 1
done

# Run the database connection test
python3 ./tests/test_db_connection.py
