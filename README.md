# Website



## Procedure

- Set Up AWS EC2 instance: 
    - Ubuntu 18.04 Image
    - t2.small
    - with Spot Requests
    - Add a subnetwork
    - Enable IP
    - 16 GB EBS
    - Open to HTTP / HTTPS
    - SSH into instance
    
- Install Docker and run at startup (https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04)
    - `sudo apt-get update`
    - `sudo apt install apt-transport-https ca-certificates curl software-properties-common`
    - `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`
    - `sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"`
    - `sudo apt update`
    - `sudo apt install docker-ce`
    Docker-compose
    - `sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
    - `sudo chmod +x /usr/local/bin/docker-compose`
 
- Set up project
    - `git clone [this repo]`
    - `cd website/backend`
    - `sudo apt install awscli`
    - `aws configure`
        - Add AWS Keys
    - `python3 download`
    - `cd ../`

- Run project
    - Set environment variable to external IP of EC2 instance
    - `sudo docker-compose up --build`
