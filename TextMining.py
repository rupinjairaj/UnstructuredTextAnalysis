#!usr/bin/python

import re
import nltk
from nltk.corpus import stopwords 
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer

# Dictionary to store the data; source is the key
data = {}

data['bbc'] = open('./Data/madmax_review/bbc.txt', 'r').read()
data['forbes'] = open('./Data/madmax_review/forbes.txt', 'r').read()
data['guardian'] = open('./Data/madmax_review/guardian.txt', 'r').read()
data['moviepilot'] = open('./Data/madmax_review/moviepilot.txt', 'r').read()

# Converting the text to lower case

print "Processing text to lower case..."

for k in data.keys():
	data[k] = data[k].lower()

print data['bbc'][:800]

# Removing punctuation

print "Processing to remove punctuation..."

for k in data.keys():
	data[k] = re.sub(r'[-./?!,":;()\']', ' ', data[k])

print data['bbc'][:800]

# Removing numbers from the list

print "Processing to remove numbers..."

for k in data.keys():
	data[k] = re.sub('[-|0-9]', ' ', data[k])

print data['bbc'][:800]

# Removing stopwords

print "Processing to remove stop words..."

for k in data.keys():
	data[k] = data[k].split()

stopwords_list = stopwords.words('english')
stopwords_list = stopwords_list + ['mad', 'max', 'film', 'fury', 'miller', 'road']

for k in data.keys():
	data[k] = [ w for w in data[k] if not w in stopwords_list ]

print data['bbc'][:80]

# Creating a wordcloud
## wordcloud for BBC
wordcloud = WordCloud(width = 1000, height = 500).generate(' '.join(data['bbc']))
plt.figure(figsize = (15, 8))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

## wordcloud for Forbes
wordcloud = WordCloud(width = 1000, height = 500).generate(' '.join(data['forbes']))
plt.figure(figsize = (15, 8))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

## wordcloud for Guardian
wordcloud = WordCloud(width = 1000, height = 500).generate(' '.join(data['guardian']))
plt.figure(figsize = (15, 8))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

## wordcloud for Moviepilot
wordcloud = WordCloud(width = 1000, height = 500).generate(' '.join(data['moviepilot']))
plt.figure(figsize = (15, 8))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# Word and Sentence tokenize

## Loading the forbes data
print "Processing for word tokenization..."
data = open('./Data/madmax_review/forbes.txt', 'r').read()
word_data = nltk.word_tokenize(data)
print word_data[:15] 

## sentence tokenization
print "Processing for sentence tokenization..."
print sent_tokenize(data)[:5]

# Parts of speech tagging

print "Processing data to tag parts of speech..."
pos_word_data = nltk.pos_tag(word_data)
print pos_word_data

# Stemming and Lemmatization

## Stemming with Porter Stemmer
print "Stemming with Porter Stemmer..."
porter_stemmer = PorterStemmer()
for w in word_data[:20]:
	print "Actual: %s Stem: %s" % (w, porter_stemmer.stem(w))

## Stemming with Lancaster Stemmer
print "Stemming with Porter Stemmer..."
lancaster_stemmer = LancasterStemmer()
for w in word_data[:20]:
	print "Actual: %s Stem: %s" % (w, lancaster_stemmer.stem(w))

## Stemming with Snowball Algorithm
print "Stemming with Snowball Stemmer..."
snowball_stemmer = SnowballStemmer("english")
for w in word_data[:20]:
	print "Actual: %s Stem: %s" % (w, snowball_stemmer.stem(w))

## Lemmatization with WordNet
wordnet_lemmatizer = WordNetLemmatizer()
for w in word_data[:20]:
	print "Actual: %s Stem: %s" % (w, wordnet_lemmatizer.stem(w))	

