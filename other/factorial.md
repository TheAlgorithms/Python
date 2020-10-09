### find factorial of number 

## With recursion 

def fact(n): 

    if(n<=1): 

        return 1 

    return n * fact(n-1)   

  

# 5 * fact(4)   

# 4 * fact(3) 

a = fact(5) 

print(a) 



def factWithoutRecursion(n):

    temp = 1

    for i in range(n, 0, -1):

        temp = temp * i

    return temp

a = factWithoutRecursion(5) 
