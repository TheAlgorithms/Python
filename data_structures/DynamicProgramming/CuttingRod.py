'''
Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example, if length of the rod is 8 and the values of different pieces are given as following, then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)


length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 1   5   8   9  10  17  17  20
'''

def cutRod(price, n): 
    val = [0]*(n+1) 
    val[0] = 0
  
    
    for i in range(1, n+1): 
        max_val = INT_MIN 
        for j in range(i): 
             max_val = max(max_val, price[j] + val[i-j-1]) 
        val[i] = max_val 
  
    return val[n] 
