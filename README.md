# Website

Personal website to display some data products and my personal blog to impose my will on the internet. 

## Procedure

- Set Up AWS EC2 instance: 
    - Ubuntu 18.04 Image
    - t2.small
        - Can't install personal packages on t2.micro
    - Spot Requests
    - Select a subnetwork (probably unnecessary)
    - Enable Auto-assign Public IP
    - 16 GB EBS (Can maybe go smaller but I don't think this increases cost significantly)
    - Open to HTTP / HTTPS on ports 80 and 5000 (Custom TCP, 5000, 0.0.0.0/0)
    - SSH into instance
    
- Install Docker and run at startup (https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04)
    - `sudo apt-get update`
    - `sudo apt -y install apt-transport-https ca-certificates curl software-properties-common`
    - `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`
    - `sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"`
    - `sudo apt update`
    - `sudo apt -y install docker-ce`
    Docker-compose
    - `sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
    - `sudo chmod +x /usr/local/bin/docker-compose`
 
- Set up project
    - `sudo git clone https://github.com/spwhite1337/website.git`
    - `cd website/backend`
    - `sudo apt -y install awscli`
    - `aws configure`
        - Add AWS Keys
    - `sudo python3 download.py`
    - `cd ../`

- Run project
    - Set environment variable to external IP of EC2 instance
    - `sudo docker-compose up --build`
