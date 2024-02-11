class DoublyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.previous = None
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __str__(self):
        return "->".join([str(item) for item in self])

    def __len__(self):
        return self.size

    def insert_at_head(self, data):
        self.insert_at_nth(0, data)

    def insert_at_tail(self, data):
        self.insert_at_nth(self.size, data)

    def insert_at_nth(self, index: int, data):
        if not 0 <= index <= self.size:
            raise IndexError("list index out of range")
        new_node = self.Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        elif index == self.size:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            new_node.previous = temp.previous
            new_node.next = temp
            temp.previous.next = new_node
            temp.previous = new_node
        self.size += 1

    def delete_head(self):
        return self.delete_at_nth(0)

    def delete_tail(self):
        return self.delete_at_nth(self.size - 1)

    def delete_at_nth(self, index: int):
        if not 0 <= index < self.size:
            raise IndexError("list index out of range")
        delete_node = self.head
        if self.size == 1:
            self.head = self.tail = None
        elif index == 0:
            self.head = self.head.next
            self.head.previous = None
        elif index == self.size - 1:
            delete_node = self.tail
            self.tail = self.tail.previous
            self.tail.next = None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            delete_node = temp
            temp.previous.next = temp.next
            temp.next.previous = temp.previous
        self.size -= 1
        return delete_node.data

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    return self.delete_head()
                elif current == self.tail:
                    return self.delete_tail()
                else:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                    self.size -= 1
                    return data
            current = current.next
        raise ValueError("No data matching given value")

    def is_empty(self):
        return self.size == 0


def test_doubly_linked_list():
    linked_list = DoublyLinkedList()
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
        linked_list.insert_at_nth(i, i + 1)
    assert str(linked_list) == "->".join(str(i) for i in range(1, 11))

    linked_list.insert_at_head(0)
    linked_list.insert_at_tail(11)
    assert str(linked_list) == "->".join(str(i) for i in range(12))

    assert linked_list.delete_head() == 0
    assert linked_list.delete_at_nth(9) == 10
    assert linked_list.delete_tail() == 11
    assert len(linked_list) == 9
    assert str(linked_list) == "->".join(str(i) for i in range(1, 10))


if __name__ == "__main__":
    test_doubly_linked_list()
