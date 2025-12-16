#!/bin/bash
set -e

apt-get update
apt-get install -y docker.io jq

systemctl start docker
systemctl enable docker

gcloud auth configure-docker europe-west1-docker.pkg.dev -q

# Start Cloud SQL Auth Proxy if not already running
if ! pgrep -f cloud-sql-proxy > /dev/null; then
  /usr/local/bin/cloud-sql-proxy radiation-monitoring-system-ca:europe-west1:radiation-mysql --port 3306 &
fi

sleep 5

DB_NAME=$(gcloud secrets versions access latest --secret=DB_NAME)
DB_USER=$(gcloud secrets versions access latest --secret=DB_USER)
DB_PASSWORD=$(gcloud secrets versions access latest --secret=DB_PASSWORD)

docker rm -f radiation-api || true

docker pull europe-west1-docker.pkg.dev/radiation-monitoring-system-ca/radiation-docker-repo/radiation-monitoring-app:latest

docker run -d -p 8080:8080\
  --name radiation-api \
  -e DB_HOST=127.0.0.1 \
  -e DB_NAME="$DB_NAME" \
  -e DB_USER="$DB_USER" \
  -e DB_PASSWORD="$DB_PASSWORD" \
  europe-west1-docker.pkg.dev/radiation-monitoring-system-ca/radiation-docker-repo/radiation-monitoring-app:latest
