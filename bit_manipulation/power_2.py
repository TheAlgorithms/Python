# Question : determine whether given number is power of 2

# logic : every no. of the form 2^i has bit represetntaion of the form : 
# 2 -> 10         1->01
# 4 -> 100        3->011
# 8 -> 1000       7->0111
# 16 -> 10000     15->01111
# 32 -> 100000    31->011111
# ... and so on

# Thus there is a pattern here, ever predecessor of power of 2 has all 0 bits flipped and so as 1 bit itself

# Complexity : using bit manipulation it can be done in O(1) time


def is_power(n):
    if n==0:
        return 'not power of two'
    if n & (n-1) == 0 :
        return 'power of 2'
    return 'not power of 2'


if __name__ == "__main__":
    input_number = int(input('enter the number : '))
    print(is_power(input_number))
