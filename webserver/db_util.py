from mariadb import connect, Cursor
import os

DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_USER = os.environ["DB_USER"]
DB_PASS = os.environ["DB_PASS"]
DB_DATABASE = os.environ["DB_DATABASE"]


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