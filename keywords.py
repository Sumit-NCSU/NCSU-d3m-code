from textblob import TextBlob

data=open("///home/sumit/nltk/data/data.txt").read()

bunch=TextBlob(data)

find_good=bunch.sentences

key_words=['disease','rare','Rare','Disease','Child','Children','child','children']

for sentence in find_good:
	if(any(map(lambda word: word in sentence, key_words))):
		print(sentence)
