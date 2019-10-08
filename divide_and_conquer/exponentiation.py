x=input("x : ")
y=input("y : ")

x1=int(x)
y1=int(y)
# print("x:",x,"y:",y)
ans=int(1)
while(y1>0):
    # print("x:",x1,"y:",y1, "ans:", ans) 
    if(y1%2 == 1):      
        ans=ans*x1
    x1=x1*x1
    y1=int(y1/2)



print("x^y is ", ans)