sudo docker run -it --rm \
-v /docker-volumes/etc/letsencrypt:/etc/letsencrypt \
-v /docker-volumes/var/lib/letsencrypt:/var/lib/letsencrypt \
-v /website/letsencrypt/site:/data/letsencrypt \
-v "/docker-volumes/var/log/letsencrypt:/var/log/letsencrypt" \
certbot/certbot \
certonly --webroot \
--email spwhite1337@gmail.com --agree-tos --no-eff-email \
--webroot-path=/data/letsencrypt \
-d scottpwhite.com -d www.scottpwhite.com
