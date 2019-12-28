
"""
Function using divide and conquer to calculate a^b.
It only works for integer a,b.
"""
def power(a,b):
    if b == 0:
        return 1
    elif ( (b%2) == 0 ):
        return (power(a,int(b/2)) * power(a,int(b/2)))
    else:
        return (a * power(a,int(b/2)) * power(a,int(b/2)))

if __name__ == "__main__":
    print(power(2,1000000))
