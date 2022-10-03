def removeVowels(sentence: str) -> str:
    """
    This removeVowel function will remove all the vowels from a given sentence or a word
    >>> removeVowels('Hello world')
    'Hll wrld'
    >>> removeVowels('Programming is my passion')
    'Prgrmmng s my pssn'
    >>> removeVowels('I love coding 24 hours')
    ' lv cdng 24 hrs'
    >>> removeVowels('')
    ''
    """

    #List of all the vowels
    vow=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    #iterating over a list of vowels
    for vowel in vow:
        #replacing the vowel with blank
        sentence=sentence.replace(f"{vowel}", "")

    #returning a updated string
    return sentence

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    #passing a string to a function removeVowels and printing the result
    print(removeVowels('Welcome to HACKTOBERFEST 2022'))