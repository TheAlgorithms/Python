class Double_Linked_List_Node():
    '''
    Double Linked List Node for LRU Cache
    '''

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class Double_Linked_List():
    '''
    Double Linked List for LRU Cache

    Methods:
        add:        Adds the given node to the end of the list
        remove:     Removes the given node from the list
    '''

    def __init__(self):
        self.head = Double_Linked_List_Node(None, None)
        self.rear = Double_Linked_List_Node(None, None)
        self.head.next = self.rear
        self.rear.prev = self.head

    def add(self, node: Double_Linked_List_Node) -> None:
        temp = self.rear.prev
        temp.next = node
        node.prev = temp
        self.rear.prev = node
        node.next = self.rear

    def remove(self, node: Double_Linked_List_Node) -> Double_Linked_List_Node:
        temp_last = node.prev
        temp_next = node.next
        node.prev = None
        node.next = None
        temp_last.next = temp_next
        temp_next.prev = temp_last

        return node


class Lru_Cache:
    '''
    LRU Cache to store a given capacity of data

    Methods:
        get:        Returns the value for the input key. Raises Value Error if key is
                    not present in cache
        set:        Sets the value for the input key
        has_key:    Checks if the input key is present in cache

    >>> cache = Lru_Cache(2)

    >>> cache.set(1, 1)

    >>> cache.set(2, 2)

    >>> cache.get(1)
    1

    >>> cache.set(3, 3)

    >>> cache.get(2)
    Traceback (most recent call last):
    ...
    ValueError: Key '2' not found in cache

    >>> cache.set(4, 4)

    >>> cache.get(1)
    Traceback (most recent call last):
    ...
    ValueError: Key '1' not found in cache

    >>> cache.get(3)
    3

    >>> cache.get(4)
    4

    >>> cache.has_key(1)
    False

    >>> cache.has_key(4)
    True
    '''

    def __init__(self, capacity):
        self.list = Double_Linked_List()
        self.capacity = capacity
        self.num_keys = 0
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.list.add(self.list.remove(self.cache[key]))
            return self.cache[key].val
        raise ValueError(f"Key '{key}' not found in cache")

    def set(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.num_keys >= self.capacity:
                key_to_delete = self.list.head.next.key
                self.list.remove(self.cache[key_to_delete])
                del self.cache[key_to_delete]
                self.num_keys -= 1
            self.cache[key] = Double_Linked_List_Node(key, value)
            self.list.add(self.cache[key])
            self.num_keys += 1

        else:
            node = self.list.remove(self.cache[key])
            node.val = value
            self.list.add(node)

    def has_key(self, key: int) -> bool:
        return key in self.cache


if __name__ == "__main__":
    import doctest

    doctest.testmod()
