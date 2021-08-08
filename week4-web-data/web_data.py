# import urllib.request, urllib.parse, urllib.error

# fhandle = urllib.request.urlopen('https://www.py4e.com/')

# for line in fhandle: 
#   print(line.decode().strip())

wpHandle = open('webpage.html', 'w')

from urllib.request import Request, urlopen
url="https://stackoverflow.com/search?q=html+error+403"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()

webpage = web_byte.decode('utf-8')

for line in webpage:
  wpHandle.write(line)

wpHandle.close()