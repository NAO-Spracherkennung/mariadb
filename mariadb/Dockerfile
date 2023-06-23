FROM mariadb:latest

# Set the environment variables
ENV MYSQL_ROOT_PASSWORD=nao

EXPOSE 3306

# Copy the import.sql file into the docker-entrypoint-initdb.d directory
COPY import.sql /docker-entrypoint-initdb.d/
