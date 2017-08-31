import sys
import io
import nltk
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

data = open('D:\work\d3m\Aug24\Health Insurance and Laws\Company_Profiles_and_Directories_US_Law_Revi2017-08-24_13-48.TXT', encoding='utf-8').read()

words = word_tokenize(data)

spread=nltk.FreqDist(words)
spread.plot(50, cumulative=True)
for word, frequency in spread.most_common(100):
	print(u'{};{}'.format(word, frequency))
