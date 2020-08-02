sudo docker run --rm -it --name certbot \
-v /docker-volumes/etc/letsencrypt:/etc/letsencrypt \
-v /docker-volumes/var/lib/letsencrypt:/var/lib/letsencrypt \
-v /website/letsencrypt/site:/data/letsencrypt \
certbot/certbot \
--staging \
certificates
