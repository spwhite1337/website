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
    
- Install Docker and run at startup
    - `sudo apt-get update`
    - `sudo apt install docker.io`
    - `sudo systemctl start docker`
    - `sudo systemctl enable docker`
 
- Set up project
    - `git clone [this repo]`
    - `cd website/backend`
    - `pip install awscli`
    - `aws configure`
        - Add AWS Keys
    - `python download`
    - `cd ../`

- Run project
    - Set environment variable to external IP of EC2 instance
    - `docker-compose up --build`
