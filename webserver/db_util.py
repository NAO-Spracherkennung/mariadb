from mariadb import connect, Cursor
import os

DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "nao")
DB_DATABASE = os.getenv("DB_DATABASE", "nao")


#create mariadb connection
def getDbConnection()->Cursor:
    return connect(
            host=DB_HOST,
            port=int(DB_PORT),
            user=DB_USER,
            password=DB_PASS,
            database=DB_DATABASE,
            autocommit=True
        ).cursor()