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

- `git clone []`
- `sudo apt-get update`
- `apt-get install python3-pip python3-dev python3-venv nginx nodejs npm`
- `aws configure`