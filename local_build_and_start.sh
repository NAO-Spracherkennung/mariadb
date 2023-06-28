#!/bin/sh

docker-compose up -d

pip install -r webserver/requirements.txt

cd webserver

python3 -m flask run