#!/bin/bash
set -e

# Update system
apt-get update
apt-get install -y docker.io jq

systemctl start docker
systemctl enable docker 

gcloud auth configure-docker europe-west1-docker.pkg.dev -q

# Get secrets from Secret Manager
DB_HOST=$(gcloud secrets versions access latest --secret=DB_HOST)
DB_NAME=$(gcloud secrets versions access latest --secret=DB_NAME)
DB_USER=$(gcloud secrets versions access latest --secret=DB_USER)
DB_PASSWORD=$(gcloud secrets versions access latest --secret=DB_PASSWORD)

# Pull image from Artifact Registry
docker pull europe-west1-docker.pkg.dev/radiation-monitoring-system-ca/radiation-docker-repo/radiation-monitoring-app:latest

# Run container with env variables
docker run -d -p 8080:8080 \
  -e DB_HOST="$DB_HOST" \
  -e DB_NAME="$DB_NAME" \
  -e DB_USER="$DB_USER" \
  -e DB_PASSWORD="$DB_PASSWORD" \
  europe-west1-docker.pkg.dev/radiation-monitoring-system-ca/radiation-docker-repo/radiation-monitoring-app:latest

