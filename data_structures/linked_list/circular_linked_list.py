class Node:
    """
    Class to represent a single node.

    Each node has following attributes
    * data
    * next_ptr
    """

    def __init__(self, data):
        self.data = data
        self.next_ptr = None

    def set_data(self, value):
        """
        Set the data field of the node to given value.
        """
        self.data = value

    def get_data(self):
        """
        Returns the data field of the current node,
        """
        return self.data

    def set_next(self, value):
        """
        Sets the next pointer of the current node.
        """
        self.next_ptr = value

    def get_next(self):
        """
        Returns the next pointer of the current node.
        """
        return self.next_ptr

    def has_next(self):
        """
        Checks if the current node has a valid next node.
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

    def __len__(self):
        """
        Dunder method to return length of the CircularLinkedList
        """
        return self.length

    def __str__(self):
        """
        Dunder method to represent the string representation of the CircularLinkedList
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

    def append(self, data):
        """
        Adds a node with given data to the end of the CircularLinkedList
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

    def prepend(self, data):
        """
        Adds a ndoe with given data to the front of the CircularLinkedList
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
