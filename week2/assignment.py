
import re # import regular expression module

numList = []  # create and intialize variables
total = 0
count = 0

fhandle = open('act_data.txt')  # open handle for text file

for line in fhandle:
  numList = re.findall('[0-9]+',line)  # finall all integers in the line with at least 1 number
  if len(numList) < 1:
    continue
  for num in numList: 
    num = int(num)      # convert to int so we can sum the items in the number list
    total = total + num # sum the total off th numbers
    count = count + 1   # increment the count of numbers that have been found

print("Found",count, "numbers")  # print the resulting count and sum total
print("Total is", total)
