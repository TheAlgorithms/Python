from __future__ import annotations

import collections
import pprint
from pathlib import Path

# Function to sort the characters in a given word
def signature(word: str) -> str:
    """
    Sorts the characters in the given word.
    
    >>> signature("test")
    'estt'
    >>> signature("this is a test")
    '   aehiisssttt'
    >>> signature("finaltest")
    'aefilnstt'
    """
    return "".join(sorted(word))

# Function to find anagrams of a given word
def anagram(my_word: str) -> list[str]:
    """
    Finds all the anagrams of the given word.
    
    >>> anagram('test')
    ['sett', 'stet', 'test']
    >>> anagram('this is a test')
    []
    >>> anagram('final')
    ['final']
    """
    return word_by_signature[signature(my_word)]

# Read the word list from the file
data: str = Path(__file__).parent.joinpath("words.txt").read_text(encoding="utf-8")
# Sort and remove duplicates
word_list = sorted({word.strip().lower() for word in data.splitlines()})

# Create a dictionary to hold the anagrams
word_by_signature = collections.defaultdict(list)

# Populate the dictionary
for word in word_list:
    word_by_signature[signature(word)].append(word)

# Main execution
if __name__ == "__main__":
    # Create a dictionary of all anagrams where the word has more than one anagram
    all_anagrams = {word: anagram(word) for word in word_list if len(anagram(word)) > 1}
    
    # Save the anagrams to a text file
    with open("anagrams.txt", "w") as file:
        file.write("all_anagrams = \n")
        file.write(pprint.pformat(all_anagrams))

