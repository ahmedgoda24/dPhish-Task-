# dPhish-Task

## Overview
dPhish-Task is a Django-based project designed to manage and analyze IP information. It leverages WebSocket communication for real-time updates and Docker for containerized development.

## Prerequisites
Ensure the following tools are installed before starting the project:
- Python 3.8 or higher
- Docker and Docker Compose
- Git

## Installation

### Clone the Repository
```bash
git clone https://github.com/your-username/dphish-task.git
cd dphish-task
```

### ⚙️ Configure Environment Variables
Create the following files inside a `.envs` directory:
- `.env`
- `.env.backend.dev`

## Building the Containers
1. Build and start the Docker containers:
    ```bash
    docker-compose up --build
    ```
2. Verify that the containers are running:
    ```bash
    docker ps
    ```
3. Stop the containers:
    ```bash
    docker-compose down
    ```