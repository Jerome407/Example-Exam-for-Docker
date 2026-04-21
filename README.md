# Dockerized CV Application

## Project Overview
This is a microservices-based web application featuring a Flask frontend and a PostgreSQL database. The project demonstrates container orchestration, network isolation, and persistent storage using Docker.

## System Architecture
The application consists of:
- **Web Service:** Flask (Python 3.11-slim) running on port 8000.
- **Database Service:** PostgreSQL for data storage.
- **Network:** Isolated Docker bridge network for secure communication.
- **Volume:** Persistent storage for the database.

## Setup Instructions
1. **Clone the repo:** `git clone https://github.com/Jerome407/Example-Exam-for-Docker.git`
2. **Build and Run:** `docker compose up --build -d`
3. **Check Status:** `docker compose ps`
4. **Access:** Open `http://localhost:8000` in your browser.

## Docker Configurations
- **Optimization:** Used `python:3.11-slim` and build caching for faster performance.
- **Security:** Implemented network isolation to protect the database service.
- **Healthchecks:** Ensures the database is ready before the web service starts.
