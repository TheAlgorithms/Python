n=6
a=1
for i in range(n,0,-1):
     print(format(" "*(n+1-i),"<1"),end="")
     for j in range(1,i):
          print(format(a,"<2"),end="")
          a+=1
b=a*2-2
for i in range(n,1,-1):
     for j in range(i,1,-1):
          print(b,end=" ")
          b-=1
     print( )