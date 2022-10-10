def __gcd(a, b):
 
    # Everything divides 0
    if (a == 0 or b == 0): return 0
     
    # base case
    if (a == b): return a
     
    # a is greater
    if (a > b):
        return __gcd(a - b, b)
             
    return __gcd(a, b - a)
 
# Function to check and print if
# two numbers are co-prime or not
def coprime(a, b):
     
    if ( __gcd(a, b) == 1):
        print("Co-Prime")
    else:
        print("Not Co-Prime")    
 
# Driver code
a = 5; b = 6
coprime(a, b)
 
a = 8; b = 16
coprime(a, b)
