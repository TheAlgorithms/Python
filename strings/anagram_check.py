"""
== Anagram Check ==
An anagarm is a word/ phrase that can be formed by rearranging
the characters of another word/ phrase, typically using each
character only once.
for example, firstWord = listen, secondWord = silent
return value will be True.
https://en.wikipedia.org/wiki/Anagram
"""


def anagram(firstWord: str, secondWord: str) -> bool:
    """
    >>> anagram(listen, silent)
    True
    >>> anagram(rat, bat)
    False
    >>> anagram(tool, loot)
    True
    """

    flag = 0
    for ele in firstWord:
        if ele in secondWord:
            flag = 1
            continue
        else:
            flag = 0
            break
    return True if (flag) else False


if __name__ == "__main__":
    firstWord = input("Enter the first word: ").strip()
    secondWord = input("Enter the second word: ").strip()
    if anagram(firstWord, secondWord):
        print(f"{firstWord} and {secondWord} are Anagrams.")
    else:
        print(f"{firstWord} and {secondWord} are not Anagrams.")
