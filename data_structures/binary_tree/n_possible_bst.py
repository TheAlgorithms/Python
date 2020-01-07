'''
Hey, We Are Going to find Some Exciting Number Called Catalan Number which is use to find the Possible binary search
tree and Binary Search Tree from the Number of Nodes.
WE USE THE FORMULA:
t(n) = SUMMATION(i = 1 to n)t(i-1)t(n-i)

You can get Further Detail from Wikipedia:
https://en.wikipedia.org/wiki/Catalan_number
'''
'''
Our Contribution:
Basically we Create the 2 function:
    1. CountBST(n node)
        CountBST Function Count the Number of Binary Search Tree Crated By n number of Node.
        INPUT: N number i.e Number of Nodes
        OUTPUT: Count i.e Number of Possible BST
    1. CountBT(n node)
        CountBT Function Count the Number of Binary Tree Crated By n number of Node.
        INPUT: N number i.e Number of Nodes
        OUTPUT: Count i.e Number of Possible BT
        
    >> CountBST(5)
    >>  42
    >> CountBST(6)
    >> 132
    >> CountBT(5)
    >> 5040
    >> CountBT(6)
    >> 95040
    
    
    >>> For Count of Binary Search Tree We find the Catalan Number Using Binomial Coefficient.
    >>> For Count of Binary Tree We find the Factorial as well as Binomial Coefficient. Multiply both of them to get 
        Number of Count of Binary Tree.
'''

def binomial_coefficient(n, k):
    '''
    Since Here we Find the Binomial Coefficient:
    https://en.wikipedia.org/wiki/Binomial_coefficient
    C(n,k) = n! / k!(n-k)!
    :param n: 2 times of Number of Nodes
    :param k: Number of Nodes
    :return:  Integer Value
    '''
    result = 1    # To kept the Calculated Value
    # Since C(n, k) = C(n, n-k)
    if k > (n - k):
        k = n - k
    #Calculate C(n,k)
    for i in range(k):
        result *= (n - i)   #result = result * (n - i)
        result //= (i + 1)  # result = result // (i + 1)

    return result

'''
We can find Catalan Number in many Ways:
But here we use Binomial Coefficent because it done the Job in O(n)
'''
def catalan(n):
    '''
    This Function will Find the Nth Catalan Number.
    :param n: n number of Nodes
    :return: Nth catalan Number
    '''
    value = binomial_coefficient(2 * n, n);
    # We have to Find the Catalan Number Using 2nCn/(n+1)
    catalan_number = value // (n + 1)
    return catalan_number   # return nth catalan Number

def CountBST(n):
    '''
    This Function Count the Number of Possible Binary Search Tree from Given Number of Nodes.
    :param n: Number of Nodes
    :return: Number : Total Number of Binary Search Tree Formed By Nodes
    '''
    count = catalan(n)  #find the Catalan Number at N index
    return count    #Return the Number of Count

def factorial(n):
    '''
    This Fuction use to Calculate The Factorial of N Number.
    :param n: Nth Value to find the Factorial
    :return: Factorial of Nth Value.
    '''
    result = 1  #kept the Result
    #Calculate the Value upto 1 * 2... n
    for i in range(1, n+1):
        result *= i # result = result * i
    return result

def CountBT(n):
    '''
    This Function return the Count of Binary Tree.
    :param n: n Number of Node
    :return: Count of Binary Tree
    '''
    catalan_value = catalan(n)  #find the nth Catalan Number
    factorial_value = factorial(n)  #find the factorial Value
    count = catalan_value * factorial_value #find the Count of Binary Tree
    return count  #return the Count

if __name__ == '__main__':
    n = int(input('Enter the Number of Node: '))
    print('Total Number of Possible Binary Search Tree from ',n, ' Number of node ',CountBST(n))
    print('Total Number of Possible Binary Search Tree from ',n, ' Number of node ' ,CountBT(n))


