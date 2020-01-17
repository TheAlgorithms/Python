# Developed by Tuan H. on 18/1/20

"""
Counting word in a sentence using dictionary comprehension
"""


def word_occurence(sentence: str) -> dict:
    occurence = {}
    words = sentence.split(' ')
    unique_words = list(set(words))
    
    # Creating a dictionary containing count of each word
    occurence = {w:words.count(w) for w in unique_words}
    
    return occurence


if __name__ == "__main__":
    input_sentence = input('Input: ')
    for word, count in word_occurence(input_sentence).items():
        print(f"{word}: {count}")
