# UnstructuredTextAnalysis

## Part 1 - Preprocessing the data
### Steps involved
* Removing punctuation
* Removing numbers
* Converting text to lower case
* Removing stop words

**NOTE**
> download the 'stopwords' package via nltk.download()

## Part 2 - WordCloud on the dataset
### Steps involved
* Installing the WordCloud python toolkit | checkout: [https://github.com/amueller/word_cloud]
* Plotting the WordClouds for the 4 data sets used

## Part 3 - Word and sentence tokenization
### Steps involved
* Word tokenization is done with 'word_tokenize' module in the nltk package
* Sentence tokenization is done with 'sent_tokenize' module in the nltk.tokenize package

**NOTE**
> download the 'punkt' package via nltk.download()

## Part 4 - Tagging parts of speech
### Steps involved
* This part is achieved using the pos_tag() function in the nltk package

## Part 5 - Stemming and lemmatization
### Steps involved
* This step was done using the 'pos_tag' function in the nltk module
* Stemming tried with 3 different algorithms- Snowball, Porter and Lancaster
* Lemmatization tried with WordNet 

**NOTE**
>download the 'averaged_perceptron_tagger' via nltk.download()
 
## Part 6 - Applying Stanford Named Entity Recognizer
### Steps involved