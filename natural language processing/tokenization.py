from nltk.tokenize import word_tokenize
import nltk

#Tokenization in NLP (Natural Language Processing) syntax is the process
#of breaking down a text or sentence into individual units called tokens.
#Tokens are nothin but sequence of characters in some particular document
#that are grouped together as a useful semantic unit """

# Using NLTK

# nltk is a popular python package for natural language processing for text analysis
#Installation:
# windows - pip3 install nltk
# Mac/Linux - sudo pip install -U nltk
#sudo pip3 install -U nltk


text = "Natural Language Processing is a fascinating field."
tokens = word_tokenize(text)
print("Tokens:", tokens)


# REFERENCE:
# https://en.wikipedia.org/wiki/Lexical_analysis#Tokenization