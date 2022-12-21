FROM ubuntu:20.04

# MAINTAINER: 개발자 정보를 나타냅니다. 
MAINTAINER "shpusan001@gmail.com"

RUN apt-get update && \
  apt-get install -y --no-install-recommends tzdata g++ curl
RUN apt-get install -y python3-pip python3-dev 
RUN cd /usr/local/bin && \
  ln -s /usr/bin/python3 python && \
  ln -s /usr/bin/pip3 pip && \
  pip install --upgrade pip

COPY . /app
WORKDIR /app

RUN pip install -r /app/requirements.txt

EXPOSE 8000

CMD cd /app && uvicorn --host=0.0.0.0 App:app --workers 8
