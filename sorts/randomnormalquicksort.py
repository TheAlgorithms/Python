import random
from tempfile import TemporaryFile
import numpy as np
import math



def _inPlaceQuickSort(A,start,end):  
    count = 0
    if start<end:
        pivot=random.gauss(0,1)
        temp=A[end]
        A[end]=A[pivot]
        A[pivot]=temp
        
        p,count= _inPlacePartition(A,start,end)
        count += _inPlaceQuickSort(A,start,p-1)
        count += _inPlaceQuickSort(A,p+1,end)
    return count

def _inPlacePartition(A,start,end):
    
    count = 0
    pivot= random.gauss(0,1)
    temp=A[end]
    A[end]=A[pivot]
    A[pivot]=temp
    newPivotIndex=start-1
    for index in xrange(start,end):
               
        count += 1
        if A[index]<A[end]:#check if current val is less than pivot value
            newPivotIndex=newPivotIndex+1
            temp=A[newPivotIndex]
            A[newPivotIndex]=A[index]
            A[index]=temp
    
    temp=A[newPivotIndex+1]
    A[newPivotIndex+1]=A[end]
    A[end]=temp
    return newPivotIndex+1,count
    
outfile = TemporaryFile()    
print("Enter number of elements :")
p = int(input())
X = np.random.standard_normal(p)
np.save(outfile, X)
print(X)

z = _inPlaceQuickSort(X,0,len(X)-1)
print(z) 
mu, sigma = 0, 1 # mean and standard deviation
s = np.random.normal(mu, sigma, p)
np.save(outfile, s)
print(s)

count, bins, ignored = plt.hist(s, 30, normed=True)

plt.plot(bins , 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')
plt.show()    
    
 
print("Do you want to use the same array: 1/2 ?")
inpt = int(input()) 
if(inpt == 1):
    outfile.seek(0)
    M = np.load(outfile)
    r = float(len(M)-1)
    i = 0
    while i < (math.log(r,2)):
        z = _inPlaceQuickSort(M,0,pow(2,i)-1)
        print(z)
        i += 1
    
    
else:
    N = np.random.normal(mu, sigma, p)
    h = _inPlaceQuickSort(N,0,len(N)-1)
    print(h)
    


