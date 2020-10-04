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

heap=Heap()

arr=[[1,3],[-2,2],[5,8],[0,1]]
k=2
arr2=[]
for i in arr:
    distance=i[0]**2+i[1]**2
    arr2.append([distance,i[0],i[1]])

for i in arr2:
    heap.element.append(i)
    heap.length+=1
    build_max_heap(heap)
    if(heap.length>k):
        heap.element.pop(0)
        heap.length-=1

for i in heap.element:
    print(str(i[1])+" "+str(i[2]))