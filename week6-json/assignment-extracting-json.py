# Author: Nathan Page
# Assignment: Extracting Data from JSON
# Description: Extact JSON that contains a list of users and comment count, and sum the total number of comments and how many users are in the list 
# Date: August 13, 2021

# Import necessary modules
import json
import urllib.request

# Init variables
num = 0
sumtotal = 0

url = input('Enter location: ') # get url/location from user

print('Retrieving',url)
urlhand = urllib.request.urlopen(url) # send url open and get the handle

data = urlhand.read() # read all data returned from urlopen()

info = json.loads(data) # load json data into a dictioinary
print('User count:', len(info['comments']))

for comment in info['comments']:    # info['comments'] gets the list of comments
    name = comment['name']          # each sub dict has a name
    count = comment['count']        #  and a count of the comments made
    num = num + 1
    sumtotal = sumtotal + int(count)
    
# print results
print('Count', num)
print('Sum', sumtotal)