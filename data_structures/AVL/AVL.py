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

    def getRight(self):
        return self.rigt

    def setRight(self, right):
        self.rigt = right

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

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
                        dad_node.setHeight(dad_node.getHeight() + 1)
                    else:
                        dad_node.setRight(node)
                        dad_node.setHeight(dad_node.getHeight() + 1)
                    break

    def rebalance(self, node):
        height_right = 0
        height_left = 0

        if node.getRight() is not None:
            height_right = node.getRight().getHeight()

        if node.getLeft() is not None:
            height_left = node.getLeft().getHeight()

        if abs(height_left - height_right) > 1:
            if height_left > height_right:
                right_child = node.getRight()
                if (right_child.getLeft().getHeight() >
                        right_child.getRight().getHeight()):
                    self.rotate_left(node)
                else:
                    self.double_rotate_right(node)
            else:
                left_child = node.getLeft()
                if (left_child.getLeft().getHeight() >
                        left_child.getRight().getHeight()):
                    self.double_rotate_left(node)
                else:
                    self.rotate_right(node)

    def rotate_left(self, node):
        # TODO: is this pythonic enought?
        aux = node.getLabel()
        node = aux.getRight()
        node.setHeight(node.getHeight() - 1)
        node.setLeft(Node(aux))
        node.getLeft().setHeight(node.getHeight() + 1)
        node.getRight().setHeight(node.getRight().getHeight() - 1)

    def rotate_right(self, node):
        aux = node.getLabel()
        node = aux.getLeft()
        node.setHeight(node.getHeight() - 1)
        node.setRight(Node(aux))
        node.getLeft().setHeight(node.getHeight() + 1)
        node.getLeft().setHeight(node.getLeft().getHeight() - 1)

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

    def getRoot(self):
        return self.root

t = AVL()
t.insert(11)
t.insert(14)
t.insert(3)
t.insert(4)
t.insert(5)
t.insert(6)
t.insert(7)
t.insert(8)
t.insert(9)
t.insert(10)
t.insert(1)
t.insert(12)
t.insert(13)
t.insert(2)
t.insert(15)
t.preShow(t.getRoot())
