#!/bin/bash

# Flask + Redis Docker Compose Automation Script
set -e 
 # Stop script on error

echo "🚀 Starting Flask + Redis project automation..."

# STEP 1: Build Docker images
echo "🛠  Building Docker images..."
docker compose build

# STEP 2: Start the containers
echo "🐳 Starting containers..."
docker compose up -d

# Giving the containers time to start
sleep 510

# STEP 3: Test the Flask API
echo "🧪 Testing API endpoints..."

echo "➡  Checking home route:"
curl -s http://localhost:5000/ | jq .

echo "➡  Setting a value in Redis:"
curl -s -X POST -H "Content-Type: application/json" \
-d '{"key":"language", "value":"Python"}' \
http://localhost:5000/set | jq .

echo "➡  Retrieving the stored value:"
curl -s http://localhost:5000/get/language | jq .

# STEP 4: Show running containers
echo "📦 Currently running containers:"
docker ps

# STEP 5: Optionally stop the containers after test
read -p "🧹 Do you want to stop and clean up containers? (y/n): " answer
if [ "$answer" == "y" ]; then
    echo "Stopping and removing containers..."
    docker compose down
    echo "✅ Cleanup complete."
else
    echo "Containers left running. You can stop them later with: docker compose down"
fi