# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 10:45:27 2021

@author: Debanjan Rudra
"""

if __name__=='__main__':
    
    for _ in range(int(input())):
        
        A = list(map(int,input().rstrip().split()))
        
        x = A[len(A)-1]
        
        for i in range(len(A)-1,0,-1):
            
            A[i] = A[i-1]
            
        A[0] = x
        
        print(A)