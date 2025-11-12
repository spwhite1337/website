# Website

Personal website to display some data products and to impose my will on the internet via blog. 

<img src="docs/logos/logo.jpg" alt="Website logo" width=256>

---
<p>
<img src="docs/logos/flask_logo.png" alt="Flask Logo" width=128/>
<img src="docs/logos/vue_logo.png" alt="vue Logo" width=128/>
<img src="docs/logos/docker_logo.png" alt="Docker Logo" width=128/>
<img src="docs/logos/nginx_logo.png" alt="NGINX Logo" width=128/>
<img src="docs/logos/aws_logo.png" alt="AWS Logo" width="128"/>
</p>

---

## Development

Run two independent apps that do not communicate with each other for debugging and dev. Requires: Python 3.9+ and npm.

- `cd backend`
- `set FLASK_APP=run.py` (`export FLASK_APP=run.py`)
- `pip install -e .`
- `flask run`
- `cd frontend`
- `npm install`
- `npm run serve`

The full app can be run through docker but tends to slow down my computer a lot.
- `cd website`
- `echo "VUE_APP_ROOT_API=http://localhost > frontend/.env.production`
- `docker-compose -f docker-compose-http.yml up --build`

## Server

### 1.) Create Instance and Download Files

- a.) Set Up AWS EC2 instance: 
    - Ubuntu
    - t2.small (~$0.0023 / hour or ~$16 / month) (t2.micro takes too long to build)
    - Enable Auto-assign Public IP
    - 10-12 GB EBS (Costs ~$0.10 GB / month)
    - Security Group `Website`:
        - SSH on 22
        - HTTP on 80
        - HTTPS on 443 (optional)
    - IAM Instance Profile: `ec2-s3access` to connect EC2 to S3

- b.) Set up project
    - Connect to instance (e.g., EC2 Connect, SSH)
    - Create SSH for github
        - From `home`: `ssh-keygen -t ed25519 -C "[email]"`
        - `eval "$(ssh-agent -s)"`
        - `ssh-add ~/.ssh/id_ed25519`
        - `cat ~/.ssh/id_ed25519.pub`
        - Paste output to github SSH keys
        - Test connection: `ssh -T git@github.com`
    - `sudo git clone https://github.com/spwhite1337/website.git`
    - `cd website`
    - `source initialization.sh`
        
### 2.) Serve over HTTP

- `cd website`
- `sudo sh -c "echo 'VUE_APP_ROOT_API=http://scottpwhite.com' > frontend/.env.production"`
- `sudo docker-compose -f docker-compose-http.yml up --build`

### 3.) Configure AWS

- Starting with a EC2 server over HTTP (see Step 1a) and a registered domain name (e.g., `scottpwhite.com`, I used Amazon Route 53 for domain registration)
- Make a "Target Group" in AWS that contains the EC2 instance hosting the website
- Create a certificate in AWS Certificate Manager (ACM) for the domain name
- Create an Application Load Balancer that (i) redirects HTTP to HTTPS, (ii) forwards HTTPS requests to the Target Group containing the EC2 instance hosting the webpage with the associated Certificate from ACM
- Register the certificate and load balancer in the DNS records for the domain (I used Route 53 in AWS).

Requests sent to `https://scottpwhite.com` (`http` redirects) will first go to the Load Balancer which then forwards them (with SSL certification, auto-renewing) to the Target Group containing the EC2 instance running the site. If we need to beef up servers or add more we simply add them to the Target Group and direct them in the front end of the site.

