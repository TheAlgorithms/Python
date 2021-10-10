# -*- coding: utf-8 -*-
"""
Created on Sat May 22 00:27:36 2021

@author: SHRIDHAR KAPSE
"""

value=[]
for j in range(2):
    lis=[]
    for i in range(3):
        b=int(input("Enter no:", ))
        lis.insert(i,b)
         
    value.insert(j,lis)
print(value)

key=[]

for j in range(2):
   lis1=[]
   for i in range(3):
     a=()
     a=tuple(map(int,input("Enter the tuple:", )))
             
     lis1.insert(i,a) 
    
   key.insert(j,lis1)
   
print(key)
d=[]
d3={}
for j in range(2):
     dict={}
     
     for i in range(3):
       dict[key[j][i]]=value[j][i]
     d.append(dict)
     print('d',j,'=',d[j])

d.append(d3)
d[2]=d[0].copy()
d[2].update(d[1])
for i,j in d[0]:
    for x,y in d[1]:
        if i==x:
            d[2][i]=j+y
            
            
print(d[2])
            




