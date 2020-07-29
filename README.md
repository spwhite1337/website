# Vue only

To re-bebuild from scratch:
- Install node.js and npm
- `npm install -g @vue-cli-init`
- `vue init webpack frontend`
- `cd frontend`
- `npm install`
- `npm run dev` to test locally

### Docker

- `docker build -t vue-only .`
- `docker run -it -p 8080:8080 --rm --name vue-only-01 vue-only`
