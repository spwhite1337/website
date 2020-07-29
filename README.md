# Vue only

To re-bebuild from scratch:
- Install node.js and npm
- `npm install -g @vue-cli`
- `vue create frontend`
- `cd frontend`
- `npm install`
- `npm run dev` to test locally

### Docker

- `cd frontend`
- `docker build -t vue-nginx .`
- `docker run -it -p 8080:80 --rm --name vue-nginx-01 vue-nginx`
- `http://localhost:8080`