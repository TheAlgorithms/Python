"""
two way heaps method is a technique used to efficiently maintain and retrieve the median of a stream of numbers (array of integers).

this method uses both max and min heap , max heap is used to store the smaller half of the numbers while min heap is used to store
larger number.

this arrangement helps us in retrieving the median of a stream of numbers easily and the time complexity of algorithm is constant [O(1)].
In brute-force method time complexity of this medianfinder algorithm would be O(n logn)

a medium article to better understand this algorithm

https://stephenjoel2k.medium.com/two-heaps-min-heap-max-heap-c3d32cbb671d 

"""


import heapq

class MedianFinder:


    def __init__(self):
        self.maxheap = []
        self.minheap = []


    def insert(self , value):
        if not self.maxheap or value <= -self.maxheap[0]:
            heapq.heappush(self.maxheap , -value)
        else :
            heapq.heappush(self.minheap , value)        

        if len(self.maxheap) - len(self.minheap) > 1:
            heapq.heappush(self.minheap , -heapq.heappop(self.maxheap))    

        elif len(self.minheap) - len(self.maxheap) > 1:
            heapq.heappush(self.maxheap , -heapq.heappop(self.minheap))
    

    def findMedian(self):
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0]) / 2.0
        
        elif len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        
        return self.minheap[0]


def main():
    

    median_finder = MedianFinder()

    stream_of_number = [5, 8, 2, 10, 1, 7, 6]

    for value in stream_of_number:
        median_finder.insert(value)

    median = median_finder.findMedian()
    print("Median:" , median)    # Median = 6

main()