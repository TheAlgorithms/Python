"""
Implementing Deque using DoublyLinkedList ...
Operations:
    1. insertion in the front -> O(1)
    2. insertion in the end -> O(1)
    3. remove from the front -> O(1)
    4. remove from the end -> O(1)
"""


class _DoublyLinkedBase:
    """A Private class (to be inherited)"""

    class _Node:
        __slots__ = "_data", "_next", "_prev"

        def __init__(self, link_p, element, link_n):
            self._prev = link_p
            self._data = element
            self._next = link_n

        def has_next_and_prev(self):
            return (
                f" Prev -> {self._prev is not None}, Next -> {self._next is not None}"
            )

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self.__len__() == 0

    def _insert(self, predecessor, e, successor):
        # Create new_node by setting it's prev.link -> header
        # setting it's next.link -> trailer
        new_node = self._Node(predecessor, e, successor)
        predecessor._next = new_node
        successor._prev = new_node
        self._size += 1
        return self

    def _delete(self, node):
        predecessor = node._prev
        successor = node._next

        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        temp = node._data
        node._prev = node._next = node._data = None
        del node
        return temp


class LinkedDeque(_DoublyLinkedBase):
    def first(self):
        """return first element
        >>> d = LinkedDeque()
        >>> d.add_first('A').first()
        'A'
        >>> d.add_first('B').first()
        'B'
        """
        if self.is_empty():
            raise Exception("List is empty")
        return self._header._next._data

    def last(self):
        """return last element
        >>> d = LinkedDeque()
        >>> d.add_last('A').last()
        'A'
        >>> d.add_last('B').last()
        'B'
        """
        if self.is_empty():
            raise Exception("List is empty")
        return self._trailer._prev._data

    # DEque Insert Operations (At the front, At the end)

    def add_first(self, element):
        """insertion in the front
        >>> LinkedDeque().add_first('AV').first()
        'AV'
        """
        return self._insert(self._header, element, self._header._next)

    def add_last(self, element):
        """insertion in the end
        >>> LinkedDeque().add_last('B').last()
        'B'
        """
        return self._insert(self._trailer._prev, element, self._trailer)

    # DEqueu Remove Operations (At the front, At the end)

    def remove_first(self):
        """removal from the front
        >>> d = LinkedDeque()
        >>> d.is_empty()
        True
        >>> d.remove_first()
        Traceback (most recent call last):
           ...
        IndexError: remove_first from empty list
        >>> d.add_first('A') # doctest: +ELLIPSIS
        <data_structures.linked_list.deque_doubly.LinkedDeque object at ...
        >>> d.remove_first()
        'A'
        >>> d.is_empty()
        True
        """
        if self.is_empty():
            raise IndexError("remove_first from empty list")
        return self._delete(self._header._next)

    def remove_last(self):
        """removal in the end
        >>> d = LinkedDeque()
        >>> d.is_empty()
        True
        >>> d.remove_last()
        Traceback (most recent call last):
           ...
        IndexError: remove_first from empty list
        >>> d.add_first('A') # doctest: +ELLIPSIS
        <data_structures.linked_list.deque_doubly.LinkedDeque object at ...
        >>> d.remove_last()
        'A'
        >>> d.is_empty()
        True
        """
        if self.is_empty():
            raise IndexError("remove_first from empty list")
        return self._delete(self._trailer._prev)
