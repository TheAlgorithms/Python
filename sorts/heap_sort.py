'''
This is a pure python implementation of the heap sort algorithm.

'''

from random import randint
import math
def parent(i):
    return math.floor((i-1)/2)

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def max_heapify(b,i,n):
    a=list(b)
    l,r,largest=left(i),right(i),0    
    if l<n and a[l]>a[i]:
        largest=l
    else:
        largest=i
    if r<n and a[largest]<a[r]:
        largest=r
    if largest!=i:
        a[largest],a[i]=a[i],a[largest]
        a=list(max_heapify(a,largest,n))
    return a    

def min_heapify(b,i,n):
    a=list(b)
    l,r,smallest=left(i),right(i),0    
    if l<n and a[l]<a[i]:
        smallest=l
    else:
        smallest=i
    if r<n and a[smallest]>a[r]:
        smallest=r
    if smallest!=i:
        a[smallest],a[i]=a[i],a[smallest]
        a=list(min_heapify(a,smallest,n))
    return a    

def build_min_heap(a):
    for i in range((len(a)//2)-1,-1,-1):
        a=list(min_heapify(a,i,len(a)))
    return a    


def build_max_heap(a):
    for i in range((len(a)//2)-1,-1,-1):
        a=list(max_heapify(a,i,len(a)))
    return a    

def heap_sort_asc(a):
    n=len(a)
    a=list(build_max_heap(a))
    for i in range(n-1,0,-1):
        a[0],a[i]=a[i],a[0]
        a=list(max_heapify(a,0,i))
    return a

def heap_sort_desc(a):
    n=len(a)
    a=list(build_min_heap(a))
    for i in range(n-1,0,-1):
        a[0],a[i]=a[i],a[0]
        a=list(min_heapify(a,0,i))
    return a


def extract_max(a):
    a=list(build_max_heap(a))
    ans=a[0]
    a[0],a[len(a)-1]=a[len(a)-1],a[0]
    a.pop()
    return max_heapify(a,0,len(a)),ans
    
def extract_min(a):
    a=list(build_min_heap(a))
    ans=a[0]
    a[0],a[len(a)-1]=a[len(a)-1],a[0]
    a.pop()
    return min_heapify(a,0,len(a)),ans

if __name__=='__main__':
    n=int(input('Enter the size of an array'))
    print('For random input , enter 1 else 2 :\n')
    op=int(input())
    if op==1:        
        a=[]
        for i in range(n):
            a.append(randint(1,n+1))
    elif op==2:
        print('Enter {} elements of array'.format(n))
        a=[]
        for i in range(n):
            a.append(int(input()))
    print('Select from below option to proceed')    
    print('1.Build Max Heap\n2.Build Min Heap\n3.Extract Maximum\n4.Extract Minimum\n5.Heap Sort (ascending)\n6.Heap Sort (descending)\n7.Exit\n')    
    inp=int(input())
    while inp!=7:
        if inp==1:
            print(build_max_heap(a))
        elif inp==2:
            print(build_min_heap(a))
        elif inp==3:
            print(extract_max(a))
        elif inp==4:
            print(extract_min(a))
        elif inp==5:
            print(heap_sort_asc(a))
        elif inp==6:
            print(heap_sort_desc(a))
        else:
            print('Invalid Option , Select again')
        inp=int(input('Done, Now What ?'))    
        
