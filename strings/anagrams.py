from __future__ import annotations

import collections
import pprint
from pathlib import Path


def signature(word: str) -> str:
    """Sorts character of a given word 
    >>> signature("test")
    'estt'
    >>> signature("this is a test")
    '   aehiisssttt'
    >>> signature("finaltest")
    'aefilnstt'
    """
    return "".join(sorted(word))


def anagram(my_word: str) -> list[str]:
    """Finds all the anagrams of a given word 
    >>> anagram('test')
    ['sett', 'stet', 'test']
    >>> anagram('this is a test')
    []
    >>> anagram('final')
    ['final']
    """
    return word_by_signature[signature(my_word)]

# read the word list from the file
data: str = Path(__file__).parent.joinpath("words.txt").read_text(encoding="utf-8")
# sort and remove duplicates
word_list = sorted({word.strip().lower() for word in data.splitlines()})

#create a dict to store anagrams
word_by_signature = collections.defaultdict(list)

# popualation of the dictionary
for word in word_list:
    word_by_signature[signature(word)].append(word)

# main code excecution
if __name__ == "__main__":
    #create dic to store where more than one angaram are present
    all_anagrams = {word: anagram(word) for word in word_list if len(anagram(word)) > 1}
    #saving the anagrams to txt file 
    with open("anagrams.txt", "w") as file:
        file.write("all_anagrams = \n ")
        file.write(pprint.pformat(all_anagrams))
