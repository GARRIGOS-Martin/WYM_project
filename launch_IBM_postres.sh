#! /bin/bash

# Docker Summarize
sudo docker run -it -p 5000:5000 quay.io/codait/max-text-summarizer
# Docker Postgres
sudo docker run --name wym_db -e POSTGRES_PASSWORD=admin -e POSTGRES_USER=wym_admin -p 5432:5432 -d postgres 