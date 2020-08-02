# Website

Personal website to display some data products and to impose my will on the internet via blog. 

<img src="docs/logo.jpg" alt="Website logo" width=256>

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
    - Set environment variable to external IP of EC2 instance
    - `sudo docker-compose up --build`

### Add SSL Certification

SSL Certification is a free process from [Let's Encrypt](https://letsencrypt.org/) to enable transfer of data over
HTTPS and removal of that annoying and embarassing warning that chrome puts on sites without SSL certification. 

First, generate a 
- Add SSL Certification [Reference](https://www.humankode.com/ssl/how-to-set-up-free-ssl-certificates-from-lets-encrypt-using-docker-and-nginx)
    - Stop and prune any running containers (e.g. `sudo docker system prune -a`)
    - 
    - `cd letsencrypt`
    
    
