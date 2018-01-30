//follows store.cgi

//strings from input
theWord = "teststring1";
originLang = "teststring2";
transLang = "teststring3";
translatedWord = "";

firstLangCol = 0;
firstWordCol = 1;
secondLangCol = 2;
secondWordCol = 3;

for checkRow in bigData:
    if theWord = checkRow[firstWordCol] and originLang = checkRow[firstLangCol] and transLang = checkRow[secondLangCol]:
        translatedWord = checkRow[secondWordCol];
        break;
    elif theWord = checkRow[secondWordCol] and originLang = checkRow[secondLangCol] and transLang = checkRow[firstLangCol]:
        translatedWord = checkRow[firstWordCol];
        break;

//I don't actually know what we're doing with the translated word yet
//also this does require us being allowed to use breaks. If we're not, I'll have to change to a while loop (bool to decide whether to stop, iterator to go through the array


