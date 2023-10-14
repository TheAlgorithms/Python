import numpy as np

def pivoting(a,n,i):
    max_index=i
    for index in range(i+1,n):
        if abs(a[index][i])>abs(a[max_index][i]):
            max_index=index
    return max_index

def gauss_elimination_pivoting(a,b,n):
    x=[]
    for i in range(n-1):
        new_index=pivoting(a,n,i)
        a[i],a[new_index]=a[new_index],a[i]
        b[i],b[new_index]=b[new_index],b[i]
        pivot=a[i][i]
        for j in range(i+1,n):
            m=-1*a[j][i]/pivot
            for k in range(0,n):
                a[j][k]+=m*a[i][k]
            b[j]+=m*b[i]
            
    for p in range(n-1,-1,-1):
        x.append(b[p]/a[p][p])
        for q in range(p-1,-1,-1):
            b[q]=b[q]-x[n-p-1]*a[q][p]
    return x
