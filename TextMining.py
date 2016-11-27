#!usr/bin/python

import re
import nltk
from nltk.corpus import stopwords 
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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