from nltk.stem.wordnet import WordNetLemmatizer
import enchant
dir = 'c:/Users/michal/My Documents/Programowanie/'

lmtzr = WordNetLemmatizer()
lmtzr.lemmatize('heated')
def retListOfWords(words):
	'''
	Otrzmuje plik txt
	Zwraca liste slow z pliku txt
	'''
	listOfWords = []
	enW = ''
	i = 0
	letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY'"
	while i < len(words):
		if words[i] in letters:
			while words[i] in letters:
				enW += words[i]
				if i < (len(words) - 1):
					i += 1
				else:
					break
			enW = enW.lower()
			#if not enW in listOfWords:
			listOfWords.append(enW)
			enW = ''
		i += 1
	print 'Zakonczono wczytywanie slow...'
	return listOfWords

def saveListOfWordsToFile(list):
	f = open(dir + 'text.txt', 'w')
	for word in list:
		f.write(word + '\n')
	print 'Zakonczono wczytywanie slow...'
	f.close()

def checkIfWordExist(word):
	d = enchant.Dict("en_UK")
	e = enchant.Dict("en_US")
	if d.check(word) == False and e.check(word) == False:
		return False
	else:
		return True

def getFlashcardsFromText(fileName):
	from functionsToGetWordsDefinitions import getFullDef
	import codecs
	f = open(fileName, 'r')
	words = f.read()
	f.close()
	dec = raw_input('Czy zapisac liste slow do pliku text.txt? y lub n?')
	listOfWords = retListOfWords(words)
	if dec == 'y':
		saveListOfWordsToFile(listOfWords)
	dec = raw_input('Czy tlumaczyc slowa i zapisac do pliku talia.txt? y lub n?')
	if dec == 'y':
		f = codecs.open(dir + 'talia.txt', 'wb', 'utf-8')
		for i in range(len(listOfWords)):
			if checkIfWordExist(listOfWords[i]) == True:
				f.write(getFullDef(listOfWords[i]))
		f.close()
	print 'Zakonczono prace programu.'