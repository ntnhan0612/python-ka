import mysql.connector
from mysql.connector import errorcode
from .connect_mysql import DatabaseConnection

DB_NAME = 'python_mysql'
PYTHON_TABLE_1 = 'python_table_1'

#get mysql db connection
dbConn = DatabaseConnection().db_conn()

class DatabaseManipulationSQL:

    def insert_data(self):

        #dinamic value parameters
        INSERT_DATA_QUERY = (
            "INSERT INTO python_mysql.python_table_1"
            "(python_version, os_name, os_version) "
            "VALUES(%(python_version)s, %(os_name)s, %(os_version)s);"
        )

        #inserted dictionary data
        data_python = {
            'python_version': '3.3',
            'os_name': 'window',
            'os_version': '10',
        }

        try:
            dbConn.cursor().execute(INSERT_DATA_QUERY, data_python)
            dbConn.commit()
            print("Insert data successful with SQL command: \n" + INSERT_DATA_QUERY)
        except mysql.connector.Error as err:
            print('Insert data into ' + PYTHON_TABLE_1 + ' with err: ' + err)

    def select_data(self):
        SELECT_DATA_QUERY = "SELECT * FROM python_mysql.python_table_1"

        cs = dbConn.cursor(buffered=True)
        cs.execute(SELECT_DATA_QUERY)
        result = cs.fetchall()
        for row in result:
            print(row)
        