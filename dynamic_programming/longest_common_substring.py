"""
Dynamic Programming (DP) : Algorithm for finding Longest Common Substring in python

LONGEST COMMON SUBSTRING PROBLEM:  Given two strings, find the length of longest substring
present in both of them.  A substring is a sequence that appears in the same relative
order and is necessarily continuous.

Name: Atharva Patil
Github Profile link:  https://github.com/atharvapatil123 
"""
"""
Parameters

string1: 1st string
string2: 2nd string
n: length of string1 
m: length of string2
"""

from typing import Tuple

def longest_common_substring(
    string1: str, string2: str, len_of_string1: int, len_of_string2: int
) -> Tuple[str, int]: 


    """
    >>> longest_common_substring("coding", "code", 6, 4)
    (3, 'cod')

    >>> longest_common_substring("fishing", "fighting", 7, 8)
    (3, 'ing')

    >>> longest_common_substring("health", "wealth", 6, 6)
    (5, 'ealth')

    >>> longest_common_substring("no", "yes", 2, 3)
    (0, '')

    """

    res = (
        0  # res variable is used to store the result: Maximum length of common subtring
    )
    string = ""  # string is used to store the longest common substring

    """
    Create a table to store Longest Common suffixes 
    Initially, all cells are initialized with -1
    """
    table = [[-1 for i in range(len_of_string2 + 1)] for j in range(len_of_string1 + 1)]

    # Making first row and column entirely 0
    for i in range(len_of_string1 + 1):
        for j in range(len_of_string2 + 1):
            if i == 0 or j == 0: 
                table[i][j] = 0

            
    # To store the indices of the table with maximum value
    k = 0
    l = 0

    for i in range(1, len_of_string1 + 1):
        for j in range(1, len_of_string2 + 1):
            if(string1[i - 1] == string2[j - 1]):
                table[i][j] = 1 + table[i - 1][j - 1]
                if(table[i][j] > res):
                    res = table[i][j]
                    k = i  # stores row value with maximum value in table
                    l = j  # stores column value with maximum value in table
            else:
                table[i][j] = 0

    i = k
    j = l
    while i > 0 and j > 0:
        if string1[i - 1] == string2[j - 1]:
            string = string + string1[i - 1]  # Use to store longest common substring
        i = i - 1
        j = j - 1

    string = "".join(reversed(string))

    return res, string


# Driver Code

if __name__ == "__main__":

    import doctest

    doctest.testmod()

    string1 = "abcde"
    string2 = "abfcde"
    
    """
    string1 and string2 represent 2 strings whose longest common substring is to be found
    That is here, string1=abcde and string2=abfcde
    Thus, longest common substring possible is cde
    """

    """
    len_of_string1 represent length of string string1
    len_of_string1 represent length of string string2
    """
    len_of_string1 = len(string1)
    len_of_string2 = len(string2) 

    
    length, string = longest_common_substring(
        string1, string2, len_of_string1, len_of_string2
    )
    """
    The function returns 2 things
    1. length: This is the length of longest common substring of the 2 strings
    2. string: This is the actual string (longest common substring)
    """

    """
    If length=0, then no common substring is present between the two strings
    """
    if length == 0:
        print("\nThere is no longest common substring possible")

    else:        
        print("\nLength of Longest Common Substring is", length)
        print("Longest Common Substring is", string)
    
    # doctest.testmod(name ='longest_common_substring', verbose = True)


