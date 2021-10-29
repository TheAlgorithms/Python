import math
print("enter points P1(x1,y1) and P2(x2,y2): ")
x1=int(input("enter x1:"))
y1=int(input("enter y1:"))
x2=int(input("enter x2:"))
y2=int(input("enter y2:"))


distt= ((x1-x2)**2+(y1-y2)**2)
dist=math.sqrt(distt)
print("THE EUCLIDIAN DISTANCE BETWEEN THE POINTS P1 AND P2 IS :")
print(dist)