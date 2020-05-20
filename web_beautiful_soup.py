import bs4 as bs
import urllib.request
from nltk.tokenize import sent_tokenize, word_tokenize


source = urllib.request.urlopen('http://ptrckprry.com/course/ssd/data/negative-words.txt').read()

soup = bs.BeautifulSoup(source, 'lxml')
nav = soup.nav


def lag_liste(kilde):

	words = word_tokenize(soup.text)
	ny_liste = []

	for line in words:

		ny_liste.append(line)
		
		if len(ny_liste) == len(words):
			print(ny_liste)



lag_liste(soup)