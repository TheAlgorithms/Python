for i in range(1,6):
    for j in range(1,6):
        if(j<=6-i):
            print("*",end="")
        else:
            print(" ",end="")    
    print()        

for i in range(1,6):
    for j in range(1,6):
        if(j<=i):
            print(j,end="")    
        else:
            print(" ",end="")
    print() 

for i in range(1,6):
    for j in range(1,6):
        if(j>=i):
            print("*",end="")    
        else:
            print(" ",end="")
    print()            

for i in range(1,6):
    for j in range(1,6):
        if(j>=6-i and j<=5):
            print("&",end="")    
        else:
            print(" ",end="")
    print()      

for i in range(1,6):
    for j in range(1,6):
        if(j>=i):
            print("1",end="0")      
        else:
            print(" ",end="")
    print()  

for i in range(1,6):
    for j in range(1,6):
        if(j>=6-i and j<=5):
            print("*",end=" ")    
        else:
            print(" ",end="")
    print()  

for i in range(1,6):
    for j in range(1,10):
        if(j>=10-i):
            print("*",end="")  
        if(j>=11-i):
            print("*",end="")      
        else:
            print(" ",end="")
    print()  

for i in range(1,6):
    for j in range(1,6):
        if(j>=i):
            print("*",end="")  
        if(j>=i+1):
            print("*",end="")
        else:
            print(" ",end="")
    print()  

for i in range(1,6):
    for j in range(1,10):
        if(j>=i and j<=10-i):
            print("*",end="")  
        else:
            print(" ",end="")
    print()

for i in range(1,6):
    for j in range(1,6):
        if(j<=i):
            print(i,end="")  
        else:
            print(" ",end="")
    print()

for i in range(1,6):
    for j in range(1,6):
        if(j>=6-i):
            print(i,end="")  
            i=i-1 
        else:
            print(" ",end="")
    print()

for i in range(1,6):
    for j in range(1,10):
        if(j>=6-i and j<=4+i):
            print("*",end="")  
        else:
            print(" ",end="")
    print()

for i in range(1,6):
    for j in range(1,6):
        if(j<=6-i):
            print(7-j-i,end="")
        else:
            print(" ",end="")    
    print()      

for i in range(1,5):
    for j in range(1,8):
        if(j>=i and j<=8-i):
            if((j-i)%2==0):
                print("1",end="")
            else:
                print("0",end="") 
        else:
            print(" ",end="")
    print()        