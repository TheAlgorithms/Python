from __future__ import print_function
try:
	xrange		#Python 2
except NameError:
	xrange = range	#Python 3


from sympy import *
numofprime=0
con=1
lis=[1]
i=3
while True:
    for j in xrange(4):
        con+=i-1
        lis.append(con)
  
    for k in lis[-4:]:
        if isprime(k)==True:
            numofprime+=1
    
    if numofprime/len(lis)<0.1:
        print(i)
        break
    
    i+=2

#26241-answer

