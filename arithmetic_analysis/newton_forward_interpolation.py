import math
from typing import List

def main() -> None:
    n = int(input("enter the numbers of values: "))

    print("enter the values of parameters in a list: ")
    x = list(map(int, input().split()))

    #to check if values of x is valid for Newton Forward Interpolation
    constant=x[1]-x[0]
    for i in range(2,n):
        if x[i]-x[i-1]!=constant:
            print("Not valid for Newton Forward Interpolation")
            
    print("enter the values of corresponding parameters: ")
    y = list(map(int, input().split()))
    
    value = int(input("enter the value to interpolate: "))
    u = (value - x[0]) / (x[1] - x[0])

    # for calculating the required value
    answer=y[0]
    temp=1  # for the part with u(u-1).../4!
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            y[j] = y[j + 1] - y[j]
        temp=temp*(u-i)/(i+1)
        answer=answer+y[0]*temp

    print(f"the value at {value} is {answer}")

if __name__ == "__main__":
    main()
