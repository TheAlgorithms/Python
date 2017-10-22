'''
A binary search Tree
'''

class Node:

    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, label):
        # Create a new Node
        new_node = Node(label)
        # If Tree is empty
        if self.empty():
            self.root = new_node
        else:
            #If Tree is not empty
            parent_node = None
            curr_node = self.root
            #While we don't get to a leaf
            while curr_node is not None:
                #We keep reference of the parent node
                parent_node = curr_node
                #If node label is less than current node
                if new_node.getLabel() < curr_node.getLabel():
                #We go left
                    curr_node = curr_node.getLeft()
                else:
                    #Else we go right
                    curr_node = curr_node.getRight()
            #We insert the new node in a leaf
            if new_node.getLabel() < parent_node.getLabel():
                parent_node.setLeft(new_node)
            else:
                parent_node.setRight(new_node)        
    
    def getNode(self, label):
        curr_node = None
        #If the tree is not empty
        if(not self.empty()):
            #Get tree root
            curr_node = self.getRoot()
            #While we don't find the node we look for
            #I am using lazy evaluation here to avoid NoneType Attribute error
            while curr_node is not None and curr_node.getLabel() is not label:
                #If node label is less than current node
                if label < curr_node.getLabel():
                    #We go left
                    curr_node = curr_node.getLeft()
                else:
                    #Else we go right
                    curr_node = curr_node.getRight()
        return curr_node

    def empty(self):
        if self.root is None:
            return True
        return False

    def preShow(self, curr_node):
        if curr_node is not None:
            print(curr_node.getLabel())
            self.preShow(curr_node.getLeft())
            self.preShow(curr_node.getRight())

    def getRoot(self):
        return self.root

'''
Example
            8
           / \
          3   10
         / \    \
        1   6    14
           / \   /
          4   7 13 
'''


if __name__ == "__main__":
    t = BinarySearchTree()
    t.insert(8)
    t.insert(3)
    t.insert(1)
    t.insert(6)
    t.insert(4)
    t.insert(7)
    t.insert(10)
    t.insert(14)
    t.insert(13)

    t.preShow(t.getRoot())

    if(t.getNode(6) is not None):
        print("The label 6 exists")
    else:
        print("The label 6 doesn't exist")

    if(t.getNode(-1) is not None):
        print("The label -1 exists")
    else:
        print("The label -1 doesn't exist")
    
