#!/bin/bash

CONTAINER_NAME="your-container-name"

while true; do
if ! docker inspect -f '{{.State.Running}}' "$CONTAINER_NAME" > /dev/null; then
echo "Container $CONTAINER_NAME is not running. Restarting..."
docker restart "$CONTAINER_NAME"
fi
sleep 10
done