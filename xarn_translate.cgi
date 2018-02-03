#!/usr/bin/python3
#Adrienne Corwin and Angela Vichitbandha
print("Content-type:text/html\n\n")

import cgi
import cgitb

cgitb.enable()

#constants to detect and print errors
NOTFOUND='unknown'
NOVAL='none'
MISSING='invalid'

#produces an HTML document to show user the results of their translation request
def showTranslation(a, b, c, d, e):
	print("<style> .found {color:green} .notfound {color:red} .proper{color:blue} .improper{color:red}</style>") #error styling
	print("<html><head><title>Translate</title></head><body>")

#if any of the fields/their values are missing print field and word invalid in red
#if the field have proper input, print them in blue
	if e:
		print("Could not do translation. Missing information in red.<br>")
	else:
		print("Here is your translation!<br>")

	if a==MISSING:
		print("<p><span class=\"improper\">Origin Language: ")
		print(MISSING)
		print("</span>")
	else:
		print("<p><span class=\"proper\">Origin Language: </span>")
		print("%s" % a)

	if b==MISSING:
		print("<p><span class=\"improper\">Requested Language: ")
		print(MISSING)
		print("</span>")
	else:
		print("<p><span class=\"proper\">Requested Language: </span>")
		print("%s" % b)

	if c==MISSING:
		print("<p><span class=\"improper\">Original Word: ")
		print(MISSING)
		print("</span>")
	else:
		print("<p><span class=\"proper\">Origin Word: </span>")
		print("%s" % c)

#if translation could not be done bc of missing info, print field and the word invalid in red
#if the translation could not be found in text file provided print unknown
#if translation is found print word in green
	if d==MISSING:
		print("<p><span class=\"improper\">Translation: </span>")
		print("<span class=\"notfound\">")
		print(MISSING)
		print("</span>")
		print("</p></body></html>")
	elif d == NOTFOUND:
		print("<p><span class=\"proper\">Translation: </span>")
		print("<span class=\"notfound\">")
		print("%s" % d)
		print("</span>")
		print("</p></body></html>")		
	else:
		print("<p><span class=\"proper\">Translation: </span>")
		print("<span class=\"found\">")
		print("%s" % d)
		print("</span>")
		print("</p></body></html>")

#looks for translation given information of inputs and returns translation if it is found
def translate(originLang, transLang, theWord):

#word to be returned
	translatedWord = ""

#constants for indexing the file's contents
	FIRSTLANG = 0
	FIRSTWORD = 1
	SECONDLANG = 2
	SECONDWORD = 3

#keeps track of whether a translation was found in the file
	found = False

	file = open("xarn_language.txt", "r")
#goes through file line by line, checking for matching terms
#ends if match is found or at end of file
	line = file.readline()
	while not found and line != '':
		line=line.rstrip()	
		entry = line.split(",")
		if theWord == entry[FIRSTWORD] and originLang == entry[FIRSTLANG] and transLang == entry[SECONDLANG]:
			translatedWord = entry[SECONDWORD]
			found = True
			break
		elif theWord == entry[SECONDWORD] and originLang == entry[SECONDLANG] and transLang == entry[FIRSTLANG]:
			translatedWord = entry[FIRSTWORD]
			found = True
			break
#if match was not found, go to next line
		else:
			line = file.readline()

	file.close();

	if not found:
		return NOTFOUND
	else:
		return translatedWord;
	
        
def main():
	form=cgi.FieldStorage()
#keeps track of whether there is a field/field value missing from user input
	hadError=False

#error handling if field/field value is missing
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
		translatedWord=MISSING
		showTranslation(originLang, transLang, theWord, translatedWord, hadError)
	else:
#otherwise, find the translated word using translate and display that
#		translationArray = store()
		translatedWord = translate(originLang, transLang, theWord)
		showTranslation(originLang, transLang, theWord, translatedWord, hadError)

if __name__=="__main__":main()
