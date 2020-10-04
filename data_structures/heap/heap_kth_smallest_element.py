# import heapq

# array=[]
# lists=[7,10,4,3,20,15]
# k=3
# for i in lists:
#     heapq.heappush(array,i)
#     if(len(array)>3):
#         array.pop()

# print(array[k-1])

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


lists=[7,10,4,3,20,15]
k=3
heap=Heap()
for i in lists:
    heap.element.append(i)
    heap.length+=1
    build_max_heap(heap)
    if(heap.length>k):
        heap.element.pop(0)
        heap.length-=1

print(heap.element[0])