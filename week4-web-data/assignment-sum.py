# Author: Nathan Page
# Assignment: Scraping Numbers from HTML using BeautifulSoup
# Date: August 7, 2021

# import necessary libraries to scrap, parse, and format html (BeautifulSoup)
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Initalize sum total variable
tot = 0
count = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Get URL to read data from
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    num = int(tag.get_text()) # convert number string to an integer
    tot = tot + num # add current number to count total 
    count = count + 1

print('Count',count)
print('Sum',tot)