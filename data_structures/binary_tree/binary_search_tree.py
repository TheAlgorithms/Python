"""
A binary search Tree
"""

class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent    # Added in order to delete a node easier

    def get_data(self):
        return self.data

    def getleft(self):
        return self.left

    def getright(self):
        return self.right

    def getparent(self):
        return self.parent

    def setdata(self, data):
        self.data = data

    def setleft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def setparent(self, parent):
        self.parent = parent

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        """
            Return a string of all the Nodes. 
            In Order Traversal
        """
        nodelist = self.__InOrderTraversal(self.root)
        str = " ".join([repr(i.get_data()) for i in nodelist])
        return str

    def __InOrderTraversal(self, node):
        nodeList = list()
        if node is not None:
            nodeList.insert(0, node)    # Preorder Traversal
            nodeList = nodeList + self.__InOrderTraversal(node.getleft()) + self.__InOrderTraversal(node.getright())
        return nodeList

    def __isRightChildren(self, node):
        if(node == node.getparent().getright()):
            return True
        else:
            return False

    def __reassignNodes(self, node, newChildren):
        if(newChildren is not None):    # reset its kids
            newChildren.setparent(node.getparent())
        if(node.getparent() is not None):   # reset its parenst
            if(self.__isRightChildren(node)):   # If it is the Right Children
                node.getparent().setRight(newChildren)
            else:   # Else it is the left children
                node.getparent().setleft(newChildren)
        else:   # no parent => root
            self.root = newChildren

    def empty(self):
        if self.root is None:
            return True
        else:
            return False

    def insert(self, data):
        """
            Insert a new node in Binary Search Tree with value label
        """
        new_node = Node(data, None) # Create a new Node
        if self.empty():    # If Tree is empty
            self.root = new_node    # set its root
        else:   # If Tree is not empty
            parent_node = self.root # from root
            while True: # While we don't get to a leaf
                if data < parent_node.get_data():    # We go left
                    if parent_node.getleft() == None:
                        parent_node.setleft(new_node)   # We insert the new node in a leaf
                        break
                    else:
                        parent_node = parent_node.getleft()
                else:   # Else we go right
                    if parent_node.getright() == None:
                        parent_node.setRight(new_node)
                        break
                    else:
                        parent_node = parent_node.getright()
            new_node.setparent(parent_node) # Set parent to the new node

    def getNode(self, data):
        if self.empty():
            raise IndexError("Warning: Tree is empty! please use another. ")
        else:   # If the tree is not empty
            node = self.getRoot()
            while node is not None and node.get_data() is not data:    # using lazy evaluation here to avoid NoneType Attribute error
                if data < node.get_data():
                    node = node.getleft()   # We go left
                else:
                    node = node.getright()  # Else we go right
            return node

    def getRoot(self):
        return self.root

    def getMax(self, node = None):
        """
            We go deep on the right branch
        """
        if(node is None):
            node = self.getRoot()
        if(not self.empty()):
            while(node.getright() is not None):
                node = node.getright()
        return node

    def getMin(self, node = None):
        """
            We go deep on the left branch
        """
        if(node is None):
            node = self.getRoot()
        if(not self.empty()):
            node = self.getRoot()
            while(node.getleft() is not None):
                node = node.getleft()
        return node

    def delete(self, data):
        node = self.getNode(data)   # Look for the node with that label
        if(node is not None):
            if(node.getleft() is None and node.getright() is None): # If it has no children
                self.__reassignNodes(node, None)
                node = None
            elif(node.getleft() is None):   # Has only right children
                self.__reassignNodes(node, node.getright())
            elif(node.getright() is None):  # Has only left children
                self.__reassignNodes(node, node.getleft())
            else:   # Has two children
                tmpNode = self.getMax(node.getleft())   # Gets the max value of the left branch
                self.delete(tmpNode.get_data())
                node.setdata(tmpNode.get_data()) # Assigns the value to the node to delete and keesp tree structure

    def traversalTree(self, traversalFunction = None, root = None):
        """
            This function traversal the tree.
            You can pass a function to traversal the tree as needed by client code
        """
        if(traversalFunction is None):  # default
            return self.__InOrderTraversal(self.root)
        else:
            return traversalFunction(self.root)

def postOrder(curr_node):
    """
        postOrder (left, right, self)
    """
    nodeList = list()
    if curr_node is not None:
        nodeList = postOrder(curr_node.getleft()) + postOrder(curr_node.getright()) + [curr_node]
    return nodeList

def binary_search_tree():
    r"""
    Example
                  8
                 / \
                3   10
               / \    \
              1   6    14
                 / \   /
                4   7 13
    """
    t = BinarySearchTree()
    testlist = [8, 3, 6, 1, 10, 14, 13, 4, 7]
    for i in testlist:
        t.insert(i)

    #Prints all the elements of the list in order traversal
    print(t)
    #Gets all the elements of the tree In pre order
    #And it prints them
    nodelist = t.traversalTree(postOrder, t.root)
    print(" ".join([repr(i.get_data()) for i in nodelist]))
    
    if(t.getNode(6) is not None):
        print("The data 6 exists")
    else:
        print("The data 6 doesn't exist")

    if(t.getNode(-1) is not None):
        print("The data -1 exists")
    else:
        print("The data -1 doesn't exist")

    if(not t.empty()):
        print(("Max Value: ", t.getMax().get_data()))
        print(("Min Value: ", t.getMin().get_data()))

    for i in testlist:
        t.delete(i)
        print(t)

    t.getNode(6)

if __name__ == "__main__":
    binary_search_tree()
