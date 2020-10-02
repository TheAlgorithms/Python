class MyCircularDeque:
    class __Node:
        def __init__(self, value):
            self.value = value
            self.previous = self.next = None

    def __init__(self, k: int):
        self.__capacity = k
        self.__size = 0
        self.__dummyRoot = self.__Node(None)
        self.__connect(self.__dummyRoot, self.__dummyRoot)

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        node = self.__Node(value)
        self.__connect(node, self.__dummyRoot.next)
        self.__connect(self.__dummyRoot, node)
        self.__size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        node = self.__Node(value)
        self.__connect(self.__dummyRoot.previous, node)
        self.__connect(node, self.__dummyRoot)
        self.__size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.__connect(self.__dummyRoot, self.__dummyRoot.next.next)
        self.__size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.__connect(self.__dummyRoot.previous.previous, self.__dummyRoot)
        self.__size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.__dummyRoot.next.value

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.__dummyRoot.previous.value

    def isEmpty(self) -> bool:
        return self.__size == 0

    def isFull(self) -> bool:
        return self.__size == self.__capacity

    def __connect(self, node: __Node, following: __Node) -> None:
        node.next = following
        following.previous = node
