#!/bin/sh

# MariaDB Docker bauen
cd mariadb
docker build -t uni-nao:mariadb .
cd ..

# MariaDB Docker starten
docker-compose --env-file .env up -d

# Virtuellen Python3 Interpreter installieren
python3 -m venv .venv

# Virtuellen Python3 Interpreter aktivieren
source .venv/bin/activate

# Webserver dependencies installieren
pip install -r webserver/requirements.txt

# Webserver starten
cd webserver
python -m flask run --host=0.0.0.0 --port=1222