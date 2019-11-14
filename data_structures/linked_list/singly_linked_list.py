from typing import Optional, Union, List


class Node:
    """A linked list element class."""

    def __init__(self, data: Union[int, float] = None, next: "Node" = None):
        self.val = data  # given data
        self.next = next  # given next


class Linked_List:
    """A linked list class, whose elements are instances of the Node class.

    Args:
        *values: 1 or more values of a list

    Attributes:
        root: the 1st element
        end: the last element
    """

    def __init__(self, *values: Union[int, float]):
        self.root = None
        self.end = None

        self.__length = 0  # length of the list

        self.add_at_head(*values)

    def add_at_head(self, *values: Union[int, float]):
        """Add a node(s) before the first element of a linked list.

        :param *values: 1 or more values of the node(s)
        """
        for val in values[::-1]:  # you can add many values
            node = Node(val, self.root)  # create a new node
            self.root = node
            if not self.root.next:
                self.end = self.root
        self.__length += len(values)  # increase the length

    def add_at_tail(self, *values: Union[int, float]):
        """Add a node(s) after the last element of a linked list.

        :param *values: 1 or more values of the node(s)
        """
        if not self.end:  # if list is empty
            self.add_at_head(*values)
        else:
            for val in values:
                self.end.next = Node(val)
                self.end = self.end.next
            self.__length += len(values)

    def add_at_index(self, index: int, *values: Union[int, float]):
        """Add a node(s) before the index-th node in a linked list.

        If the index equals to the length of the linked list, the node will be
        appended to the end of the linked list.

        :param index: the node index
        :param *values: 1 or more values of the node(s)
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
            self.__length += len(values)
        else:
            raise IndexError

    def delete_at_index(self, index: int):
        """Delete the index-th node in a linked list, if the index is valid.

        :param index: the node index
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
            self.__length -= 1
        else:
            raise IndexError

    def pop_root(self) -> Union[int, float, None]:
        """Remove the first node from a linked list and return its value.

        :return: the 1st node value
        """
        if not self:
            return None
        res = self.root.val
        self.delete_at_index(0)
        return res

    def pop_end(self) -> Union[int, float, None]:
        """Remove the last node  from a linked list and return its value.

        :return: the last node value
        """
        if len(self) < 2:
            return self.pop_root()
        res = self.end.val
        self.delete_at_index(len(self) - 1)
        return res

    def _get(self, index: int) -> Optional[Node]:
        """Get the index-th node in a linked list.

        :return: the index-th node
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

    def __len__(self) -> int:  # len(list)
        return self.__length

    def __iter__(self) -> Union[int, float, None]:  # for i in list
        for i in range(len(self)):
            yield (self._get(i)).val

    def __getitem__(
        self, item
    ) -> Union[int, float, List[Union[int, float]]]:  # list[index], list[i:j:k]
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

    def __setitem__(
        self, key: int, value: Union[int, float, None]
    ):  # list[key] = value
        (self._get(key)).val = value

    def __contains__(self, item: Union[int, float, None]) -> bool:  # if item in list
        temp = self.root
        while temp and temp.val != item:
            temp = temp.next
        return temp is not None

    def __add__(self, other: "Linked_List") -> "Linked_List":  # list1 + list2
        first = [i for i in self]
        second = [i for i in other]
        result = Linked_List(*first)
        result.add_at_tail(*second)
        return result

    def __str__(self) -> str:  # str(list)
        return " -> ".join(str(i) for i in self)
