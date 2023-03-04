"""
- A linked list is similar to an array, it holds values. However, links in a linked
    list do not have indexes.
- This is an example of a double ended, doubly linked list.
- Each link references the next link and the previous one.
- A Doubly Linked List (DLL) contains an extra pointer, typically called previous
    pointer, together with next pointer and data which are there in singly linked list.
 - Advantages over SLL - It can be traversed in both forward and backward direction.
     Delete operation is more efficient
"""


class Node:
    def __init__(self, data: int, previous=None, next_node=None):
        self.data = data
        self.previous = previous
        self.next = next_node

    def __str__(self) -> str:
        return f"{self.data}"

    def get_data(self) -> int:
        return self.data

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous


class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            value = self.current.get_data()
            self.current = self.current.get_next()
            return value


class LinkedList:
    def __init__(self):
        self.head = None  # First node in list
        self.tail = None  # Last node in list

    def __str__(self):
        current = self.head
        nodes = []
        while current is not None:
            nodes.append(current.get_data())
            current = current.get_next()
        return " ".join(str(node) for node in nodes)

    def __contains__(self, value: int):
        current = self.head
        while current:
            if current.get_data() == value:
                return True
            current = current.get_next()
        return False

    def __iter__(self):
        return LinkedListIterator(self.head)

    def get_head_data(self):
        if self.head:
            return self.head.get_data()
        return None

    def get_tail_data(self):
        if self.tail:
            return self.tail.get_data()
        return None

    def set_head(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.insert_before_node(self.head, node)

    def set_tail(self, node: Node) -> None:
        if self.head is None:
            self.set_head(node)
        else:
            self.insert_after_node(self.tail, node)

    def insert(self, value: int) -> None:
        node = Node(value)
        if self.head is None:
            self.set_head(node)
        else:
            self.set_tail(node)

    def insert_before_node(self, node: Node, node_to_insert: Node) -> None:
        node_to_insert.next = node
        node_to_insert.previous = node.previous

        if node.get_previous() is None:
            self.head = node_to_insert
        else:
            node.previous.next = node_to_insert

        node.previous = node_to_insert

    def insert_after_node(self, node: Node, node_to_insert: Node) -> None:
        node_to_insert.previous = node
        node_to_insert.next = node.next

        if node.get_next() is None:
            self.tail = node_to_insert
        else:
            node.next.previous = node_to_insert

        node.next = node_to_insert

    def insert_at_position(self, position: int, value: int) -> None:
        current_position = 1
        new_node = Node(value)
        node = self.head
        while node:
            if current_position == position:
                self.insert_before_node(node, new_node)
                return
            current_position += 1
            node = node.next
        self.insert_after_node(self.tail, new_node)

    def get_node(self, item: int) -> Node:
        node = self.head
        while node:
            if node.get_data() == item:
                return node
            node = node.get_next()
        raise Exception("Node not found")

    def delete_value(self, value):
        if (node := self.get_node(value)) is not None:
            if node == self.head:
                self.head = self.head.get_next()

            if node == self.tail:
                self.tail = self.tail.get_previous()

            self.remove_node_pointers(node)

    @staticmethod
    def remove_node_pointers(node: Node) -> None:
        if node.get_next():
            node.next.previous = node.previous

        if node.get_previous():
            node.previous.next = node.next

        node.next = None
        node.previous = None

    def is_empty(self):
        return self.head is None


def create_linked_list() -> None:
    """
    >>> new_linked_list = LinkedList()
    >>> new_linked_list.get_head_data() is None
    True
    >>> new_linked_list.get_tail_data() is None
    True
    >>> new_linked_list.is_empty()
    True
    >>> new_linked_list.insert(10)
    >>> new_linked_list.get_head_data()
    10
    >>> new_linked_list.get_tail_data()
    10
    >>> new_linked_list.insert_at_position(position=3, value=20)
    >>> new_linked_list.get_head_data()
    10
    >>> new_linked_list.get_tail_data()
    20
    >>> new_linked_list.set_head(Node(1000))
    >>> new_linked_list.get_head_data()
    1000
    >>> new_linked_list.get_tail_data()
    20
    >>> new_linked_list.set_tail(Node(2000))
    >>> new_linked_list.get_head_data()
    1000
    >>> new_linked_list.get_tail_data()
    2000
    >>> for value in new_linked_list:
    ...    print(value)
    1000
    10
    20
    2000
    >>> new_linked_list.is_empty()
    False
    >>> for value in new_linked_list:
    ...    print(value)
    1000
    10
    20
    2000
    >>> 10 in new_linked_list
    True
    >>> new_linked_list.delete_value(value=10)
    >>> 10 in new_linked_list
    False
    >>> new_linked_list.delete_value(value=2000)
    >>> new_linked_list.get_tail_data()
    20
    >>> new_linked_list.delete_value(value=1000)
    >>> new_linked_list.get_tail_data()
    20
    >>> new_linked_list.get_head_data()
    20
    >>> for value in new_linked_list:
    ...    print(value)
    20
    >>> new_linked_list.delete_value(value=20)
    >>> for value in new_linked_list:
    ...    print(value)
    >>> for value in range(1,10):
    ...    new_linked_list.insert(value=value)
    >>> for value in new_linked_list:
    ...    print(value)
    1
    2
    3
    4
    5
    6
    7
    8
    9
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
