"""
This is the implementation of a dynamic array, and is simillar to the 
array implementaion in python standard library
"""

import ctypes

class DynamicArray(object):

    def __init__(self):
        self.length = 0
        self.capacity = 1
        self.array = self.make_array(self.capacity)
    
    def __len__(self):
        return self.length
    
    def __getitem__(self, k):
        if not 0 <= k <= self.length:
            return IndexError(f"{k} Out of Bounds")
        return self.array[k]
    
    def append(self, elem):
        if self.length == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.length] = elem
        self.length += 1
    
    def _resize(self, newCapacity):
        B = self.make_array(newCapacity)
        for elem in range(self.length):
            B[elem] = self.array[elem]
        self.array = B
        self.capacity = newCapacity

    def make_array(self, newCapacity):
        return (newCapacity * ctypes.py_object)()


if __name__ == "__main__":
    from doctest import testmod

    testmod()