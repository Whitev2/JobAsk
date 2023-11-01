FROM node:18

WORKDIR /app

COPY package*.json ./
COPY . ./

RUN npm cache clean --force
RUN npm install
RUN npm run build

EXPOSE 80


ENTRYPOINT ["npm", "start"]
#ENTRYPOINT ["cd .nuxt"]
