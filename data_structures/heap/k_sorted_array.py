def swap(array,i,j):
    temp=array[i]
    array[i]=array[j]
    array[j]=temp

def min_heapify(heap,i):
    left=2*i
    right=2*i+1

    if(left<=heap.length and heap.element[left-1]<heap.element[i-1]):
        smallest=left
    else:
        smallest=i
    if(right<=heap.length and heap.element[right-1]<heap.element[smallest-1]):
        smallest=right
    if(smallest!=i):
        swap(heap.element,i-1,smallest-1)
        min_heapify(heap,smallest)

def build_min_heap(heap):
    length=heap.length
    for i in range(length,0,-1):
        min_heapify(heap,i)

class Heap():
    def __init__(self,setter=[]):
        self.element=[]
        if(len(setter)!=0):
            for i in setter:
                self.element.append(i)
        self.length=len(self.element)

arr=[6,5,3,2,8,10,9]
k=3
heap=Heap()
sorted_array=[]

for i in arr:
    heap.element.append(i)
    heap.length+=1
    build_min_heap(heap)
    if(heap.length>k):
        item=heap.element.pop(0)
        sorted_array.append(item)
        heap.length-=1
        
while(heap.length>0):
    item=heap.element.pop(0)
    sorted_array.append(item)
    heap.length-=1
    build_min_heap(heap)

print(sorted_array)