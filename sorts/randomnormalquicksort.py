import random
from tempfile import TemporaryFile
import numpy as np
import math
import matplotlib.pyplot as plt


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
p = 1000 # 1000 elements are to be sorted




mu, sigma = 0, 1 # mean and standard deviation
X = np.random.normal(mu, sigma, p)
np.save(outfile, X)
print(X)

count, bins, ignored = plt.hist(X, 30, normed=True)

plt.plot(bins , 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')
plt.show()    
    



outfile.seek(0)  # using the same array
M = np.load(outfile)
r = float(len(M)-1)
i = 0
while i < (math.log(r,2)):
    z = _inPlaceQuickSort(M,0,pow(2,i)-1) # taking 0, 2 , 4, 8, 16 .... elements in succesion and printing the number of comparisons
    print("No of Comprisons for %d elements is %d"%(pow(2,i)-1,z))
    i += 1
 
