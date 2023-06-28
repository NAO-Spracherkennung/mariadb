# MariaDB Docker bauen

Set-Location -Path ".\mariadb"
docker build -t uni-nao-mariadb .
Set-Location -Path ".."

#MariaDB Docker starten
docker-compose --env-file .env up -d

# Virtuellen Python3 Interpreter installieren
python -m venv .venv

# Virtuellen Python3 Interpreter aktivieren
.\.venv\Scripts\Activate.ps1

# Webserver dependencies installieren
pip install -r .\webserver\requirements.txt

# Webserver starten
Set-Location -Path ".\webserver"
python -m flask run