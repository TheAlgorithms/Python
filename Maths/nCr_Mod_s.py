#python program to calculate nCr%s
#where 's' is a prime number greater than 'n'

#import necessary functions
from functools import reduce
import operator as op

# Function to calculate nCr
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer//denom

# Driver code
if __name__ == '__main__':
    n = 1000
    r = 800
    s = pow(10,9) + 7
    
    # nC0 = 1
    if r == 0 and n > r:
        ans = 1
    elif n > r:
        ans = ncr(n,r)
        ans = ans % s
    elif n == r:
        ans = 1  # nCn = 1
    else:    
        ans = 0  # control reaches here only when n < r (----invalid case----) O/P = 0
    
    #print result    
    print(int(ans))    
