#!/usr/bin/python3
#Adrienne Corwin and Angela Vichitbandha
print("Content-type:text/html\n\n")

import cgi
import cgitb

cgitb.enable() #enable cgi traceback for debugging

#constants to detect and print errors
NOTFOUND='unknown'
NOVAL='none'
MISSING='invalid'

#produces an HTML document to show user the results of their translation request
def showTranslation(origin, requested, givenWord, transWord, errorBool):
	print("<style> .found {color:green} .notfound {color:red} .proper{color:blue} .improper{color:red}</style>") #error styling
	print("<html><head><title>Translate</title></head><body>")

#if any of the fields/their values are missing print field and word invalid in red
#if the field have proper input, print them in blue
	if errorBool:
		print("Could not do translation. Missing information in red.<br>")
	else:
		print("Here is your translation!<br>")

	if origin==MISSING:
		print("<p><span class=\"improper\">Origin Language: ")
		print(MISSING)
		print("</span>")
	else:
		print("<p><span class=\"proper\">Origin Language: </span>")
		print("%s" % origin)

	if requested==MISSING:
		print("<p><span class=\"improper\">Requested Language: ")
		print(MISSING)
		print("</span>")
	else:
		print("<p><span class=\"proper\">Requested Language: </span>")
		print("%s" % requested)

	if givenWord==MISSING:
		print("<p><span class=\"improper\">Original Word: ")
		print(MISSING)
		print("</span>")
	else:
		print("<p><span class=\"proper\">Origin Word: </span>")
		print("%s" % givenWord)

#if translation could not be done bc of missing info, print field and the word invalid in red
#if the translation could not be found in text file provided print unknown
#if translation is found print word in green
	if transWord==MISSING:
		print("<p><span class=\"improper\">Translation: </span>")
		print("<span class=\"notfound\">")
		print(MISSING)
		print("</span>")
		print("</p></body></html>")
	elif transWord == NOTFOUND:
		print("<p><span class=\"proper\">Translation: </span>")
		print("<span class=\"notfound\">")
		print("%s" % transWord)
		print("</span>")
		print("</p></body></html>")		
	else:
		print("<p><span class=\"proper\">Translation: </span>")
		print("<span class=\"found\">")
		print("%s" % transWord)
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
	line = file.readline()
	while not found and line != '': #until translation found or file ends
		line=line.rstrip() #remove nextline character at end of entry
		entry = line.split(",") #split line of file input into the languages and words
#               Since the file could have the given language as the first or second entry, must check both ways
#               if the entry matches (either way) set translatedWord as the translation and mark as found
		if theWord == entry[FIRSTWORD] and originLang == entry[FIRSTLANG] and transLang == entry[SECONDLANG]:
			translatedWord = entry[SECONDWORD]
			found = True
		elif theWord == entry[SECONDWORD] and originLang == entry[SECONDLANG] and transLang == entry[FIRSTLANG]:
			translatedWord = entry[FIRSTWORD]
			found = True
#if match was not found, get the next line
		else:
			line = file.readline()

	file.close();

	if not found:
		return NOTFOUND # return const val NOTFOUND if the translation was not available
	else:
		return translatedWord;
	
        
def main():
	form=cgi.FieldStorage()
#keeps track of whether there is a field/field value missing from user input
	hadError=False

#error handling, if field/field value is missing, set hadError as true and put const val MISSING as the value
#otherwise, set the value as the one given from the form (all lower case)
#should this value be stripped of any trailing whitespace in case?
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
		translatedWord = translate(originLang, transLang, theWord)
		showTranslation(originLang, transLang, theWord, translatedWord, hadError)

if __name__=="__main__":main()
