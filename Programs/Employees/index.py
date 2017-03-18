#!/usr/bin/python

import pymysql
from sys import argv

name = input("Enter the name you want to store: ")

pymysql.install_as_MySQLdb()

import MySQLdb

# connect
db = MySQLdb.connect("localhost", "root", "", "college")

# prepare a cursor object using cursor() method
cursor = db.cursor()

query  = "INSERT INTO student(Name) VALUES(%s)"
args   = (name)

cursor.execute(query, args)

sql    = "SELECT Name FROM student"
cursor.execute(sql)
result = cursor.fetchall()

for n in result:
	print(" | ".join(n))

cursor.close()
db.close()