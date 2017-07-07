'''
A AVL tree
'''


class Node:

    def __init__(self, label):
        self.label = label
        self.left = None
        self.rigt = None
        self.parent = None
        self.height = 0

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left
        self.left.setParent(self)
        self.left.setHeight(self.height + 1)
        
    def getRight(self):
        return self.rigt

    def setRight(self, right):
        self.rigt = right
        self.rigt.setParent(self)
        self.rigt.setHeight(self.height + 1)

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent
        self.height = (self.parent.getHeight() + 1 if
                        (self.parent is not None) else 0)

    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height


class AVL:

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            self.root.setHeight(0)
            self.size = 1
        else:
            # Same as Binary Tree
            dad_node = None
            curr_node = self.root

            while True:
                if curr_node is not None:

                    dad_node = curr_node

                    if node.getLabel() < curr_node.getLabel():
                        curr_node = curr_node.getLeft()
                    else:
                        curr_node = curr_node.getRight()
                else:
                    if node.getLabel() < dad_node.getLabel():
                        dad_node.setLeft(node)
                    else:
                        dad_node.setRight(node)
                    self.rebalance(dad_node)
                    break

    def rebalance(self, node):
        height_right = 0
        height_left = 0
        n = node
        while n is not None:
            height_right = 0
            height_left = 0

            if node.getRight() is not None:
                height_right = node.getRight().getHeight()

            if node.getLeft() is not None:
                height_left = node.getLeft().getHeight()

            if abs(height_left - height_right) > 1:
                if height_left > height_right:
                    left_child = node.getRight()
                    if ():
                        self.rotate_left(n)
                        break
                    else:
                        self.double_rotate_right(n)
                        break
                else:
                    right_child = node.getRight()
                    if right_child is not None:
                        h_right = (right_child.getRight().getHeight()
                            if (right_child.getRight() is not None) else 0)
                        h_left = (right_child.getLeft().getHeight()
                            if (right_child.getLeft() is not None) else 0)

                    if (h_left > h_right):
                        self.double_rotate_left(n)
                        break
                    else:
                        self.rotate_right(n)
                        print(n.getLabel())
                        break
            n = n.getParent()

    def rotate_left(self, node):
        pass

    def rotate_right(self, node):
        n = Node(node.getLabel())
        n.setRight(node.getRight())
        n.setLeft(Node(node.getParent().getLabel()))
        node = n

    def double_rotate_left(self, node):
        self.rotate_right(node.getRight().getRight())
        self.rotate_left(node)

    def double_rotate_right(self, node):
        self.rotate_left(node.getLeft().getLeft())
        self.rotate_right(node)

    def empty(self):
        if self.root is None:
            return True
        return False

    def preShow(self, curr_node):
        if curr_node is not None:
            self.preShow(curr_node.getLeft())
            print(curr_node.getLabel(), end=" ")
            self.preShow(curr_node.getRight())

    def preorden(self, curr_node):
        if curr_node is not None:
            self.preShow(curr_node.getLeft())
            self.preShow(curr_node.getRight())
            print(curr_node.getLabel(), end=" ")

    def getRoot(self):
        return self.root

t = AVL()
# t.insert(1)
# t.preShow(t.getRoot())
# print("\n")
# t.preorden(t.getRoot())
# print("\n")
# t.insert(2)
# t.preShow(t.getRoot())
# print("\n")
# t.preorden(t.getRoot())
# print("\n")
# t.insert(3)
# t.preShow(t.getRoot())
# print("\n")
# t.preorden(t.getRoot())
# print("\n")
# print(t.getRoot().getHeight())
# print(t.getRoot().getRight().getHeight())
t.insert(1)
t.insert(2)
t.insert(3)
# t.insert(4)
# t.preShow(t.getRoot())
# print("\n")
# t.preorden(t.getRoot())
# print("\n")
# t.insert(5)
# t.preShow(t.getRoot())
# print("\n")
# t.preorden(t.getRoot())
# print("\n")
# t.insert(6)
# t.preShow(t.getRoot())
# print("\n")
# t.preorden(t.getRoot())
# print("\n")
# t.insert(7)
# t.preShow(t.getRoot())
# print("\n")
# t.preorden(t.getRoot())
# print("\n")
# t.insert(8)
# t.preShow(t.getRoot())
# print("\n")
# t.preorden(t.getRoot())
# print("\n")
# t.insert(9)
# t.preShow(t.getRoot())
# print("\n")
# t.preorden(t.getRoot())
# print("\n")
# t.insert(10)
# t.preShow(t.getRoot())
# print("\n")
# t.preorden(t.getRoot())
# print("\n")
# t.insert(11)
# t.preShow(t.getRoot())
# print("\n")
# t.preorden(t.getRoot())
# print("\n")
# t.insert(12)
# t.preShow(t.getRoot())
# print("\n")
# t.preorden(t.getRoot())
# print("\n")
# t.insert(13)
# t.preShow(t.getRoot())
# print("\n")
# t.preorden(t.getRoot())
# print("\n")
# t.insert(14)
# t.preShow(t.getRoot())
# print("\n")
# t.preorden(t.getRoot())
# print("\n")
# t.insert(15)
# t.preShow(t.getRoot())
# print("\n")
# t.preorden(t.getRoot())
