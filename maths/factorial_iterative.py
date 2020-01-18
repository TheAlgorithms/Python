# factorial of a number


n=int(input("Enter a number"))
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

if n>=0:
    print(factorial(n))
else:
    raise ValueError("ValueError: factorial() not defined for negative vlaues")
    

    
    

