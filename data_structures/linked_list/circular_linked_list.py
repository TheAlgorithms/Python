import typing


class Node:
    """
    Class to represent a single node.

    Each node has following attributes
    * data
    * next_ptr
    """

    def __init__(self, data: typing.Any):
        self.data = data
        self.next_ptr = None

    def set_data(self, value: typing.Any):
        """
        Set the data field of the node to given value.
        >>> node = Node(1)
        >>> node.set_data(2)
        >>> node.get_data()
        2
        """
        self.data = value

    def get_data(self) -> typing.Any:
        """
        Returns the data field of the current node.
        >>> node = Node(1)
        >>> node.get_data()
        1
        """
        return self.data

    def set_next(self, value: typing.Type['Node']):
        """
        Sets the next pointer of the current node.
        >>> node, node1 = Node(1), Node(2)
        >>> node.set_next(node1)
        >>> node.get_next().get_data()
        2
        """
        self.next_ptr = value

    def get_next(self) -> typing.Type['Node']:
        """
        Returns the next pointer of the current node.
        >>> node = Node(1)
        >>> node.get_next() is None
        True
        """
        return self.next_ptr

    def has_next(self) -> bool:
        """
        Checks if the current node has a valid next node.
        >>> node = Node(1)
        >>> node.has_next()
        False
        """
        return self.next_ptr is not None


class CircularLinkedList:
    """
    Class to represent the CircularLinkedList.

    CircularLinkedList has following attributes.
    * HEAD
    * length
    """

    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self) -> int:
        """
        Dunder method to return length of the CircularLinkedList
        >>> cll = CircularLinkedList()
        >>> len(cll)
        0
        >>> cll.append(1)
        >>> len(cll)
        1
        """
        return self.length

    def __str__(self) -> str:
        """
        Dunder method to represent the string representation of the CircularLinkedList
        >>> cll = CircularLinkedList()
        >>> print(cll)
        Empty linked list
        >>> cll.append(1)
        >>> cll.append(2)
        >>> print(cll)
        <Node data=1> => <Node data=2>
        """
        current_node = self.head
        if not current_node:
            return "Empty linked list"

        result = [f"<Node data={current_node.get_data()}>"]
        current_node = current_node.get_next()

        while current_node != self.head:
            result.append(f"<Node data={current_node.get_data()}>")
            current_node = current_node.get_next()

        return " => ".join(result)

    def append(self, data: typing.Any):
        """
        Adds a node with given data to the end of the CircularLinkedList
        >>> cll = CircularLinkedList()
        >>> cll.append(1)
        >>> cll.append(2)
        >>> len(cll)
        2
        >>> print(cll)
        <Node data=1> => <Node data=2>
        """
        current_node = self.head

        new_node = Node(data)
        new_node.set_next(new_node)

        if current_node is None:
            self.head = new_node
        else:
            while current_node.get_next() != self.head:
                current_node = current_node.get_next()

            current_node.set_next(new_node)
            new_node.set_next(self.head)

        self.length += 1

    def prepend(self, data: typing.Any):
        """
        Adds a ndoe with given data to the front of the CircularLinkedList
        >>> cll = CircularLinkedList()
        >>> cll.prepend(1)
        >>> cll.prepend(2)
        >>> len(cll)
        2
        >>> print(cll)
        <Node data=2> => <Node data=1>
        """
        current_node = self.head

        new_node = Node(data)
        new_node.set_next(new_node)

        if current_node is None:
            self.head = new_node
        else:
            while current_node.get_next() != self.head:
                current_node = current_node.get_next()

            current_node.set_next(new_node)
            new_node.set_next(self.head)

            self.head = new_node

        self.length += 1

    def delete_front(self):
        """
        Removes the 1st node from the CircularLinkedList
        >>> cll = CircularLinkedList()
        >>> for i in range(5)
        ...     cll.append(i)
        ...
        >>> print(cll)
        <Node data=0> => <Node data=1> => <Node data=2> => <Node data=3> => <Node data=4>
        >>> cll.delete_front()
        >>> print(cll)
        <Node data=1> => <Node data=2> => <Node data=3> => <Node data=4>
        """
        if self.head is None:
            raise IndexError()

        current_node = self.head

        if current_node.get_next() == current_node:
            self.head, self.length = None, 0
        else:
            while current_node.get_next() != self.head:
                current_node = current_node.get_next()

            current_node.set_next(self.head.get_next())
            self.head = self.head.get_next()

        self.length -= 1

    def delete_rear(self):
        """
        Removes the last node from the CircularLinkedList
        >>> cll = CircularLinkedList()
        >>> for i in range(5)
        ...     cll.append(i)
        ...
        >>> print(cll)
        <Node data=0> => <Node data=1> => <Node data=2> => <Node data=3> => <Node data=4>
        >>> cll.delete_rear()
        >>> print(cll)
        <Node data=0> => <Node data=1> => <Node data=2> => <Node data=3>
        """
        if self.head is None:
            raise IndexError()

        temp_node, current_node = self.head, self.head

        if current_node.get_next() == current_node:
            self.head, self.length = None, 0
        else:
            while current_node.get_next() != self.head:
                temp_node = current_node
                current_node = current_node.get_next()

            temp_node.set_next(current_node.get_next())

        self.length -= 1
