# base image
FROM node:lts-alpine

# set working directory
WORKDIR /app

COPY package*.json ./

RUN npm install
RUN npm install @vue/cli -g

COPY . .

# start app
CMD ["npm", "run", "serve"]


## production stage
#RUN npm run build
#FROM nginx:stable-alpine as production-stage
#COPY --from=build-stage /app/dist /usr/share/nginx/html
#COPY --from=build-stage /app/nginx.conf /etc/nginx/conf.d/default.conf
#EXPOSE 80
#CMD ["nginx", "-g", "daemon off;"]