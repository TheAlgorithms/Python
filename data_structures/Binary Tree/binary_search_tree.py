'''
A binary search Tree
'''
class Node:

    def __init__(self, label, parent):
        self.label = label
        self.left = None
        self.right = None
        #Added in order to delete a node easier
        self.parent = parent

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

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, label):
        # Create a new Node
        new_node = Node(label, None)
        # If Tree is empty
        if self.empty():
            self.root = new_node
        else:
            #If Tree is not empty
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
            #Set parent to the new node
            new_node.setParent(parent_node)      
    
    def delete(self, label):
        if (not self.empty()):
            #Look for the node with that label
            node = self.getNode(label)
            #If the node exists
            if(node is not None):
                #If it has no children
                if(node.getLeft() is None and node.getRight() is None):
                    self.__reassignNodes(node, None)
                    node = None
                #Has only right children
                elif(node.getLeft() is None and node.getRight() is not None):
                    self.__reassignNodes(node, node.getRight())
                #Has only left children
                elif(node.getLeft() is not None and node.getRight() is None):
                    self.__reassignNodes(node, node.getLeft())
                #Has two children
                else:
                    tmpNode = self.getMax(node.getLeft())
                    self.delete(tmpNode.getLabel())
                    self.__reassignNodes(node, tmpNode)
    
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

    def getMax(self, root = None):
        if(root is not None):
            curr_node = root
        else:
            #We go deep on the right branch
            curr_node = self.getRoot()
        if(not self.empty()):
            while(curr_node.getRight() is not None):
                curr_node = curr_node.getRight()
        return curr_node

    def getMin(self, root = None):
        if(root is not None):
            curr_node = root
        else:
            #We go deep on the left branch
            curr_node = self.getRoot()
        if(not self.empty()):
            curr_node = self.getRoot()
            while(curr_node.getLeft() is not None):
                curr_node = curr_node.getLeft()
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

    def __isRightChildren(self, node):
        if(node == node.getParent().getRight()):
            return True
        return False

    def __reassignNodes(self,node, newChildren):
        if(newChildren is not None):
            newChildren.setParent(node.getParent())
        if(node.getParent() is not None):
            #If it is the Right Children
            if(self.__isRightChildren(node)):a
                    node.getParent().setRight(newChildren)
            else:
                #Else it is the left children
                node.getParent().setLeft(newChildren)
        else:
            #It is the root of the tree
            node.setLabel(newChildren.getLabel())

def testBinarySearchTree():
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

    '''
    Example After Deletion
                  7
                 / \
                3   14
               / \    
              1   6    
                 /   
                4   
    '''
    t = BinarySearchTree()
    t.insert(8)
    t.insert(3)
    t.insert(10)
    t.insert(6)
    t.insert(1)
    t.insert(10)
    t.insert(14)
    t.insert(13)
    t.insert(4)
    t.insert(7)

    t.preShow(t.getRoot())

    if(t.getNode(6) is not None):
        print("The label 6 exists")
    else:
        print("The label 6 doesn't exist")

    if(t.getNode(-1) is not None):
        print("The label -1 exists")
    else:
        print("The label -1 doesn't exist")
    
    if(not t.empty()):
        print("Max Value: ", t.getMax().getLabel())
        print("Min Value: ", t.getMin().getLabel())
    
    t.delete(13)
    t.delete(10)
    t.delete(8)

    t.preShow(t.getRoot())

if __name__ == "__main__":
    testBinarySearchTree()
