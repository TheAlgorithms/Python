#Factorial of a number using memoization
result=[-1]*10
result[0]=result[1]=1
def factorial(num):
    """
    >>> factorial(7)
    5040
    >>> factorial(-1)
    'Number should not be negative.'
    >>> [factorial(i) for i in range(5)]
    [1, 1, 2, 6, 24]
    """
    
    if num<0:
        return "Number should not be negative."
    if result[num]!=-1:
        return result[num]
    else:
        result[num]=num*factorial(num-1)
        #uncomment the following to see how recalculations are avoided
        #print(result)
        return result[num]

#factorial of num
#uncomment the following to see how recalculations are avoided
##result=[-1]*10
##result[0]=result[1]=1
##print(factorial(5))
# print(factorial(3))
# print(factorial(7))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
