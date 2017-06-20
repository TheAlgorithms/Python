'''
A binary search Tree
'''
class Node:

    def __init__(self, label):
        self.label = label
        self.left = None
        self.rigt = None

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


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, label):

        #Create a new Node

        node = Node(label)

        if self.empty():
            self.root = node
        else:
            dad_node = None
            curr_node = self.root

            while True:
                if curr_node != None:

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
                    break

    def empty(self):
        if self.root == None:
            return True
        return False

    def preShow(self, curr_node):
        if curr_node != None:
            print(curr_node.getLabel(), end=" ")

            self.preShow(curr_node.getLeft())
            self.preShow(curr_node.getRight())

    def getRoot(self):
        return self.root

