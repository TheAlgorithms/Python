#Problem Statement :- https://leetcode.com/problems/kth-largest-element-in-a-stream/


from heapq import heapify, heappop, heappush, heappushpop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.k = k
        self.arr = nums
        
        heapify( self.arr) 
        
        # Keep popping smaller elemnts till size = k
        while len( self.arr ) > self.k:
            heappop( self.arr )

    def add(self, val: int) -> int:
        
        heap_top = 0
        
        # Always keep heap size = k
        # Top element = kth largest element
        if len( self.arr ) < self.k:
            heappush( self.arr, val)
        else:
            heappushpop( self.arr, val)
        
        return self.arr[heap_top]