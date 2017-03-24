# Import the modules
import sys
import random

lookuparr = {1 : 'It is certain', 
			 2 : 'Outlook good', 
			 3 : 'You may rely on it', 
			 4 : 'Ask again later', 
			 5 : 'Concentrate and ask again', 
			 6 : 'Reply hazy, try again', 
			 7 : 'My reply is no', 
			 8 : 'My sources say no'}

ans = True

while ans:
	question = input("Ask the magic 8 ball a question: (press enter to quit)")

	answers = random.randint(1, 8)

	if question == "":
		sys.exit()

	print(lookuparr[answers])