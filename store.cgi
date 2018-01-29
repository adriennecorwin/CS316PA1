#!/usr/bin/python

import cgi
import cgitb

print("Content-type:text/html\n\n")
cgitb.enable()

bigData=[]
file = open("xarn_language.txt", "r")
for line in file:
        smallData = line.split(",")
        bigData.append(smallData)
print bigData

