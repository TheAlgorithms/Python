"""
LPS Problem Statement: Given a sequence, find the length of the longest palindromic subsequence in it.
Example:"anamana"(length-7),is the longest palindromic subsequences of "abnamancdhfga".
"""
 
def lps(str): 
    n = len(str) 
  
    # Create a table to store results of subproblems 
    L = [[0 for x in range(n)] for x in range(n)] 
  
    # Strings of length 1 are palindrome of length 1 
    for i in range(n): 
        L[i][i] = 1
  
    # Build the table. Note that the lower diagonal values of table are useless and not filled in the process.  
    # cl is length of substring 
    for cl in range(2, n + 1): 
        for i in range(n-cl + 1): 
            j = i + cl-1
            if str[i] == str[j] and cl == 2: 
                L[i][j] = 2
            elif str[i] == str[j]: 
                L[i][j] = L[i + 1][j-1] + 2
            else: 
                L[i][j] = max(L[i][j-1], L[i + 1][j]); 
  
    return L[0][n-1] 
  
# Driver program to test above functions 
if __name__ == "__main__":
    seq = "abnamancdhfga"
    n = len(seq) 
    print("The length of the LPS is " + str(lps(seq))) 
    import doctest

    doctest.testmod()