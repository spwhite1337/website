# Website

Personal website to display some data products and my personal blog to impose my will on the internet. 

<img src="docs/logo.jpg" alt="Website logo" width=256>

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
    
- Update DNS records in GoDaddy account
    - Log-in -> Scott White (upper right) -> Manage Domains -> DNS -> Manage Zones -> Search `scottpwhite.com`
    - Match records to the IP Address from the EC2 instance
    
    <img src="docs/DNS_records.JPG" alt="DNS Records" width=256>
    
- Set up project
    - Go to instance root (on EC2; `cd ../../` when default connection places you in `home/ubuntu`)
    - `sudo git clone https://github.com/spwhite1337/website.git`
    - `cd website`
    - `source initialization.sh`

- Run project
    - Set environment variable to external IP of EC2 instance
    - `sudo docker-compose up --build`
