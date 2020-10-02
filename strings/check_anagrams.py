"""
wiki: https://en.wikipedia.org/wiki/Anagram
"""


def check_anagrams(first_str: str, second_str: str) -> bool:
    """
    Two strings are anagrams if they are made of the same letters
    arranged differently (ignoring the case).
    >>> check_anagrams('Silent', 'Listen')
    True
    >>> check_anagrams('This is a string', 'Is this a string')
    True
    >>> check_anagrams('This is    a      string', 'Is     this a string')
    True
    >>> check_anagrams('There', 'Their')
    False
    """
    return (
        "".join(sorted(first_str.lower())).strip()
        == "".join(sorted(second_str.lower())).strip()
    )

def checkAnagramsAlternate(first_str: str, second_str: str) -> bool:
    '''
    Strategy is to:
    (a) first check whether the length of both of the srings are same. If not, they can never be anagrams.
    (b) second check to make is whether all the characters in both the strings occur the same number of times
    
    Case 1: SILENT and LIST
    >>> not anagrams because (a) failed
    Case 2: SILENT and LISTED
    >>> not anagrams because (b) failed
    Case 3: SILENT and LISTEN 
    >>> anagrams because both (a) and (b) passed
    
    We will be using a hashmap to keep track of the number of letters of each type
    '''
    if len(first_str)!=len(second_str):
        return False
    letterCount=dict()
    #traversing through first string and storing the count of different variables
    for letter in first_str:
        if letter not in letterCount:
            letterCount[letter]=1
        else:
            letterCount[letter]+=1
    #traversing through second string and checking whether the letters and letter counts match
    for letter in second_str:
        if letter not in letterCount:
            return False
        else:
            letterCount[letter]-=1
    #traversing through the hashmap to check if all the entries have a value=0
    for entry in letterCount:
        if letterCount[entry]!=0:
            return False
        else:
            continue
    return True

if __name__ == "__main__":
    from doctest import testmod

    testmod()
    input_A = input("Enter the first string ").strip()
    input_B = input("Enter the second string ").strip()

    status1 = check_anagrams(input_A, input_B)
    print(f"{input_A} and {input_B} are {'' if status else 'not '}anagrams.")
    status2 = checkAnagramsAlternate(input_A,input_B)
    print(status2)
