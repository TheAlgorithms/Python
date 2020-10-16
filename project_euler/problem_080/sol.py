"""
Project Euler Problem 80: https://projecteuler.net/problem=80
Author: Sandeep Gupta
Problem statement: For the first one hundred natural numbers, find the total of
the digital sums of the first one hundred decimal digits for all the irrational
square roots.
"""

import math as m
def sqrtn(a, d):
   for x in range(1, 10):
       div = d*20 +x
       if div*x <= a <(div+1)*(x+1):
           return (x, a - div*x)
       
   return (0, a)
           

# a =int(input())   
def solution():  
    """ 
    used simple trick of calculating square root by hand on notebooks.
    
    answer : 40886
    """
    sos =0   
    num =1
    
    while num<=100:
        
        if m.sqrt(num)% m.floor(m.sqrt(num)) == 0:
            num +=1
            continue
        a = num 
        
        s = int
        if len(str(a))%2 ==0:
            s = 2
        else:
            s = 1
        
        ans =[] 
        
        k=0
        last = 0
        rem = 0
        for j in range(s,(len(str(a)))+1,2):
            i = int(str(rem)+str(a)[k:j])
            # print("i: ",i,end=" ")
            last ,rem = sqrtn(i, last)
            # print(last, rem)
            ans.append(last)
            last =""
            for i in ans:
                last +=str(i)
            last =int(last)
            k=j
                
        while len(ans)< 100:
            i = int(str(rem)+"00")
            # print("i: ",i,end=" ")
            last ,rem = sqrtn(i, last)
            # print(last, rem)
            ans.append(last)
            # result.append(last)
            last =""
            for i in ans:
                last +=str(i)
            last =int(last)
    
        sos += sum(ans)
        num +=1
    return sos
        
if __name__ == "__main__":
    print(solution())
        
