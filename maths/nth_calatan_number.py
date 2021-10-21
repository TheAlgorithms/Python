
#program to find nth Catalan Number using dynamic programming.
"""
Catalan numbers are a sequence of natural numbers that occurs 
in many interesting counting problems like counting the number 
of expressions containing n pairs of parentheses which are 
correctly matched. 
For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).
for more info : https://en.wikipedia.org/wiki/Catalan_number
"""
def catalan(n):
    if (n == 0 or n == 1):
        return 1
  
    # Table to store results of subproblems
    catalan = [0 for i in range(n + 1)]
  
    # Initialize first two values in table
    catalan[0] = 1
    catalan[1] = 1
  
    # Fill entries in catalan[] using recursive formula
    for i in range(2, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] = catalan[i] + catalan[j] * catalan[i-j-1]
  
    # Return last entry
    return catalan[n]
  
# Driver code
for i in range (10):
    print (catalan(i))
