#!/usr/bin/python

import pymysql

pymysql.install_as_MySQLdb()

import MySQLdb

#	host	user	password
db = MySQLdb.connect("localhost", "root", "", "college")

# 	prepare a cursor object using cursor() method
cursor = db.cursor()

#	execute SQL query using execute() method()
cursor.execute("SHOW TABLES")

#	Fetch a single row using fetchone() method.
data = cursor.fetchmany()

for n in data:
	print ("Database version : %s " % n)

#	disconnect from server
db.close()