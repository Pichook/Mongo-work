
import mysql.connector
import pymongo


client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb = client['mongo_mysql']

work = mydb.mongo_mysqlwork

mysqldb = mysql.connector.connect(
    host="localhost",
    database="kit_db",
    port = '3306',
    user="root",
    password="fluffy1324##")

cursor = mysqldb.cursor(dictionary = True)

cursor.execute(f"select * from students")

student = cursor.fetchall()

if len(student) > 0:
    a = work.insert_many(student)
    print(len(a.inserted_ids))