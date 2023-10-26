# syntax=docker/dockerfile:1

FROM python:3.12

WORKDIR /app

COPY Pipfile .
COPY envfile.txt .
RUN cp envfile.txt .env

RUN apt-get update
RUN apt-get update && apt-get install -y gnupg2
RUN apt-get install -y curl apt-transport-https
RUN apt-get update
RUN python -m pip install --upgrade pip
RUN pip3 install pipenv
RUN pipenv --python 3.12
RUN pipenv install
RUN pipenv requirements > requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY . .
