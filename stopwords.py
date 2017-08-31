import sys
import io
import nltk
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

data = open('D:\work\d3m\Aug24\Health Insurance and Laws\Company_Profiles_and_Directories_US_Law_Revi2017-08-24_13-48.TXT', encoding='utf-8').read()

stop_words = set(stopwords.words())
words = word_tokenize(data)
words_selected = []
for w in words:
	if w not in stop_words:
		words_selected.append(w)
	
print(words_selected)