class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"{self.data}"


class LinkedList:
    def __init__(self):
        self.head = None  # initialize head to None
        self.size = 0  # length of linked list

    def insert_tail(self, data) -> None:
        self.insert_nth(self.size, data)

    def insert_head(self, data) -> None:
        self.insert_nth(0, data)

    def insert_nth(self, index: int, data) -> None:
        if index < 0 or index > self.size:  # test if index is valid.
            raise IndexError("list index out of range.")
        new_node = Node(data)  # create a new node
        if self.head is None:
            self.head = new_node
        elif index == 0:
            new_node.next = self.head  # link new_node to head
            self.head = new_node  # make NewNode as head
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.size += 1

    def print_list(self) -> None:  # print every node data
        print(self)

    def delete_head(self):  # delete from head
        return self.delete_nth(0)

    def delete_tail(self):  # delete from tail
        return self.delete_nth(self.size - 1)

    def delete_nth(self, index: int):
        if index < 0 or index > self.size - 1:  # test if index is valid
            raise IndexError("list index out of range.")
        delete_node = self.head  # default first node
        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            delete_node = temp.next
            temp.next = temp.next.next
        self.size -= 1
        return delete_node.data

    def is_empty(self) -> bool:
        return self.head is None  # return True if head is none

    def reverse(self):
        prev = None
        current = self.head

        while current:
            # Store the current node's next node.
            next_node = current.next
            # Make the current node's next point backwards
            current.next = prev
            # Make the previous node be the current node
            prev = current
            # Make the current node the next node (to progress iteration)
            current = next_node
        # Return prev in order to put the head at the end
        self.head = prev

    def __repr__(self):  # String representation/visualization of a Linked Lists
        current = self.head
        string_repr = []
        while current:
            string_repr.append(f"{current.data}")
            current = current.next
        return "->".join(string_repr)

    def __str__(self) -> str:
        return repr(self)

    # Indexing Support. Used to get a node at particular position
    def __getitem__(self, index):
        current = self.head

        # If LinkedList is empty
        if current is None:
            raise IndexError("The Linked List is empty")

        # Move Forward 'index' times
        for _ in range(index):
            # If the LinkedList ends before reaching specified node
            if current.next is None:
                raise IndexError("Index out of range.")
            current = current.next
        return current.data

    # Used to change the data of a particular node
    def __setitem__(self, index, data):
        current = self.head
        # If list is empty
        if current is None:
            raise IndexError("The Linked List is empty.")
        for i in range(index):
            if current.next is None:
                raise IndexError("Index out of range.")
            current = current.next
        current.data = data

    def __len__(self) -> int:
        """
        Return length of linked list i.e. number of nodes
        >>> linked_list = LinkedList()
        >>> len(linked_list)
        0
        >>> linked_list.insert_tail("head")
        >>> len(linked_list)
        1
        >>> linked_list.insert_head("head")
        >>> len(linked_list)
        2
        >>> _ = linked_list.delete_tail()
        >>> len(linked_list)
        1
        >>> _ = linked_list.delete_head()
        >>> len(linked_list)
        0
        """
        return self.size


def test_singly_linked_list() -> None:
    """
    >>> test_singly_linked_list()
    """
    linked_list = LinkedList()
    assert linked_list.is_empty() is True
    assert str(linked_list) == ""

    try:
        linked_list.delete_head()
        assert False  # This should not happen.
    except IndexError:
        assert True  # This should happen.

    try:
        linked_list.delete_tail()
        assert False  # This should not happen.
    except IndexError:
        assert True  # This should happen.

    for i in range(10):
        assert len(linked_list) == i
        linked_list.insert_nth(i, i + 1)
    assert str(linked_list) == "->".join(str(i) for i in range(1, 11))

    linked_list.insert_head(0)
    linked_list.insert_tail(11)
    assert str(linked_list) == "->".join(str(i) for i in range(0, 12))

    assert linked_list.delete_head() == 0
    assert linked_list.delete_nth(9) == 10
    assert linked_list.delete_tail() == 11
    assert str(linked_list) == "->".join(str(i) for i in range(1, 10))


def main():
    from doctest import testmod

    testmod()
    test_singly_linked_list()

    linked_list = LinkedList()
    linked_list.insert_head(input("Inserting 1st at head ").strip())
    linked_list.insert_head(input("Inserting 2nd at head ").strip())
    print("\nPrint list:")
    linked_list.print_list()
    linked_list.insert_tail(input("\nInserting 1st at tail ").strip())
    linked_list.insert_tail(input("Inserting 2nd at tail ").strip())
    print("\nPrint list:")
    linked_list.print_list()
    print("\nDelete head")
    linked_list.delete_head()
    print("Delete tail")
    linked_list.delete_tail()
    print("\nPrint list:")
    linked_list.print_list()
    print("\nReverse linked list")
    linked_list.reverse()
    print("\nPrint list:")
    linked_list.print_list()
    print("\nString representation of linked list:")
    print(linked_list)
    print("\nReading/changing Node data using indexing:")
    print(f"Element at Position 1: {linked_list[1]}")
    linked_list[1] = input("Enter New Value: ").strip()
    print("New list:")
    print(linked_list)
    print(f"length of linked_list is : {len(linked_list)}")


if __name__ == "__main__":
    main()
