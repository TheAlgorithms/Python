# max heap using array

class maxHeap:
    def __init__(self):
        self.data=[]
        self.length=0
    def getLength(self):
        return self.length
    def leftChild(self,index):
        if self.getLength()>=(2*index)+1:
            return self.data[(2*index)+1]
        else:
            return None
    def rightChild(self,index):
        if self.getLength()>=(2*index)+2:
            return self.data[(2*index)+2]
        else:
            return None
    def getMax(self):
        if self.getLength()==0:
            return None
        return self.data[0]

    def swap(self,index1,index2):
        temp=self.data[index1]
        self.data[index1]=self.data[index2]
        self.data[index2]=temp
    def getMaxChildIndex(self,index):
        if 2*index<self.length:
            if self.length>2*index+2:
                if self.data[(2*index)+1]>self.data[(2*index)+2]:
                    return (2*index)+1
                return (2*index)+2
        else:
            return None


    def heapify(self,index):
        if index !=0 and self.data[index//2]<self.data[index]:
            # this is for upward sorting
             while index !=0 and self.data[index//2]<self.data[index]:
                 self.swap(index,index//2)
                 index=index//2
        else:
            check=self.getMaxChildIndex(index)
            while check!=None:
                if self.data[check]> self.data[index]:
                    self.swap(index,check)
                    index=check
                    check=self.getMaxChildIndex(index)
                else:
                    break

    def insert(self,value):
        self.data.append(value)
        self.length+=1
        self.heapify(self.length-1)
        print(self.length,">>>",self.data)

    def delete(self):
        temp=self.data[0]
        self.swap(0,self.length-1)
        self.data=self.data[:self.length-1]
        self.length-=1
        self.heapify(0)
        print(self.length,">>>",self.data)
        return temp


heap=maxHeap()
from random import randint
for i in range(20):
    heap.insert(randint(1,1000))

# for i in range(19):
#     print(heap.delete())
print("\n\n\n")
for i in range(19):
    print("max element>>",heap.delete())


