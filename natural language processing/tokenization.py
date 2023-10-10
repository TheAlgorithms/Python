""" Tokenization in NLP (Natural Language Processing) syntax is the process
of breaking down a text or sentence into individual units called tokens.
Tokens are nothin but sequence of characters in some particular document 
that are grouped together as a useful semantic unit """

# Using NLTK

# nltk is a popular python package for natural language processing for text analysis
"""
Installation:
windows - pip3 install nltk
Mac/Linux - sudo pip install -U nltk
sudo pip3 install -U nltk
"""
from nltk.tokenize import word_tokenize
import nltk 
nltk.download('punkt')
from spacy.lang.en import English


text = "Natural Language Processing is a fascinating field."
tokens = word_tokenize(text)
print("Tokens using NLTK:",tokens)

#Using Spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = English()

text = """Here we've handpicked some of the interesting deals on the best camera smartphones under
 Rs. 20,000. This ranges from OnePlus Nord CE 3 Lite 5G to Redmi Note 12 5G. Shoppers are advised 
 to compare prices with Flipkart's ongoing Big Billion Days Sale 2023 before placing the order."""

#  "nlp" Object is used to create documents with linguistic annotations.
my_doc = nlp(text)

# Create list of word tokens
token_list = []
for token in my_doc:
    token_list.append(token.text)
print("Tokens using Spacy:",token_list)