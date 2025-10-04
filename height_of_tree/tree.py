class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 

    def __str__(self):
        return str(self.info) 


class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def height(node):
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))

def tree_height_from_list(data):
    bst = BinarySearchTree()
    for x in data:
        bst.create(x)
    return height(bst.root)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
