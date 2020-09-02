# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 20:43:05 2020

@author: Saptarshi
"""
n = int(input())


ans = []

if n==1:
    print(1)
    print(1)
    quit()

w=n    
for i in range(1, n):
    if w>2*i:
        ans.append(i)
        w=w-i
    else:
        ans.append(w)
        break
    
   

print(len(ans))
print(' '.join([str(i) for i in ans]))
