# Scott's Website

Personal Website with flask+vue to display data products and my blog.

## Procedure

- Python 3.5
- Node.js
- npm
- aws credentials


## Set up Client-Side

#### Development

- `cd frontend`
- `npm install`
- `npm run dev`

#### Production

- `cd frontend`
- Set environ var `process.env.BASE_URL`
- `npm install`
- `npm run build`
- `npm run`


## Set up Server-Side
- `cd backend`
- `export / set FLASK_APP=run.py`
- `export / set FLASK_DEBUG=1`

### Hints because I am new to vue / javascript

- Very useful tutorial: https://codeburst.io/full-stack-single-page-application-with-vue-js-and-flask-b1e036315532
- Deployment https://stackabuse.com/single-page-apps-with-vue-js-and-flask-deployment/
- https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04

## Production Server

- `sudo apt-get update`
- `wget https://repo.continuum.io/archive/Anaconda3-2018.12-Linux-x86_64.sh`
- `bash Anaconda3-2018.12-Linux-x86_64.sh`
- `source .bashrc`
- `sudo apt-get install nginx nodejs npm`
- `sudo apt-get install libsm6 libxrender1 libfontconfig1`
- `git clone website / card-classifier / sports-bettors / presidents-speeches`
- `conda create -n website python=3.5`
- `conda activate website`
- `pip install -e .`
- `pip install ../card-classifier && pip install ../sports-bettors && pip install ../presidents-speeches`
- `aws configure`