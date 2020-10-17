k = 50
def E_116(i, k): 
    ways = [1] * i + [0] * (k-i+1) 
    for j in range(i, k+1): 
        ways[j] += ways[j - 1] + ways[j - i] 
    return ways[k] - 1
  
print("Number of black tiles =", k, "units") 
print("Number of ways to fill:", E_116(2, k) + E_116(3, k) + E_116(4, k)) 

#This will give us the answer : 20492570929
