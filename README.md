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
