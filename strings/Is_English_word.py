import nltk
from nltk.corpus import words

# Download the words corpus
# Get the set of English words once
english_words = set(words.words())

def is_english_word(word):
    return word.lower() in english_words

while True:
    # Input 
    input_word = input("Enter a word (or type 'exit' to quit): ")
    if input_word.lower() == 'exit':
        break
    if is_english_word(input_word):
        print(f"{input_word} is an English word.")
    else:
        print(f"{input_word} is not an English word.")
