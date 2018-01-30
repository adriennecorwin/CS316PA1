#!/usr/bin/python3

import cgi
import cgitb

print("Content-type:text/html\n\n")
cgitb.enable()

def showTranslation(a, b, c, d):
	print("Origin Language: %s\n" % a)
	print("Requested Language: %s\n" % b)
	print("Original word: %s\n" % c)
	print("Translation: %s\n" % d)

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

def translate(bigData, originLang, transLang, theWord):
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
		return "not found"
	else:
#		print(translatedWord)
		return translatedWord

def main():
	form=cgi.FieldStorage()
	theWord = str(form.getvalue('theword')).lower()
	originLang = str(form.getvalue('fromnative')).lower()
	transLang = str(form.getvalue('newlanguage')).lower()
	translationArray=store()
	translatedWord=translate(translationArray, originLang, transLang, theWord)
	showTranslation(originLang, transLang, theWord, translatedWord)

if __name__=="__main__":main()

