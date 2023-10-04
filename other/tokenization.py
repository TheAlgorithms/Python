# Tokenization: Splitting text into words or sentences.
# https://www.tutorialspoint.com/natural_language_processing/natural_language_processing_python.htm
import nltk

nltk.download("punkt")
from nltk.tokenize import word_tokenize, sent_tokenize

text = "NLTK is a leading platform for building Python programs to work with human language data."
words = word_tokenize(text)
sentences = sent_tokenize(text)
print(words)
print(sentences)
