# dPhish-Task

## Overview
dPhish-Task is a Django-based project designed to manage and analyze IP information. It uses WebSocket communication for real-time updates and Docker for containerized development.

## Prerequisites
Before starting the project, ensure you have the following installed:
- Python 3.8 or higher
- Docker and Docker Compose
- Node.js (if applicable for frontend development)
- Git

## Installation

### Clone the Repository
```bash
git clone https://github.com/your-username/dphish-task.git
cd dphish-task

## ⚙️ Configure Environment Variables

Create the following files inside a `.envs` directory:

- `.env`
- `.env.backend.dev`

## Building the Containers
1-Build and start the Docker containers
docker-compose up --build
2-Verify that the containers are running
docker ps
3-Stop the containers
docker-compose down