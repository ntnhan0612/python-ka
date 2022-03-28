# importing required libraries
import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'python_mysql'

class DatabaseConnection:

  def db_conn(self):
    try:
      dbConn = mysql.connector.connect(
        user='nhan', #username
        password='nhan', #password
        host='localhost', #host
        database='python_mysql', #database name
        auth_plugin='mysql_native_password' # if the server is configured to use sha256_password by default and you want to connect to an account that authenticates using mysql_native_password
      )
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)

    print("MySQL connected")
    return dbConn

  def close_db_conn(self, conn):
    conn.cursor().close()
    conn.close()
    print("Connection is closed")


  # db_cursor()