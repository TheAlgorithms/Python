def swap(array,i,j):
    temp=array[i]
    array[i]=array[j]
    array[j]=temp

def max_heapify(heap,i):
    left=2*i
    right=2*i+1

    if(left<=heap.length and heap.element[left-1]>heap.element[i-1]):
        largest=left
    else:
        largest=i
    if(right<=heap.length and heap.element[right-1]>heap.element[largest-1]):
        largest=right
    if(largest!=i):
        swap(heap.element,i-1,largest-1)
        max_heapify(heap,largest)

def build_max_heap(heap):
    length=heap.length
    for i in range(length//2,0,-1):
        max_heapify(heap,i)

class Heap():
    def __init__(self,setter=[]):
        self.element=[]
        if(len(setter)!=0):
            for i in setter:
                self.element.append(i)
        self.length=len(self.element)

arr=[1,3,12,5,15,11]
k1=3
k2=6

def solve(arr,k):
    heap=Heap()
    for i in arr:
        heap.element.append(i)
        heap.length+=1
        build_max_heap(heap)
        if(heap.length>k):
            heap.element.pop(0)
            heap.length-=1
    return heap.element[0]

element1=solve(arr,k1)
element2=solve(arr,k2)
sum=0
for i in arr:
    if(i>element1 and i<element2):
        sum+=i
print(sum)