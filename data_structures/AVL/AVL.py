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

    def getHeight(self, height):
        return self.height


class AVL:

    def __init__(self):
        self.root = None
        self.size = 0

    # def __init__(self, root):
    #     self.root = root
    #     self.size = 1

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

                        if (dad_node.getRight().getHeight() -
                                dad_node.getLeft.getHeight() > 1):
                            self.rebalance(dad_node)

                    else:
                        dad_node.setRight(node)
                        dad_node.setHeight(dad_node.getHeight() + 1)

                        if (dad_node.getRight().getHeight() -
                                dad_node.getLeft.getHeight() > 1):
                            self.rebalance(dad_node)
                    break

    def rebalance(self, node):
        pass

    def rotate_left(self, node):
        pass

    def rotate_right(self, node):
        pass

    def double_rotate_left(self, node):
        pass

    def double_rotate_righs(self, node):
        pass
