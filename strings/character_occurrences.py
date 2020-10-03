
def char_occurrence(word:str)->dict:
    """
    The function char_occurrence will calculate the frequency of each letter in the given string
    >>> Enter string:hello
        h: 1
        e: 1
        l: 2
        o: 1
    >>> Enter string:hello world
        h: 1
        e: 1
        l: 3
        o: 2
         : 1
        w: 1
        r: 1
        d: 1
        > 
    """
    # Creating a dictionary containing count of each letter
    # 'f' indicates count or frequency of each letter
    # 'word' indicates the string input by the user
    f = defaultdict(int)
    for letter in word:
        f[letter] += 1
    return f

if __name__ == "__main__":
    word=input("Enter string:")
    from collections import defaultdict
    for letter, frequency in char_occurrence(word).items():
        print(f"{letter}: {frequency}")
