# Clear docker cache
sudo docker system prune -a
# serve http page
sudo docker-compose up -d
# Get new certs
sudo docker run -i --rm \
-v /docker-volumes/etc/letsencrypt:/etc/letsencrypt \
-v /docker-volumes/var/lib/letsencrypt:/var/lib/letsencrypt \
-v /website/letsencrypt/site:/data/letsencrypt \
-v "/docker-volumes/var/log/letsencrypt:/var/log/letsencrypt" \
certbot/certbot \
certonly --webroot \
--email spwhite1337@gmail.com --agree-tos --no-eff-email \
--webroot-path=/data/letsencrypt \
-d scottpwhite.com -d www.scottpwhite.com --break-my-certs

# Shut down and prune cert-container
sudo docker-compose down
sudo docker system prune -a
# Serve website
cd ../
sudo docker-compose -f docker-compose-https.yml up --build -d
