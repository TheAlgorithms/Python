#Numerical Integration
import math

def f(x):
    return 1/(1+x)
print("\nPROGRAM is VALID for FUNCTION\nf(x)=root(cos(x))\n")

a=float(input("Enter Lower Limit : "))
b=float(input("Enter Upper Limit : "))
n=int(input("\nEnter Number of Sub-Intervals : "))
h=(b-a)/n

Y=[]
x=a
for i in range(n+1):
    x=a+(i*h)
    Y.append(f(x))
    print('{:<20} | {:<20}'.format(x,f(x)))

#Trapezoidal Rule
def T(L):
    return h*(2*sum(L)-L[0]-L[-1])/2

#Simpson1/3
def S13(L):
    OD,E=0,0
    for i in range(1,n):
        if i%2!=0:
            OD+=L[i]
        else:
            E+=L[i]
    return h*(L[0]+L[-1]+(4*OD)+(2*E))/3

#Simpson3/3
def S38(L):
    A,B=0,0
    for i in range(1,n):
        if i%3!=0:
            A+=L[i]
        else:
            B+=L[i]
    return h*3*(L[0]+L[-1]+(3*A)+(2*B))/8

print("\nTrapezoidal Rule",T(Y),sep='\n')
print("\nSimpson's 1/3 Rule",S13(Y),sep='\n')
print("\nSimpson's 3/8 Rule",S38(Y),sep='\n')
