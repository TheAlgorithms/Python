a=25

# 1. if else-if else ladder statement in python
if(a<3):
    print("The value of a is greater than 3")
elif(a>10):
    print("The value of a is greater than 10")
else: 
    print("The value of a is not greater than 3 or 10")
    
# 2. multiple if statements in python
if(a<3):
    print("The value of a is greater than 3")

if(a>10):
    print("The value of a is greater than 10")

if(a>10 and a<20): 
    print("The value of a is between 10 and 20")
    
if(a>20 and a<30):
    print("The value of a is between 20 and 30")
else: 
    print("The value of a is greater than 30")
    
print("Done")