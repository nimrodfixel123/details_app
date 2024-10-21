# Details App

## Overview
The Details App is a Flask-based web application containerized with Docker. It connects to a PostgreSQL database and has various endpoints for managing contacts. This project includes everything required to set up, run, and test the application using Docker and Docker Compose.

## Features
- Flask-based web application
- PostgreSQL database integration
- Dockerized for easy deployment
- Health check endpoint (`/api/health_check`)
- CRUD operations for managing contacts

## Prerequisites
To successfully run this project, ensure you have the following dependencies installed:
- **Docker**: for containerization
- **Docker Compose**: for orchestrating the containers
- **Git**: for cloning the project

## Project Structure
details_app/
├── Dockerfile
├── README.md
├── TASKS.md
├── build.sh
├── details.py
├── docker-compose.yml
├── gunicorn_conf.py
├── pgsql/
│   ├── data/
│   └── pg_hba.conf
├── poetry.lock
├── pyproject.toml
├── src/
│   └── details/
│       ├── __init__.py
│       ├── app.py
│       ├── libs/
│       │   ├── __init__.py
│       │   └── libs.py
│       ├── static/
│       │   ├── css/
│       │   │   └── styles.css
│       │   ├── favicon.ico
│       │   ├── img/
│       │   │   └── bg-mobile-fallback.jpg
│       │   ├── js/
│       │   │   └── scripts.js
│       │   └── mp4/
│       │       └── bg.mp4
│       └── templates/
│           ├── index.html
│           └── layout.html
└── tests/
    └── test_db_connection.py



## Database Initialization
The database initialization for PostgreSQL is handled within the `app.py` file. The app will automatically create the necessary tables if they don't already exist. This ensures the database is set up correctly before the application starts serving requests.

## Testing
The test file `test_db_connection.py` is located under the `tests` directory. This script tests the connection between the Flask application and the PostgreSQL database.

## Usage Instructions
1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:
    ```bash
    cd details_app
    ```

3. Run the `build.sh` script to build and run the application:
    ```bash
    ./build.sh
    ```

    This script does the following:
    - Builds the Docker image using the `Dockerfile`.
    - Spins up the necessary containers (Flask app and PostgreSQL) using `docker-compose.yml`.
    - Waits for the database to start.
    - Runs the test to verify the database connection.
    - Launches the Flask app.

The application will be available at `http://localhost:8000` and ready to use once the setup completes.

---

