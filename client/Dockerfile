FROM nginx:latest

# MAINTAINER: 개발자 정보를 나타냅니다. 
MAINTAINER "shpusan001@gmail.com"

RUN apt-get update && \
  apt-get install -y --no-install-recommends tzdata g++ curl

RUN apt-get install -y nodejs
RUN apt-get install -y npm

COPY . /app
WORKDIR /app

RUN npm i
RUN npm run build

EXPOSE 3000

RUN cp default.conf /etc/nginx/conf.d/default.conf

CMD nginx -g "daemon off;"