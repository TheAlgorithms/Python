"""
Author  : Anubhav Sharma

This is a pure Python implementation of Dynamic Programming solution to the longest
palindrome substring of a given string.
I use Manacher Algorithm which is amazing algorithm and find solution in linear time complexity.

The problem is  :
Given a string, to find the longest palindrome sub-string in that given string and
return it.
Example: aabbabbaababa as input will return
         aabbabbaa as output
"""
def manacher_algo_lps(s,n):
    """
    PARAMETER
    --------------
    s = string
    n = string_len (int)

    manacher Algorithm is the fastest technique to find the longest palindrome substring in any given string.

    RETURN
    ---------------
    Longest Palindrome String(String)
    """
    # variables to use
    p = [0] * n
    c = 0
    r = 0
    maxlen = 0

    # Main Algorithm
    for i in range(n):
        mirror = 2*c-i # Finding the Mirror(i.e. Pivort to break) of the string
        if i < r:
            p[i] = (r - i) if (r - i) < p[mirror] else p[mirror]
        a = i + (1 + p[i])
        b = i - (1 + p[i])

        # Attempt to expand palindrome centered at currentRightPosition i 
        # Here for odd positions, we compare characters and 
        # if match then increment LPS Length by ONE 
        # If even position, we just increment LPS by ONE without 
        # any character comparison
        while a<n and b>=0 and s[a] == s[b]:
            p[i] += 1
            a += 1
            b -= 1
        if (i + p[i]) > r:
            c = i
            r = i + p[i]
            if p[i] > maxlen:               # Track maxLPSLength
                maxlen = p[i]
    i = p.index(maxlen)
    return s[i-maxlen:maxlen+i][1::2]

def longest_palindrome(s: str) -> str:
    s = '#'.join(s)
    s = '#'+s+'#'

    # Calling Manacher Algorithm
    return manacher_algo_lps(s,len(s))

def main():

    # Input to enter
    input_string = "abbbacdcaacdca"

    # Calling the longest palindrome algorithm
    s = longest_palindrome(input_string)
    print("LPS Using Manacher Algorithm {}".format(s))

# Calling Main Function
if __name__ == "__main__":

    main()

    import doctest
    doctest.testmod()

