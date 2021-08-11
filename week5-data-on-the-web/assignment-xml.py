# Author: Nathan Page
# Assignment: Extracting Data from XML
# Date: August 8th, 2021

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Init variables
total = 0
count = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Get location/URL
url = input('Enter location: ')
if len(url) < 1: quit()

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

results = tree.findall('.//count')

# Find count text values and add to sum total
for num in results:
  total = total + int(num.text) # Get .text value of tag and convert to an integer
  count = count + 1
print('Count:',count)
print('Sum:',total)