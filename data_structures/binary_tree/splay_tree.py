class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


class SplayTree:
    def __init__(self):
        self.root = None

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x

        y.parent = x.parent
        # x is root
        if x.parent == None:
            self.root = y
        # x is left child
        elif x == x.parent.left:
            x.parent.left = y
        # x is right child
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x

        y.parent = x.parent
        # x is root
        if x.parent == None:
            self.root = y
        # x is right child
        elif x == x.parent.right:
            x.parent.right = y
        # x is left child
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def splay(self, n):
        # node is not root
        while n.parent != None:
            # node is child of root, one rotation
            if n.parent == self.root:
                if n == n.parent.left:
                    self.rightRotate(n.parent)
                else:
                    self.leftRotate(n.parent)

            else:
                p = n.parent
                g = p.parent  # grandparent

                if n.parent.left == n and p.parent.left == p:  # both are left children
                    self.rightRotate(g)
                    self.rightRotate(p)

                elif n.parent.right == n and p.parent.right == p:  # both are right children
                    self.leftRotate(g)
                    self.leftRotate(p)

                elif n.parent.right == n and p.parent.left == p:
                    self.leftRotate(p)
                    self.rightRotate(g)

                elif n.parent.left == n and p.parent.right == p:
                    self.rightRotate(p)
                    self.leftRotate(g)

    def insert(self, n):
        y = None
        temp = self.root
        while temp != None:
            y = temp
            if n.data < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        n.parent = y

        if y == None:  # newly added node is root
            self.root = n
        elif n.data < y.data:
            y.left = n
        else:
            y.right = n

        self.splay(n)

    def bstSearch(self, n, x):
        if x == n.data:
            self.splay(n)
            return n
        elif x < n.data:
            return self.bstSearch(n.left, x)
        elif x > n.data:
            return self.bstSearch(n.right, x)
        else:
            return None

    def preOrder(self, n):
        if n != None:
            print(n.data)
            self.preOrder(n.left)
            self.preOrder(n.right)
    
    def inOrder(self, n):
        if n != None:
            self.inOrder(n.left)
            print(n.data)
            self.inOrder(n.right)
    
    def postOrder(self, n):
        if n != None:
            self.postOrder(n.left)
            self.postOrder(n.right)
            print(n.data)
    
    


if __name__ == '__main__':
    tree = SplayTree()

    tree.insert(Node(90))
    '''
    The tree looks like this:
                        90
    '''

    tree.insert(Node(10))
    '''
    The tree looks like this:
                        90
                       /
                      10
    '''

    tree.insert(Node(34))
    '''
    The tree looks like this:
                        34
                       /  \
                      10   90
    '''

    tree.insert(Node(18))
    '''
    The tree looks like this:
                        18
                       /  \
                      10   34
                            \
                            90
    '''

    tree.insert(Node(25))
    '''
    The tree looks like this:
                        25
                       /  \
                     18    34
                    /        \
                   10        90
    '''

    tree.insert(Node(60))
    '''
    The tree looks like this:
                        60
                       /  \
                     25    90
                    /  \
                   18   34
                  /
                10
    '''

    tree.insert(Node(100))
    '''
    Finally the tree looks like this:
                        100 
                       /
                      90
                     /
                    60
                   /
                  25
                 /  \
                18   34
               /
              10
    '''
    
    tree.bstSearch(tree.root, 10) # splay 10 to root 
    '''
    The tree looks like this:
                        10
                          \
                          100
                         /
                        60
                       /  \
                      18   90
                        \
                         25
                           \
                            34
    '''   

    print("The Pre-order traveral of the tree is:")
    tree.preOrder(tree.root)
    '''
    The traversal of the tree is:   10, 100, 60, 18, 25, 34, 90
    '''

    print("The In-order traveral of the tree is:")
    tree.inOrder(tree.root)
    '''
    The traversal of the tree is:   10, 100, 60, 18, 25, 34, 90
    '''

    print("The Post-order traveral of the tree is:")
    tree.postOrder(tree.root)
    '''
    The traversal of the tree is:   34, 25, 18, 90, 60, 100, 10
    '''
