# function to find double factorial of given number.

'''
Double factorial of a non-negative integer n, 
is the product of all the integers from 1 to n that have the same parity (odd or even) as n.
It is also called as semifactorial of a number and is denoted by !!.
For example, 
9!! = 9*7*5*3*1 = 945. 
Note that--> 0!! = 1.
'''

def double_factorial(input_num): 
    """
  Calculate the double factorial of specified number
  
    >>>double_factorial(5)
    15
    >>>double_factorial(8)
    384
    >>>double_factorial(3)
    3
    >>>double_factorial(0)
    1
    >>>-1
    Traceback (most recent call last):
      File "<string>", line 11, in <module>
      File "<string>", line 4, in doublefactorial
    ValueError: double_factorial() not defined for negative values
    """
    if (input_num<0):
       raise ValueError("double_factorial() not defined for negative values")
    if (input_num == 0 or input_num == 1): 
        return 1; 
    return input_num * double_factorial(input_num - 2)
  
  
# Driver Code 
input_num = int(input("Enter the number to calculate its double factorial = ")) 
print("Double factorial of",input_num,"=", double_factorial(input_num))
