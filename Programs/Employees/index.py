#!/usr/bin/python

import pymysql
from sys import argv

pymysql.install_as_MySQLdb()

import MySQLdb

# connect
db = MySQLdb.connect("localhost", "root", "", "cmd")

# prepare a cursor object using cursor() method
cursor = db.cursor()

script, quantity, price = argv
print(quantity*price)

# query = ("SELECT Id, Name FROM Student")
query = ("INSERT INTO products(quantity,price,total) VALUES("+quantity+","+ price+","+ quantity+price+"")

cursor.execute(query)

# for (Id, Name) in cursor:
#	print(Id, Name)

cursor.close()
db.close()