def maxDivide( a, b ): 
    while a % b == 0: 
        a = a / b 
    return a  
  

def isUgly( no ): 
    no = maxDivide(no, 2) 
    no = maxDivide(no, 3) 
    no = maxDivide(no, 5) 
    return 1 if no == 1 else 0
  
def getNthUglyNo( n ): 
    i = 1
    count = 1 
  
 
    while n > count: 
        i += 1
        if isUgly(i): 
            count += 1
    return i 
  
num=input("Enter number:")
no = getNthUglyNo(150) 
print("150th ugly no. is ", no) 
