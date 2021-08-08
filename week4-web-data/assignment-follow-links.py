# Author: Nathan Page
# Assignment: Following Links in Python 
# Date: August 8, 2021

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Initialize variables
links = []
names = []

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
# url =  'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
count = input('Enter count: ')
position = input('Enter position: ')

try:
  count = int(count)
  position = int(position)
except:
  print('Please enter only integer values for count and position')
  quit()

# Iterate through the links the number of times determined by count variable
i=0
while i<=count:
  print(url)
  
  # get html content 
  html = urllib.request.urlopen(url, context=ctx).read()
  soup = BeautifulSoup(html, 'html.parser')
  
  # Retrieve all of the anchor tags
  tags = soup('a')
  for tag in tags:
      link = tag.get('href', None)
      links.append(link)

  # update the url variable with the next link to follow
  url = links[position-1]
  links.clear() # need to clear links array after getting next link
  i=i+1 
