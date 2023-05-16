class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0  # New attribute to track length

    def __iter__(self) -> Iterator[Any]:
        node = self.head
        while self.head:
            yield node.data
            node = node.next
            if node == self.head:
                break

    def __len__(self) -> int:
        return self.length

    # ... Rest of the code ...

    def insert_tail(self, data: Any) -> None:
        self.insert_nth(self.length, data)  # Update length instead of calling len(self)

    def insert_head(self, data: Any) -> None:
        self.insert_nth(0, data)  # Update length instead of calling len(self)

    def insert_nth(self, index: int, data: Any) -> None:
        if index < 0 or index > self.length:  # Update length check
            raise IndexError("list index out of range.")
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.tail = self.head = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = self.tail.next = new_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            if index == self.length:  # Update length check
                self.tail = new_node
        self.length += 1  # Update length

    def delete_front(self):
        return self.delete_nth(0)

    def delete_tail(self) -> Any:
        return self.delete_nth(self.length - 1, update_length=True)  # Update length instead of calling len(self)

    def delete_nth(self, index: int = 0, update_length: bool = False) -> Any:
        if not 0 <= index < self.length:  # Update length check
            raise IndexError("list index out of range.")
        delete_node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        elif index == 0:
            self.tail.next = self.tail.next.next
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            delete_node = temp.next
            temp.next = temp.next.next
            if index == self.length - 1:  # Update length check
                self.tail = temp
        if update_length:
            self.length -= 1  # Update length
        return delete_node.data

    def is_empty(self) -> bool:
        return self.length == 0
