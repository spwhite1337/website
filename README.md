### Vue-Only 

To re-bebuild from scratch:
- Install node.js and npm
- `npm install -g @vue-cli`
- `vue create frontend`
- `cd frontend`
- `npm install`
- `npm run dev` to test locally

#### Vue-Nginx on Docker

- `cd frontend`
- `docker build -t vue-nginx .`
- `docker run -it -p 8080:80 --rm --name vue-nginx-01 vue-nginx`

### Flask only

- `cd backend`
- `conda activate backend`
- `pip install -e .`
- `set FLASK_APP=run.py`
- `flask run`

#### Flask on Docker

- `cd backend`
- `docker build -t flask .`
- `docker run -it -p 5000:5000 --rm --name flask-01 flask`

### Docker

- `cd frontend`
- `docker build -t vue-nginx-flask .`
- `docker run -it -p 8080:80 --rm --name vue-nginx-flask-01 vue-nginx-flask`
- `http://localhost:8080`