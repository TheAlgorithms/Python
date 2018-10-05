from math import sqrt
x=3

while x<=sqrt(600851475143):
    y=2
    flag=0
    while y<=sqrt(x):
        if(x%y==0):
            flag=1
            break
        else:
            y+=1
    if(flag==0 | 600851475143%x==0):
        print(x)
    x+=1
