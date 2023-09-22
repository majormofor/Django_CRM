import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'
)


# prepare a cursor object
cursorObject = dataBase.cursor()

#create a dataBase
cursorObject.execute("CREATE DATABASE mofor")

print("All done!")