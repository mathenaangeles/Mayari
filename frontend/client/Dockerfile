FROM node:12.2.0-alpine
EXPOSE 8080

WORKDIR /app
COPY package.json /app/package.json
RUN npm install
RUN npm install @vue/cli -g

CMD ["npm", "run", "serve"]

# build stage
# FROM node:lts-alpine as build-stage
# WORKDIR /app
#COPY package*.json ./
#RUN npm install
#COPY . .
#RUN npm run build

# production stage
#FROM nginx:stable-alpine as production-stage
#COPY --from=build-stage /app/dist /usr/share/nginx/html
#EXPOSE 80
#CMD ["nginx", "-g", "daemon off;"]