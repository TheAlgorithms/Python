
def swap(data,index1,index2):
    temp=data[index1]
    data[index1]=data[index2]
    data[index2]=temp
    return data
def heapify(data,size,index):
    left=(2*index)+1
    right=(2*index)+2
    largest=index

    if left<size and data[left]>data[largest]:
        largest=left
    if right<size and data[right]>data[largest]:
        largest=right

    if largest!=index:
        data=swap(data,index,largest)
        data=heapify(data,size,largest)

    return data

def heapSort(data):
    n=len(data)
    leastParent=n
    for i in range(leastParent,-1,-1):
        data=heapify(data,n,i)

    for i in range(n-1,0,-1):
        if(data[0]>data[i]):
            data=swap(data,0,i)
            data=heapify(data,i,0)
    return data


from random import randint
# data=[13, 302, 602, 851, 351, 186]

data=[randint(1,1000) for x in range(6)]
data=heapSort(data)
print(data)
