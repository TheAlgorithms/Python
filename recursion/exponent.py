'''
    Trying to find the exponent using Python.
'''

def exponentRecursion(a,b):
    if b==0:
        return 1
    tmp = exponentRecursion(a,b//2)
    y = tmp*tmp
    if b%2:
        y = y*a
    return y

if __name__ =="__main__":
    print(exponentRecursion(5,3))