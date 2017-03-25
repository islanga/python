# from urllib import urllib2
import urllib.request
import json

url   		= "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&"

query 		= input("What do you want to search for ? >> ")

query 		= urllib.parse.urlencode({'q' : query })

response 	= urllib.request.urlopen(url + query).read().decode('utf8')

data 		= json.loads(response)

print(data)

results 	= data['responseData']['results']

for result in results:
	title = result['title']
	url   = result['url']
	print(title + '; ' + url)