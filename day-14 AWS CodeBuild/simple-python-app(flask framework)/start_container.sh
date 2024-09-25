#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull abhishekf5/sample-python-flask-app

# Run the Docker image as a container  -p for prt mapping, -it for interactive mode, -d to run in background or as daemon.
# In computing, a daemon (pronounced DEE-muhn) is a program that runs continuously as a background process and wakes up to handle periodic service requests, which often come from remote processes.
docker run -d -p 5000:8000
