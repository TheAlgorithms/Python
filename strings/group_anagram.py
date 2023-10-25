"""
author: Aayush Soni
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of
a different word or phrase, typically using all the original letters exactly once.

Leetcode link: https://leetcode.com/problems/group-anagrams/description/
"""


def group_anagrams(words):
    """
    Group anagrams in a list of words.

    This function takes a list of words and groups them
    based on whether they are anagrams of each other.

    Examples:
    >>> group_anagrams(["cat", "dog", "tac", "god", "act"])
    {'act': ['cat', 'tac', 'act'], 'dgo': ['dog', 'god']}

    >>> group_anagrams(["listen", "silent", "hello", "world"])
    {'eilnst': ['listen', 'silent'], 'ehllo': ['hello'], 'dlorw': ['world']}
    """
    grouped_words = dict()

    # Put all anagram words together in a dictionary
    # where the key is the sorted word
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word not in grouped_words:
            grouped_words[sorted_word] = [word]
        else:
            grouped_words[sorted_word].append(word)

    return grouped_words


if __name__ == "__main__":
    arr = ["cat", "dog", "tac", "god", "act"]
    groups = group_anagrams(arr)

    # Sort the groups for consistent output
    sorted_groups = sorted(groups)

    for key in sorted_groups:
        group = groups[key]
        print(" ".join(group))

    import doctest

    doctest.testmod()
