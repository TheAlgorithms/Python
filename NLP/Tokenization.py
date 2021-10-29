# Import spaCy and load the language library
import spacy

nlp = spacy.load('en_core_web_sm')

# Create a string that includes opening and closing quotation marks
mystring = '"We\'re moving to L.A.!"'
print(mystring)

# Create a Doc object and explore tokens
doc = nlp(mystring)

for token in doc:
    print(token.text, end=' | ')

len(doc)
len(doc.vocab)

