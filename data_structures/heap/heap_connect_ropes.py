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


ropes=[1,2,3,4,5]
cost=0

heap=Heap(ropes)
build_min_heap(heap)
while(heap.length>1):
    a=heap.element.pop(0)
    heap.length-=1
    min_heapify(heap,1)
    b=heap.element.pop(0)
    heap.length-=1
    ans=a+b
    cost+=ans
    heap.element.append(ans)
    heap.length+=1
    build_min_heap(heap)

print(cost)