#!/bin/bash

# Define variables for your container
CONTAINER_NAME="my_gitagpt_container"
IMAGE_NAME="ankitsharma61016/gitagpt108"
HOST_PORT=40000  # Change this to the desired host port
CONTAINER_PORT=40000  # Change this to the desired container port
HF_ACCESS_TOKEN=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

# Check if the container is already running
if [ "$(docker ps -q -f name=${CONTAINER_NAME})" ]; then
    echo "[-] Container ${CONTAINER_NAME} is already running."
    exit 0
fi

# Check if the container exists but is stopped
if [ "$(docker ps -aq -f status=exited -f name=${CONTAINER_NAME})" ]; then
    echo "[+] Removing stopped container ${CONTAINER_NAME}..."
    docker rm ${CONTAINER_NAME}
fi

# Pull the latest image from the repository
docker pull ${IMAGE_NAME}
echo "[+] Successfully pulled ${IMAGE_NAME}..."

# Run the Docker container with port mapping
docker run -e HF_ACCESS_TOKEN=${HF_ACCESS_TOKEN} -d --name ${CONTAINER_NAME} -p ${HOST_PORT}:${CONTAINER_PORT} ${IMAGE_NAME}  
# Check if the container started successfully
if [ "$(docker ps -q -f name=${CONTAINER_NAME})" ]; then
    echo "[+] Container ${CONTAINER_NAME} is now running and accessible on port ${HOST_PORT}."
else
    echo "[-]Failed to start container ${CONTAINER_NAME}."
fi
