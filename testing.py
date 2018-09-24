'''#import cx_Oracle
import pymysql
#pymysql.install_as_MySQLdb()
db=pymysql.connect("localhost","root","root","test")
cur=db.cursor()
cur.execute("select version()")
data=cursor.fetchone()
print("Database version: %s",data)
db.close()
print('Sucessfully imported')
'''

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="test"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employe")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
