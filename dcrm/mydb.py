# install mysql on your computer
# http://dev.mysql.com/downloads/installer
# pip install mysql
# NOT pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector as mysql

# Attempt to establish a connection to the MySQL database
dataBase = mysql.connect(
    user = 'root',
    host = '172.22.80.1',
    passwd = 'authenticate'
)

# Check if the connection is successfully established

cursorObject = dataBase.cursor()
#cursorObject.execute("CREATE DATABASE crm_db")
print('All done!')

# prepare a cursor object
