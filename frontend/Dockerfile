# build stage
FROM node:lts-alpine as build-stage
WORKDIR /frontend
COPY package*.json ./
ENV NODE_OPTIONS=--openssl-legacy-provider
RUN npm install
COPY . .
RUN npm run build

# production stage
FROM nginx:latest as production-stage
COPY --from=build-stage /frontend/dist /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]
