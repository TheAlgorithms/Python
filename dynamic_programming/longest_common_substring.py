"""
Dynamic Programming (DP) : Algorithm for finding Longest Common Substring in python

LONGEST COMMON SUBSTRING PROBLEM:  Given two strings, find the length of longest substring
present in both of them.  A substring is a sequence that appears in the same relative
order and is necessarily continuous.

Name: Atharva Patil
Github Profile link:  https://github.com/atharvapatil123 
"""
 
def longest_common_substring(X: str, Y: str, n: int, m: int):
    """
    Parameters

    X: 1st string
    Y: 2nd string
    n: length of X string
    m: length of Y string

    Returns

    The funtion longest_common_substring returns 2 things:
    1. length: This is the length of longest common substring of the 2 strings
    2. string: This is the actual string (longest common substring)


    longest_common_substring("coding", "code")
    length = 3, string = 'cod')

    longest_common_substring("fishing", "fighting")
    length = 3, string = 'ing')

    longest_common_substring("health", "wealth")
    length = 5, string = 'ealth'

    longest_common_substring("no", "yes")
    length = 0, string = none
    """

    res = 0 # res variable is used to store the result: Maximum length of common subtring
    string="" # string is used to store the longest common substring

    """
    Create a table to store Longest Common suffixes 
    Initially, all cells are initialized with -1
    """
    table = [[-1 for i in range(m+1)] for j in range(n+1)]

    # Making first row and column entirely 0
    for i in range(n+1):
        for j in range(m+1):
            if(i==0 or j==0): 
                table[i][j]=0

            
    # To store the indices of the table with maximum value
    k=0
    l=0

    for i in range(1,n+1):
        for j in range(1,m+1):
            if(X[i-1]==Y[j-1]):
                table[i][j] = 1 + table[i-1][j-1]
                if(table[i][j]>res):
                    res = table[i][j]
                    k=i # stores row value with maximum value in table
                    l=j # stores column value with maximum value in table
            else:
                table[i][j] = 0;

    i=k
    j=l
    while(i>0 and j>0):
        if(X[i-1]==Y[j-1]):
            string = string+X[i-1] # Use to store longest common substring
        i=i-1
        j=j-1

    string = "".join(reversed(string))

    return res, string
 
 
# Driver Code

if __name__ == "__main__":
    X = "abcde"
    Y = "abfcde"
    
    """
    X and Y represent 2 strings whose longest common substring is to be found
    That is here, X=abcde and Y=abfcde
    Thus, longest common substring possible is cde
    """

    """
    n represent length of string X
    m represent length of string Y
    """
    n = len(X)
    m = len(Y) 

    
    length, string = longest_common_substring(X, Y, n, m)
    """
    The function returns 2 things
    1. length: This is the length of longest common substring of the 2 strings
    2. string: This is the actual string (longest common substring)
    """

    """
    If length=0, then no common substring is present between the two strings
    """
    if(length==0):
        print('\nThere is no longest common substring possible')

    else:        
        print('\nLength of Longest Common Substring is', length)
        print('Longest Common Substring is', string)

    import doctest

    doctest.testmod()
