def factorial(n):
    if n==0:
        return 1
    elif n<0:
        print("ValueError: factorial() not defined for negative  values")
    else:
        return n*factorial(n-1)
    
n=int(input("Enter a number"))
factorial(n)
