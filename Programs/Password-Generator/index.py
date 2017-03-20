import string
from random import *
characters = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(characters) for x in range(randint(8, 16)))

def writeFile(password):
	file = open("password.txt", "a+")
	file.writelines(password)
	file.close()

def readFile():
	file = open("password.txt", "r")
	print(file.read())
	file.close()

writeFile(password)
readFile()