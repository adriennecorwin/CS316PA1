#!/usr/bin/python

import cgi
import cgitb

print("Content-type:text/html\n\n")
cgitb.enable()

def showTranslation(a, b, c, d):
	print("Origin Language: %s\n" % a)
	print("Requested Language: %s\n" % b)
	print("Original word: %s\n" % c)
	print("Translation:")

def store():
	bigData=[]
	file = open("xarn_language.txt", "r")
	for line in file:
		line=line.rstrip()
        	smallData = line.split(",")
        	bigData.append(smallData)
#	print(bigData)
	file.close()
	return bigData

def translate(bigData):
	#strings from input
	theWord = "agua"
	originLang = "spanish"
	transLang = "english"
	translatedWord = ""

	firstLangCol = 0
	firstWordCol = 1
	secondLangCol = 2
	secondWordCol = 3

	found = False
	counter=0
	while not found and counter<len(bigData):
		checkRow=bigData[counter]
    		if theWord == checkRow[firstWordCol] and originLang == checkRow[firstLangCol] and transLang == checkRow[secondLangCol]:
			translatedWord = checkRow[secondWordCol]
        		found = True
    		elif theWord == checkRow[secondWordCol] and originLang == checkRow[secondLangCol] and transLang == checkRow[firstLangCol]:
			translatedWord = checkRow[firstWordCol]
			found = True
		else:
			counter=counter+1
	if not found:
		print "not found"
	else:
#		print(translatedWord)
	return translatedWord

def main():
	translationArray=store()
	translate(translationArray)

if __name__=="__main__":main()

#form=cgi.FieldStorage()
#nLang=(form.getvalue('nativeLang'))
#nWord=(form.getvalue('nativeWord'))
#tLang=(form.getValue('transLang'))
#tWord=translate(bigData)
