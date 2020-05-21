FROM node:8.7.0-alpine

RUN mkdir -p /srv/app/react-client
WORKDIR /srv/app/react-client


COPY package.json /srv/app/react-client
COPY package-lock.json /srv/app/react-client

RUN npm install

EXPOSE 3000

COPY . ./

CMD ["npm","start"]