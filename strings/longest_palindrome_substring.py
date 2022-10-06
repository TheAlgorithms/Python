"""
Python solution for finding longest palindrome substring
"""

def printSubStr(str : str, low : int, high : int) -> None:
    """
    Inputs:
    str: String value representing input string
    low: Integer value representing starting index of substring
    high: Integer value representing ending index of substring

    return Value: None

    This method just prints the substring
    """
    for i in range(low, high+1):
        print(str[i], end='')

def longestPalSubStr(str : str) -> int:
    """
    Inputs:
    str: String value representing the input string

    Outputs:
    return Value: maxLen (storing the length of longest palindrome substring)
    """
    n = len(str)
    maxLen = 1
    start = 0

    for i in range(n):
        for j in range(i, n):
            flag = 1
            for k in range(0, ((j-i)//2)+1):
                if str[i+k] != str[j-k]:
                    flag = 0
            if flag != 0 and (j-i+1) > maxLen:
                start = i
                maxLen = j-i+1
    
    print("Longest Palindrome Substring:", end='')
    printSubStr(str, start, start+maxLen-1)
    return maxLen

"""
Driver Code
"""

if __name__ == '__main__':
    str = input()
    print("\nLength =", longestPalSubStr(str))