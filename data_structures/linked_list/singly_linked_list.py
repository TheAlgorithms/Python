class Node:
    def __init__(self, data=None, next=None):
        self.val = data  # given data
        self.next = next  # given next


class Linked_List:
    """
    A linked list class, whose elements are instances of the Node class.
    :param root: The 1st element
    :param end: The last element
    """
    def __init__(self, *values):
        self.root = None
        self.end = None
        self._length = 0    # length of the list

        self.add_at_head(*values)

    def add_at_head(self, *values):
        """
        Add a node(s) with value(s) before the first element of a linked list.
        :param values: a number or a sequence of numbers
        :return:
        """
        for val in values[::-1]:    # you can add many values
            node = Node(val, self.root) # create a new node
            self.root = node
            if not self.root.next:
                self.end = self.root
        self._length += len(values) # increase the length

    def add_at_tail(self, *values):
        """
        Append a node(s) with value(s) to the last element of a linked list.
        :param values: a number or a sequence of numbers
        :return:
        """
        if not self.end:    # if list is empty
            self.add_at_head(*values)
        else:
            for val in values:
                self.end.next = Node(val)
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
            for val in values[::-1]:
                temp = self._get(index - 1)
                node = Node(val, temp.next)
                temp.next = node
            self._length += len(values)
        else:
            raise IndexError

    def delete_at_index(self, index):
        """
        Delete the index-th node in a linked list, if the index is valid.
        :param index: the node index
        :return:
        """
        if 0 <= index < len(self):
            if len(self) == 1:
                self.root = None
                self.end = None
            elif index == 0:
                self.root = self.root.next
            elif index == len(self) - 1:
                self.end = self._get(len(self) - 2)
                self.end.next = None
            else:
                temp = self._get(index - 1)
                temp.next = temp.next.next
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
        Remove the last node  from a linked list and return its value.
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
        if not isinstance(index, int):
            raise TypeError
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
        temp = self.root
        for i in range(index):
            temp = temp.next
        return temp

    def __len__(self):  # len(list)
        return self._length

    def __iter__(self): # for i in list
        for i in range(len(self)):
            yield (self._get(i)).val

    def __getitem__(self, item):    # list[index], list[i:j:k]
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
        result = Linked_List(*first)
        result.add_at_tail(*second)
        return result

    def __str__(self):  #   str(list)
        return ' -> '.join(str(i) for i in self)
