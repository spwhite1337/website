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

- Set Up AWS EC2 instance: 
    - Ubuntu 18.04 Image
    - t2.small (~$0.0023 / hour or ~$16 / month)
        - t2.micro works if you download the `minified` branch of `card-classifier`, otherwise you will get a 
        `Killed` error during install of `master` on t2.micro (I assume `tensorflow` is the culprit). This is ~1/2 the 
        price of t2.small.
    - Optional: Check Spot Requests to lower costs. But be warned that Amazon is on bullshit and your instance will 
    disappear without explanation.
    - Enable Auto-assign Public IP
    - 10-12 GB EBS (Costs ~$0.10 GB / month)
    - Security Group `Website`:
        - SSH on 22
        - HTTP on 80
        - HTTPS on 443
    - IAM Instance Profile: `ec2-s3access` to connect EC2 to S3
    
- Set up project
    - SSH into instance
    - Go to server root (EC2 defaults login as `ubuntu` so just `cd ../../` after ssh-ing in)
    - `sudo git clone https://github.com/spwhite1337/website.git`
        - To setup SSH on EC2 for Github
            - From home: `ssh-keygen -t ed25519 -C "spwhite1337@gmail.com"`
            - `eval "$(ssh-agent -s)"`
            - `ssh-add ~/.ssh/id_ed25519`
            - `cat ~/.ssh/id_ed25519.pub`
            - Paste output to github SSH keys
            - Test connection: `ssh -T git@github.com`
    - `cd website`
    - `source initialization.sh`
        
### 2.) Serve over HTTP

- `cd website`
- `sudo sh -c "echo 'VUE_APP_ROOT_API=http://scottpwhite.com' > frontend/.env.production"`
- `sudo docker-compose -f docker-compose-http.yml up --build`

---

### 3.) Configure AWS

- Can't figure this out yet...

