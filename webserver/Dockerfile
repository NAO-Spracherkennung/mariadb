# syntax=docker/dockerfile:1

FROM python:3.9.17-slim-bullseye

ENV TRANSCRIBER_HOST="transcriber"
ENV TRANSCRIBER_PORT="5000"
ENV DB_HOST="db"
ENV DB_PORT="3306"
ENV DB_USER="root"
ENV DB_PASSWORD="nao"
ENV DB_DATABASE="nao"


EXPOSE 5000

WORKDIR /app

COPY requirements.txt requirements.txt

# install MariaDBConnector/C
RUN apt-get update
RUN apt install wget curl gcc -y
RUN wget https://r.mariadb.com/downloads/mariadb_repo_setup
RUN chmod +x mariadb_repo_setup
RUN ./mariadb_repo_setup --mariadb-server-version="mariadb-10.6"
RUN apt install libmariadb3 libmariadb-dev -y

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]