n=int(input().strip())
m=2*n-1
a=n;b=2
for i in range(m//2+1):
    if i==0:
        for j in range(a):
            print('*',end='')
    else:
        for j in range(2*i):
            print(' ',end='')
        for j in range(a):
            print('*',end='')
    a-=1
    print()
for i in range(m//2+1,m):
    if i==m-1:
        for j in range(b):
            print('*',end='')
    else:
        for j in range(2*(m-i-1)):
            print(' ',end='')
        for j in range(b):
            print('*',end='')
    b+=1
    print()
	
'''
I/P: 3                    
O/P: ***
       **
         *
       **
     ***	  
'''	 
