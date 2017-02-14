#!/usr/bin/python

import pymysql

pymysql.install_as_MySQLdb()

import MySQLdb

# connect
db = MySQLdb.connect("localhost", "root", "", "cmd")

# prepare a cursor object using cursor() method
cursor = db.cursor()

query = ("SELECT Id, Name FROM Student")

cursor.execute(query)

for (Id, Name) in cursor:
	print(Id, Name)

cursor.close()
db.close()