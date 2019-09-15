'''
- A linked list is similar to an array, it holds values. However, links in a linked list do not have indexes.
- This is an example of a double ended, doubly linked list.
- Each link references the next link and the previous one.
- A Doubly Linked List (DLL) contains an extra pointer, typically called previous pointer, together with next pointer and data which are there in singly linked list.
 - Advantages over SLL - IT can be traversed in both forward and backward direction.,Delete operation is more efficent'''



class Node:
    """
    A linked list element class.
    """
    def __init__(self, value=None, prev=None, next=None):
        self.val = value
        self.prev = prev
        self.next = next

        
class DLinkedList:
    """
    A linked list class, whose elements are an instance of the Node class.
    :param root: The 1st element
    :param end: The last element
    """
    def __init__(self, *values):
        self.root = None
        self.end = None
        self._length = 0
        
        self.add_at_head(*values)

    def add_at_head(self, *values):
        """
        Add a node(s) with value(s) before the first element of a linked list.
        :param values: a number or a sequence of numbers
        :return:
        """
        for val in values[::-1]:
            node = Node(val, None, self.root)
            try:
                self.root.prev = node
            except AttributeError:
                pass
            self.root = node
            if not self.root.next:
                self.end = self.root
        self._length += len(values)

    def add_at_tail(self, *values):
        """
        Append a node(s) with value(s) to the last element of a linked list.
        :param values: additional values
        :return:
        """
        if not self.end:
            self.add_at_head(*values)
        else:
            for val in values:
                self.end.next = Node(val, self.end)
                self.end = self.end.next
            self._length += len(values)

    def add_at_index(self, index, *values):
        """
        Add a node(s) with value(s) before the index-th node in a linked list. If the index equals to the length
        of the linked list, the node will be appended to the end of the linked list.
        :param index: the node index
        :param values: a number or a sequence of numbers
        :return:
        """
        if index == 0:
            self.add_at_head(*values)
        elif index == len(self):
            self.add_at_tail(*values)
        elif 0 < index < len(self):
            for val in values:
                temp = self._get(index - 1)
                node = Node(val, temp, temp.next)
                temp.next = node
                node.next.prev = node
            self._length += len(values)
        else:
            raise IndexError

    def delete_at_index(self, index):
        """
        Delete the index-th node in a linked list, if the index is valid.
        :param index: node index
        :return:
        """
        if 0 <= index < len(self):
            if len(self) == 1:
                self.root = None
                self.end = None
            elif index == 0:
                self.root = self.root.next
                self.root.prev = None
            elif index == len(self) - 1:
                self.end = self.end.prev
                self.end.next = None
            else:
                temp = self._get(index - 1)
                temp.next = temp.next.next
                temp.next.prev = temp
            self._length -= 1
        else:
            raise IndexError

    def pop_root(self):
        """
        Remove the first node from a linked list and return its value.
        :return value: The 1st node value
        """
        if not self:
            return None
        res = self.root.val
        self.delete_at_index(0)
        return res

    def pop_end(self):
        """
        Remove the last node from a linked list and return its value.
        :return value: The last node value
        """
        if len(self) < 2:
            return self.pop_root()
        res = self.end.val
        self.delete_at_index(len(self) - 1)
        return res

    def _get(self, index):
        """
        Get the index-th node in a linked list.
        """
        if index >= len(self):
            raise IndexError
        if index == 0:
            return self.root
        if index == len(self) - 1:
            return self.end
        if index < 0:
            if abs(index) > len(self):
                raise IndexError
            index += len(self)
        temp = None
        if index <= len(self) // 2:
            temp = self.root
            for i in range(index):
                temp = temp.next
        else:
            temp = self.end
            for i in range(len(self) - index - 1):
                temp = temp.prev
        return temp

    def __len__(self):  # len(list)
        return self._length

    def __iter__(self): # for i in list
        for i in range(len(self)):
            yield (self._get(i)).val

    def __getitem__(self, item):    # list[index], list[i, j, k]
        if isinstance(item, slice):
            start = 0 if not item.start else item.start
            stop = len(self) if not item.stop else item.stop
            step = 1 if not item.step else item.step
            if step < 0:
                start, stop = stop, start
                start -= 1
                stop -= 1
            return [(self._get(i)).val for i in range(start, stop, step)]
        return (self._get(item)).val

    def __setitem__(self, key, value):  # list[key] = value
        (self._get(key)).val = value

    def __contains__(self, item):   # if item in list
        temp = self.root
        while temp and temp.val != item:
            temp = temp.next
        return temp is not None

    def __add__(self, other):   # list1 + list2
        first = [i for i in self]
        second = [i for i in other]
        result = DLinkedList(*first)
        result.add_at_tail(*second)
        return result

    def __str__(self):  # str(list)
        return ' >< '.join(str(i) for i in self)
