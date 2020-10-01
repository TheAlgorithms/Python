#What is __init__.py ?
#The __init__.py files are required to make Python treat the directories as containing packages; this is done to prevent directories with a common name, such as string, 
#from unintentionally hiding valid modules that occur later on the module search path.


#What is inside __init__.py ?
#The __init__.py file makes Python treat directories containing it as modules. Furthermore, this is the first file to be loaded in a module, so you can use it to execute code that
#you want to run each time a module is loaded, or specify the submodules to be exported.


# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    x, y = 0, 1
    while x < n:
        print(x, end=' ')
        x, y = y, x+y
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    x, y = 0, 1
    while x < n:
        result.append(a)
        x, y = x, x+y
    return result
    
#The module is completed!
#Now it can be simply imported

import fibo
