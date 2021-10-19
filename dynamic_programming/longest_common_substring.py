# Dynamic Programming (DP) : Algorithm for finding Longest Common Substring in python

# Name: Atharva Patil
# Github Profile link:  https://github.com/atharvapatil123 
 
def longest_common_substring(X, Y, n, m):

    # res variable is used to store the result: Maximum length of common subtring
    res = 0

    # Create a table to store Longest Common suffixes 
    # Initially, all cells are initialized with -1
    table = [[-1 for k in range(m+1)] for l in range(n+1)]

    # Making first row and column entirely 0
    for i in range(n+1):
        for j in range(m+1):
            if(i==0 or j==0): 
                table[i][j]=0
            

    for i in range(1,n+1):
        for j in range(1,m+1):
            if(X[i-1]==Y[j-1]):
                table[i][j] = 1 + table[i-1][j-1]
                res = max(res, table[i][j]) 
            else:
                table[i][j] = 0;

    return res
 
 
# Driver Code
X = "abcde"
Y = "abfcde"
 
n = len(X)
m = len(Y)

print('\nLength of Longest Common Substring is', longest_common_substring(X, Y, n, m))
# 3 is returned