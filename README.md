# Website

Personal website to display some data products and to impose my will on the internet via blog. 

<img src="docs/logo.jpg" alt="Website logo" width=256>

Note: This repo works for the `scottpwhite.com` domain and is hard-coded in every `.conf` and `.sh` file. If adopting 
this repo to a new website, you will need to change these along with my email in `letsencrypt-prod.sh`.

---

###  AWS

- Set Up AWS EC2 instance: 
    - Ubuntu 18.04 Image
    - t2.small (~$0.0023 / hour or ~$16 / month)
        - Can't install project on t2.micro (Exits with `Killed` error)
    - Spot Requests (Will lower the costs but not sure how much)
    - Explicitly select a subnetwork (probably unnecessary)
    - Enable Auto-assign Public IP
    - 16 GB EBS (Costs ~$0.10 GB / month, @TODO trim down)
    - Security Group `Website`:
        - SSH on 22
        - HTTP on 80
        - HTTPS on 443
        - Custom TCP on 5000 (for backend)
    
### GoDaddy    

- Update DNS records in GoDaddy account
    - Log-in -> Scott White (upper right) -> Manage Domains -> DNS -> Manage Zones -> Search `scottpwhite.com`
    - Match records to the IP Address from the EC2 instance
    
    <img src="docs/DNS_records.JPG" alt="DNS Records" width=256>
    

### Serve over HTTP    


- Set up project
    - SSH into instance
    - Go to server root (on EC2; `cd ../../` when default connection places you in `home/ubuntu`)
    - `sudo git clone https://github.com/spwhite1337/website.git`
    - `cd website`
    - `source initialization.sh`

- Serve Website over HTTP
    - Set `VUE_APP_ROOT_API` in `website/frontend/.env.production` to external IP of EC2 instance
    - `cd website`
    - `sudo docker-compose -f docker-compose-http.yml up --build`

---

### Add SSL Certification

SSL Certification is a free process from [Let's Encrypt](https://letsencrypt.org/) to enable transfer of data over
HTTPS and removal of that annoying and embarrassing warning that chrome puts on sites without SSL certification. 

First, generate an SSL certificate with Let's Encrypt / Certbot on a test site served over the domain 
[Reference](https://www.humankode.com/ssl/how-to-set-up-free-ssl-certificates-from-lets-encrypt-using-docker-and-nginx).
- Stop and prune any running containers (e.g. `sudo docker system prune -a`)
- `cd letsencrypt`
- `sudo docker-compose up -d`
- Go to `http://scottpwhite.com` and `http://www.scottpwhite.com` to verify site is working over http
- In another session, test the certification process with:
    - `source letsencrypt-staging.sh`
    - Ensure success with `source letsencrypt-info.sh`
    - You should see something like the following:
        
     <img src="docs/>

- Generate the certificates and save them to docker-volumes
    - Note: rate limits are currently at 50 certificates per domain per week. Should be plenty but best not waste them.
    - Remove staging volumes: `sudo docker rm -rf /docker-volumes/`
    - Get certs with `source letsencrypt-prod.sh`
    - See info with `source letsencrypt-info.sh`

- Shut down initial certication container with: `sudo docker-compose down`

Second, set up a process to automatically renew SSL certificates in the docker environment:
- @TODO
