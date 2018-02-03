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

#not called anywhere, added to the translate function
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


def translate(originLang, transLang, theWord):
	translatedWord = ""

        FIRSTLANG = 0
        FIRSTWORD = 1
        SECONDLANG = 2
        SECONDWORD = 3

        found = False

	file = open("xarn_language.txt", "r")

        for line in file:
		line=line.rstrip()	
		entry = line.split(",")
                if theWord == entry[FIRSTWORD] and originLang == entry[FIRSTLANG] and transLang = entry[SECONDLAG]:
                        translatedWord = entry[SECONDWORD]
                        found = True
                        break
                elif theWord == entry[SECONDWORD] and originLang == entry[SECONDLANG] and transLang == entry[FIRSTLANG]:
                        translatedWord = entry[FIRSTWORD]
                        found = True
                        break
# needs an else here? if we do an iterator it would be ++

        file.close();

        if not found:
                return NOTFOUND
        else:
                return translatedWord;
	
        
def main():
	form=cgi.FieldStorage()
	hadError=False

#error handling
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

#if there was an error then we display the problems
	if hadError:
		translatedWord=NOVAL
		showTranslation(originLang, transLang, theWord, translatedWord)
	else:
#otherwise, find the translated word using translate and display that
#		translationArray = store()
		translatedWord = translate(originLang, transLang, theWord)
		showTranslation(originLang, transLang, theWord, translatedWord)

if __name__=="__main__":main()
