import urllib.request
import re

url = 'http://www.google.co.za'

# connect to a URL
website = urllib.request.urlopen(url)

# read html code
html = website.read()

# use re.findall to get all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)


print(links)