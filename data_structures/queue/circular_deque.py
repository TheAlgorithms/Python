class MyCircularDeque:
    """
    Doubly-linklist implementation of Deque
    Deque is a double ended queue which can
    insert, remove and get in front element in: O(1)
    insert, remove and get in back element in: O(1)
    """

    class Node:
        def __init__(self, value):
            self.value = value
            self.previous = self.next = None

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.dummyRoot = self.Node(None)
        self.connect(self.dummyRoot, self.dummyRoot)

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        node = self.Node(value)
        self.connect(node, self.dummyRoot.next)
        self.connect(self.dummyRoot, node)
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        node = self.Node(value)
        self.connect(self.dummyRoot.previous, node)
        self.connect(node, self.dummyRoot)
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.connect(self.dummyRoot, self.dummyRoot.next.next)
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.connect(self.dummyRoot.previous.previous, self.dummyRoot)
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.dummyRoot.next.value

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.dummyRoot.previous.value

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

    def connect(self, node: Node, following: Node) -> None:
        node.next = following
        following.previous = node


def main():
    circularDeque = MyCircularDeque(3)

    print(circularDeque.insertLast(1))
    print(circularDeque.insertLast(2))
    print(circularDeque.insertFront(3))
    print(circularDeque.insertFront(4))
    print(circularDeque.getRear())
    print(circularDeque.isFull())
    print(circularDeque.deleteLast())
    print(circularDeque.insertFront(4))
    print(circularDeque.getFront())


if __name__ == "__main__":
    main()
