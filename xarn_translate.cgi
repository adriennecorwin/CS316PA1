#!/usr/bin/python3

import cgi
import cgitb

NOTFOUND='unknown'
NOVAL='none'
MISSING='invalid'

print("Content-type:text/html\n\n")
cgitb.enable()


def showTranslation(a, b, c, d):
	print("<style> .found {color:green} .notfound {color:red} .proper{color:blue}</style>")
	print("<html><head><title>Translate</title></head><body>")
	print("<p><span class=\"proper\">Origin Language: </span>")
	print("%s" % a)
	print("</p><p><span class=\"proper\">Requested Language: </span>")
	print("%s" % b)
	print("</p><p><span class=\"proper\">Original word: </span>")
	print("%s" % c)
	print("</p><p><span class=\"proper\">Translation: </span>")
	if d != NOTFOUND:
		print("<span class=\"found\">")
		print("%s" % d)
		print("</span>")
		print("</p></body></html>")
	else:
		print("<span class=\"notfound\">")
		print("%s" % d)
		print("</span>")
		print("</p></body></html>")

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
		return NOTFOUND
	else:
#		print(translatedWord)
		return translatedWord

def main():
	form=cgi.FieldStorage()
	hadError=False
	if str(form.getvalue('theword')).lower() == NOVAL:
		hadError=True
		theWord=MISSING
	else:
		theWord=str(form.getvalue('theword')).lower()

	if str(form.getvalue('fromnative')).lower() == NOVAL:
		hadError=True
		originLang=MISSING
	else:
		originLang=str(form.getvalue('fromnative')).lower()

	if str(form.getvalue('newlanguage')).lower() == NOVAL:
		hadError=True
		transLang=MISSING
	else:
		transLang=str(form.getvalue('newlanguage')).lower()

	if hadError:
		translatedWord=NOVAL
		showTranslation(originLang, transLang, theWord, translatedWord)
	else:
		translationArray = store()
		translatedWord = translate(translationArray, originLang, transLang, theWord)
		showTranslation(originLang, transLang, theWord, translatedWord)

if __name__=="__main__":main()
