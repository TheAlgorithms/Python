def factorial(n):
    if n==0:
        return 1
    elif n<0:
        raise ValueError("ValueError: factorial() not defined for negative  values")
    else:
        return n*factorial(n-1)

if __name__=="__main__":
    n=int(input("Enter a number"))
factorial(n)
