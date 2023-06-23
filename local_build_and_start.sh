#!/bin/sh

cd ./mariadb
docker build --tag deniskasak/uni-nao:mariadb .

cd ..

cd ./transcriber
docker build --tag deniskasak/uni-nao:transcriber .

cd ..

cd ./webserver
docker build --tag deniskasak/uni-nao:webserver .

cd ..

docker-compose up -d
