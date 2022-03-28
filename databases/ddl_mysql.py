import mysql.connector
from mysql.connector import errorcode
# import connect_mysql as cm
from .connect_mysql import DatabaseConnection

DB_NAME = 'python_mysql'
PYTHON_TABLE_1 = 'python_table_1'
#global dictionary var
TABLE = {}
#get mysql db connection
dbConn = DatabaseConnection().db_conn()

class DatabaseDefinitionSQL:

    def create_table(self):
        TABLE[PYTHON_TABLE_1] = (
        "CREATE TABLE IF NOT EXISTS python_mysql.python_table_1 ("
        "id INT auto_increment NOT NULL,"
        "python_version varchar(100) NULL,"
        "os_name varchar(100) NULL,"
        "os_version varchar(100) NULL,"
        "PRIMARY KEY (`id`)"
        ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"
        )

        try:
            dbConn.cursor().execute(TABLE[PYTHON_TABLE_1])
            print('Create table successful with command: \n' + TABLE[PYTHON_TABLE_1])
        except mysql.connector.Error as err:
            print('Create table with error: ' + err)