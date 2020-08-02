# Website

Personal website to display some data products and my personal blog to impose my will on the internet. 

<img src="docs/logo.jpg" alt="Website logo" width=256>

## Procedure

- Set Up AWS EC2 instance: 
    - Ubuntu 18.04 Image
    - t2.small (~$0.0023 / hour or ~$16 / month)
        - Can't install project on t2.micro (Exits with `Killed` error)
    - Spot Requests
    - Select a subnetwork (probably unnecessary)
    - Enable Auto-assign Public IP
    - 16 GB EBS (Can maybe go smaller but I don't think this increases cost significantly)
    - Security Group `Website`:
        - SSH on 22
        - HTTP on 80
        - HTTPS on 443
        - Custom TCP on 5000 (for backend)
    
- Update DNS records in GoDaddy account
    - Log-in -> Scott White (upper right) -> Manage Domains -> DNS -> Manage Zones -> Search `scottpwhite.com`
    - Match records to the IP Address from the EC2 instance
    
    <img src="docs/DNS_records.JPG" alt="DNS Records" width=256>
    
- Set up project
    - SSH into instance
    - Go to instance root (on EC2; `cd ../../` when default connection places you in `home/ubuntu`)
    - `sudo git clone https://github.com/spwhite1337/website.git`
    - `cd website`
    - `source initialization.sh`

- Run project
    - Set environment variable to external IP of EC2 instance
    - `sudo docker-compose up --build`
