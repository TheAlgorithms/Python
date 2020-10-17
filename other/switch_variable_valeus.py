def switch(x, y):   
  temp = x   
  x = y   
  y = temp   
  print("var1 = " + x + ", var2 = " + y)  

var1 = input("Enter value for variable 1: ") 
var2 = input("Enter value for variable 2: ") 
print("Before switch: var1 = " + var1 + ", var 2 = " + var2) 
print("After switch: ", end="")
switch(var1, var2)
