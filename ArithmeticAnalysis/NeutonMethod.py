import math

def newton(function,function1,startingInt): #function is the f(x) and function1 is the f'(x)
  x_n=startingInt
  while True:
      x_n1=x_n-function(x_n)/function1(x_n)
      if abs(x_n-x_n1)<0.00001:
          return x_n1
      x_n=x_n1
      
def f(x):
    return math.pow(x,3)-2*x-5

def f1(x):
    return 3*math.pow(x,2)-2

print(newton(f,f1,3))