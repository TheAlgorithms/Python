def swap(array,i,j):
    temp=array[i]
    array[i]=array[j]
    array[j]=temp

def min_heapify(heap,i):
    left=2*i
    right=2*i+1

    if(left<=heap.length and heap.element[left-1][0]<heap.element[i-1][0]):
        smallest=left
    else:
        smallest=i
    if(right<=heap.length and heap.element[right-1][0]<heap.element[smallest-1][0]):
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

arr=[1,1,1,3,2,2,4]
k=2
d={}
arr2=[]
for i in arr:
    if(i in d):
        d[i]+=1
    else:
        d[i]=1

for key,element in d.items():
    arr2.append([element,key])

heap=Heap()
for i in arr2:
    heap.element.append(i)
    heap.length+=1
    build_min_heap(heap)
    if(heap.length>k):
        heap.element.pop(0)
        heap.length-=1

print(heap.element)

for i in heap.element:
    print(i[1])