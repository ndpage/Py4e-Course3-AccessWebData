
import re # import regular expression module

numList = []  # create list for all numbers
total = 0
count = 0
fhandle = open('sample.txt')  #open handle for sample text file

for line in fhandle:
  numList = re.findall('[0-9]+',line)
  if len(numList) < 1:
    continue
  for num in numList:
    num = int(num)
    total = total + num
    count = count + 1

print("Found",count, "numbers")
print("Total is", total)
