# Developed by Tuan H. on 18/1/20

"""
Counting word in a sentence using dictionary comprehension
"""
from collections import defaultdict

def word_occurence(sentence: str) -> dict:
    """
    >>> from collections import Counter
    >>> all(word_occurence(s) == Counter(s.split(' ')) for s in
    ...     ("a b a b c a", "I love to love Python ❤️ 💕 ❤️", "", " ; ;"))
    True
    """
    occurence_count = defaultdict(int)
    words = sentence.split(' ')
    unique_words = list(set(words))
    # Creating a dictionary containing count of each word
    occurence_count = {w:words.count(w) for w in unique_words}
    return occurence_count


if __name__ == "__main__":
    input_sentence = input('Input: ')
    for word, count in word_occurence(input_sentence).items():
        print(f"{word}: {count}")
