"""
Problem Explanation:
A word in english is provided, you have to convert it into pig latin. 

Pig Latin takes the word and checks if the word begins with a vowel, if it does then just add "way" at the end of the string. Else take the consonant (or the consonant cluster) move it to the end of the word and suffix an "ay". 
"""

def translate_pig_latin(str: str, char_pos: int = 0) -> str:
    """
    This function will convert english word to pig latin word
    """
    arr = ['a', 'e', 'i', 'o', 'u']
    if(str[0] in arr):
        if(char_pos == 0):
            return str + 'way'
        return str + "ay"
    else:
        if(char_pos == len(str)):
            return str + 'ay'
        translate_pig_latin(str[1:] + str[0], char_pos + 1)


if __name__ == "__main__":
    from doctest import testmod

    translate_pig_latin("owl")
    testmod()
