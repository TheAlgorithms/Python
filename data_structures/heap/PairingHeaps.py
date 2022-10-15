# Pairing Heaps implementation 

class PairingHeap:
    
    def __init__(self):
        self.heap = [0]
        self.size = 0
        self.root=min(self.heap)

    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self.BubbleUp(self.size)

    def merge(self, root1, root2):
        if root1 is None:
            return root2
        elif root2 is None:
            return root1
        elif root1< root2:
            self.heap.append(root2)
            return root1

        else:
            self.heap.append(root1)
        return root2


    def delete(self):
        self.root=None
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        deletedValue = self.heap.pop(-1)
        self.size -= 1
        return deletedValue


    def findMin(self):
        if self.root==None:
            print("Pairing Heap is empty")
        else:
            return self.root


    def getSize(self):
        print (len(self.heap))

# Two Pass Method
        
    def BubbleUp(self, key):
        if self.heap[key] > self.heap[key // 2] or key <= 1:          # parent and child
            return ()
        else:
            self.heap[key], self.heap[key // 2] = self.heap[key // 2], self.heap[key]
            return self.BubbleUp(key // 2)


# Driver Code

heap = PairingHeap()

print("Pairing Heap upon Insertion:")
heap.insert(2)
heap.insert(18)
heap.insert(20)
heap.insert(1)
heap.insert(3)
heap.insert(8)
print(heap.heap)
print()

print("Getting Mininmum in pairing heap:")
print(heap.findMin())
print()

print("Merging roots in pairing heaps:")
print("Smaller root =",heap.merge(5,1))
print("Heap after merge:")
print(heap.heap)
print()

print("Pairing Heap after deleting:")
heap.delete()
heap.delete()
print(heap.heap)
print()

print("Size of Pairing Heap:")
heap.getSize()