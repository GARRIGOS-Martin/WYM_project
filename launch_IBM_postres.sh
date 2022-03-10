#! /bin/bash

# Docker Summarize
sudo docker run -it -p 5000:5000 quay.io/codait/max-text-summarizer
# Docker Postgres
sudo docker run --name wym_db -e POSTGRES_PASSWORD=admin -e POSTGRES_USER=wym_admin -p 5432:5432 -d postgres 
# Docker sentiment
sudo docker run -it -p 5005:5000 codait/max-text-sentiment-classifier

FROM ubuntu:16.04

#MAINTANER Your Name "youremail@domain.tld"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]