#!/bin/bash
sudo apt-get update
sudo apt-get install -y docker.io docker-compose git
sudo systemctl start docker
sudo systemctl enable docker
git clone https://github.com/johnjg12/python-skeleton-app.git /opt/python-skeleton-app
cd /opt/python-skeleton-app
# Echo the hostname into a file
echo "HOSTNAME=$(hostname)" > .env
sudo docker-compose up -d --build
