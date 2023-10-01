def func(x):
    return x*x*x - x*x + 2
  
# Prints root of func(x) with error of EPSILON
def bisection(x, y):
 
    if (func(x) * func(y) >= 0):
        print("You have not assumed right a and b\n")
        return
  
    z = x
    while ((y-x) >= 0.01):
 
        # Find middle point
        z = (x+y)/2
  
        # Check if middle point is root
        if (func(z) == 0.0):
            break
  
        # Decide the side to repeat the steps
        if (func(z)*func(x) < 0):
            y = z
        else:
            x = z
             
    print("The value of root is : ","%.4f"%z)
     
a = int(input())
b = int(input())
bisection(a, b)
