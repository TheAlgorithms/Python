from math import sqrt
x=2
z=0
y=0
while True:
    flag=0
    for y in range(2,int(sqrt(x))):
        if(x%y==0):
            flag=1
            break
    if(flag==0):
        z+=1
    if(z==10001):
        print(x)
        break
    x+=1
