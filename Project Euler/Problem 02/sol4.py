a=1
b=2
c=3
newnum=0
result=2
while newnum<4000000:
    newnum=c+b
    if newnume%2==0:
        result+=newnum
    x=c
    y=b
    z=a
    c=newnum
    b=x
    a=y

print(result)
