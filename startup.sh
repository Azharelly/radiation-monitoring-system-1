#!/bin/bash
set -e

apt-get update
apt-get install -y docker.io

systemctl start docker
systemctl enable docker

gcloud auth configure-docker europe-west1-docker.pkg.dev --quiet

docker run -d -p 8080:8080 \
  europe-west1-docker.pkg.dev/radiation-monitoring-system-ca/radiation-docker-repo/radiation-monitoring-app:latest
