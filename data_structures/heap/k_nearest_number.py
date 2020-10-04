def swap(array,i,j):
    temp=array[i]
    array[i]=array[j]
    array[j]=temp

def max_heapify(heap,i):
    left=2*i
    right=2*i+1

    if(left<=heap.length and heap.element[left-1][0]>heap.element[i-1][0]):
        largest=left
    else:
        largest=i
    if(right<=heap.length and heap.element[right-1][0]>heap.element[largest-1][0]):
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


arr=[5,6,7,8,9]
k=3
x=7
heap=Heap()
for i in arr:
    heap.element.append([abs(i-x),i])
    heap.length+=1
    build_max_heap(heap)
    if(heap.length>k):
        heap.element.pop(0)
        heap.length-=1

for i in heap.element:
    print(i[1])