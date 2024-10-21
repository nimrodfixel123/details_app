
import os
import time
import requests
import subprocess

APP_URL = 'http://localhost:8123/api/health_check'
DB_CONTAINER_NAME = 'postgres-container'

def check_app_connection():
    """
    Check if the application is running and can connect to the database.
    """
    try:
        response = requests.get(APP_URL, timeout=5)
        if response.status_code == 200:
            print("Application is connected to the database.")
            return True
        else:
            print(f"Application error: Status Code {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")
        return False

def restart_db_container():
    """
    Attempt to restart the PostgreSQL container.
    """
    print(f"Restarting database container: {DB_CONTAINER_NAME}")
    try:
        subprocess.run(["docker", "restart", DB_CONTAINER_NAME], check=True)
        print(f"{DB_CONTAINER_NAME} restarted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to restart database container: {e}")

def verify_and_fix_connection():
    """
    Verify the application is connected to the database. If not, try to restart the DB container and retry.
    """
    if not check_app_connection():
        print("Attempting to fix the issue by restarting the database container.")
        restart_db_container()

        # Wait a few seconds for the container to restart
        time.sleep(10)

        # Recheck the connection
        if check_app_connection():
            print("Connection fixed and application is now connected to the database.")
        else:
            print("The issue persists. Please check the application logs for further investigation.")
    else:
        print("No issues detected.")

if __name__ == "__main__":
    print("Starting application and database connection test...")
    verify_and_fix_connection()
