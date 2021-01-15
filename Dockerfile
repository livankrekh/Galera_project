# base image
FROM node:14.15.3

# set working directory
WORKDIR client/app

COPY /client/package.json package.json
RUN npm install
COPY /client .
RUN npm install @vue/cli@4.5.10 -g

# start app
CMD ["npm", "run", "serve"]