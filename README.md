# Deployment

Jede Komponente hat einen Ordner mit dem Code inkl. einer Dockerfile.

## MariaDB
image: deniskasak/uni-nao-mariadb\
port: 3306\
\
import.sql enthält alle notwendigen Daten für die Datenbank und wird im Docker Image mitgeliefert.\
Beim ersten Start des Dockercontainers, wird die MariaDB automatisch mit den Daten aus import.sql gefüllt:\
\
User: root\
Passwort: nao\
\
Datenbank: nao\
Tabellen: answers, generic_terms, synonyms\

## Transcriber
image: deniskasak/uni-nao-transcriber\
port: 5000\
\
Umgebungsvariablen:\
WHISPER_MODEL = tiny, small, base, medium, large\
\
Der Transcriber nutzt whisper mit WHISPER_MODEL, um die gesendete Audiodatei zu transkribieren\
\
POST /\
Audiodatei als file mitsenden\
Return: Text\

