import math
x = 2
add = 0
a = int(input("Enter Numerator: "))
b = int(input("Enter Denomenator: "))

c = a/b
temp = c

print(c)
print("Output: 0")
while(add!=c):
    if((1/x)<=temp):
        add=add+(1/x)
        temp=c-add
        print("+1/", x)
    x=x+1


print(add)
