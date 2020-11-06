# Clear docker cache
sudo docker system prune -a
# serve http page
sudo docker compose up -d
# Remove staging volumes
sudo rm -rf ../../docker-volumes
# Get new certs
source letsencrypt-prod.sh
# Shut down and prune cert-container
sudo docker-compose down
sudo docker system prune -a
# Serve website
cd ../
sudo docker-compose -f docker-compose-https.yml up --build -d
