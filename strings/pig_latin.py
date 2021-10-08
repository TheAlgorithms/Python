"""
Problem Explanation:
A word in english is provided, you have to convert it into pig latin. 

Pig Latin takes the word and checks if the word begins with a vowel, if it does then just add "way" at the end of the string. Else take the consonant (or the consonant cluster) move it to the end of the word and suffix an "ay". 
"""

def translatePigLatin(str, charPos = 0) -> str:
    """
    This function will convert english word to pig latin word
    """
    arr = ['a', 'e', 'i', 'o', 'u']
    if(str[0] in arr):
        if(charPos == 0):
            return str + 'way'
        return str + "ay"
    else:
        if(charPos == len(str)):
            return str + 'ay'
        translatePigLatin(str[1:] + str[0], charPos + 1)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
