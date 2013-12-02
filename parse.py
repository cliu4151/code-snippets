#!/usr/bin/env python

import re

# Open a file
main = open ("WebExtract.txt", "r")

# File to be written to
writ = open ('10032.txt','w')


# Loop through lines in file 'main'
for line in main:
    # line of file is json
    # split the line by comma, store results in temp
    temp = line.split(',');
    
    # create match objects
    # pattern match certain parts of the line
    matchObj = re.match(r'"1"', temp[2], re.M | re.I)
    matchObj2 = re.match(r'"10032"', temp[5], re.M | re.I)
    
    # check matches and then write to file if match
    if matchObj and matchObj2:
        writ.write(line)

# close files
main.close()
writ.close()
