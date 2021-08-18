from typing import Any, Hashable

'''
The following implementation of LRU Cache is one of the most elegant pythonic implementations. 
It only uses the in-built python dictionary. This works because 
the Python dictionary maintains the order of insertion of keys and ensures O(1) operations on insert, delete and access.
'''
class LRUCache(dict):
    '''
    Initialize an LRU Cache with given capacity.
    capacity : int -> the capacity of the LRU Cache
    '''
    def __init__(self, capacity : int):
        self.remaining:int = capacity
	
    '''
    This method gets the value associated with the key.
    key : Hashable -> a hashable object that is mapped to a value inside of the LRU cache.
    returns -> value : Any -> any object that is stored as a value inside of the LRU cache.
    '''
    def get(self, key:Hashable)->Any:
        if key not in self:
            raise KeyError(f"{key} not found.")
        val = self.pop(key) # Pop the key-value and re-insert to maintain the order
        self[key] = val
        return val

    '''
    This method puts the value associated with the key provided inside of the LRU cache.
    key : Hashable -> a hashable object that is mapped to a value inside of the LRU cache.
    value: Any -> any object that is to be associated with the key inside of the LRU cache.
    '''
    def put(self, key:Hashable, value:Any):
        # To pop the last value inside of the LRU cache
        if key in self:
            self.pop(key)
            self[key] = value
            return

        if self.remaining > 0: self.remaining -= 1
        # To pop the least recently used item from the dictionary 
        else: self.pop(next(iter(self)))
        self[key] = value