#!/bin/bash

# Deploy Script for EPL Project

echo "🚀 Starting Deployment..."

# 1. Pull the latest changes from git
echo "📥 Pulling latest changes..."
git pull origin main

# 2. Rebuild and restart containers
echo "🔄 Rebuilding and restarting containers..."
docker compose down
docker compose up --build -d

# 3. Apply database migrations
echo "🗄️ Applying migrations..."
docker compose exec web python manage.py migrate

# 4. Collect static files
echo "🎨 Collecting static files..."
docker compose exec web python manage.py collectstatic --noinput

echo "✅ Deployment completed successfully!"
