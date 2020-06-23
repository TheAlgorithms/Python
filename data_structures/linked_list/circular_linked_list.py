from typing import Any


class Node:
    """
    Class to represent a single node.

    Each node has following attributes
    * data
    * next_ptr
    """

    def __init__(self, data: Any):
        self.data = data
        self.next_ptr = None


class CircularLinkedList:
    """
    Class to represent the CircularLinkedList.

    CircularLinkedList has following attributes.
    * head
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
        >>> cll.prepend(0)
        >>> len(cll)
        2
        >>> cll.delete_front()
        >>> len(cll)
        1
        >>> cll.delete_rear()
        >>> len(cll)
        0
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

        results = [current_node.data]
        current_node = current_node.next_ptr

        while current_node != self.head:
            results.append(current_node.data)
            current_node = current_node.next_ptr

        return " => ".join(f"<Node data={result}>" for result in results)

    def append(self, data: Any) -> None:
        """
        Adds a node with given data to the end of the CircularLinkedList
        >>> cll = CircularLinkedList()
        >>> cll.append(1)
        >>> print(f"{len(cll)}: {cll}")
        1: <Node data=1>
        >>> cll.append(2)
        >>> print(f"{len(cll)}: {cll}")
        2: <Node data=1> => <Node data=2>
        """
        current_node = self.head

        new_node = Node(data)
        new_node.next_ptr = new_node

        if current_node:
            while current_node.next_ptr != self.head:
                current_node = current_node.next_ptr

            current_node.next_ptr = new_node
            new_node.next_ptr = self.head
        else:
            self.head = new_node

        self.length += 1

    def prepend(self, data: Any) -> None:
        """
        Adds a ndoe with given data to the front of the CircularLinkedList
        >>> cll = CircularLinkedList()
        >>> cll.prepend(1)
        >>> cll.prepend(2)
        >>> print(f"{len(cll)}: {cll}")
        2: <Node data=2> => <Node data=1>
        """
        current_node = self.head

        new_node = Node(data)
        new_node.next_ptr = new_node

        if current_node:
            while current_node.next_ptr != self.head:
                current_node = current_node.next_ptr

            current_node.next_ptr = new_node
            new_node.next_ptr = self.head

        self.head = new_node
        self.length += 1

    def delete_front(self) -> None:
        """
        Removes the 1st node from the CircularLinkedList
        >>> cll = CircularLinkedList()
        >>> cll.delete_front()
        Traceback (most recent call last):
        ...
        IndexError: Deleting from an empty list
        >>> cll.append(1)
        >>> cll.append(2)
        >>> print(f"{len(cll)}: {cll}")
        2: <Node data=1> => <Node data=2>
        >>> cll.delete_front()
        >>> print(f"{len(cll)}: {cll}")
        1: <Node data=2>
        >>> cll.delete_front()
        >>> print(f"{len(cll)}: {cll}")
        0: Empty linked list
        """
        if not self.head:
            raise IndexError("Deleting from an empty list")

        current_node = self.head

        if current_node.next_ptr == current_node:
            self.head = None
        else:
            while current_node.next_ptr != self.head:
                current_node = current_node.next_ptr

            current_node.next_ptr = self.head.next_ptr
            self.head = self.head.next_ptr

        self.length -= 1
        if not self.head:
            assert self.length == 0

    def delete_rear(self) -> None:
        """
        Removes the last node from the CircularLinkedList
        >>> cll = CircularLinkedList()
        >>> cll.delete_rear()
        Traceback (most recent call last):
        ...
        IndexError: Deleting from an empty list
        >>> cll.append(1)
        >>> cll.append(2)
        >>> print(f"{len(cll)}: {cll}")
        2: <Node data=1> => <Node data=2>
        >>> cll.delete_rear()
        >>> print(f"{len(cll)}: {cll}")
        1: <Node data=1>
        >>> cll.delete_rear()
        >>> print(f"{len(cll)}: {cll}")
        0: Empty linked list
        """
        if not self.head:
            raise IndexError("Deleting from an empty list")

        temp_node, current_node = self.head, self.head

        if current_node.next_ptr == current_node:
            self.head = None
        else:
            while current_node.next_ptr != self.head:
                temp_node = current_node
                current_node = current_node.next_ptr

            temp_node.next_ptr = current_node.next_ptr

        self.length -= 1
        if not self.head:
            assert self.length == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
