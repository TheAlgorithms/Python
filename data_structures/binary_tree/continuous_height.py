import doctest

class Node(object):
    def __init__(self, val : int) -> None:
        self.data = val
        self.left = None
        self.right = None

class BST:
    def __init__(self) -> None: 
        self.root = None

    def create(self, value : int) -> None:  #value is the element to be inserted to BST
        doctest.testmod()
        if self.root == None:
            self.root = node(value)
        else:
            current = self.root
            while True:
                if current.data > value:
                    if current.left != None:
                        current = current.left
                    else:
                        current.left = node(value)
                        break
                elif current.data < value:
                    if current.right:
                        current = current.right
                    else:
                        current.right = node(value)
                        break
                else:
                    break

def height_of_tree(root : Node) -> int:
    doctest.testmod()
    if not root:
        return -1
    return 1 + max(height_of_tree(root.right), height_of_tree(root.left))

if __name__ == "__main__":
    doctest.testmod()
    t = int(input())
    for i in range(t):
        n = int(input())
        ar = list(map(int, input().split()))
        tree = BST()
        for i in range(n):
            tree.create(ar[i])
            print(height_of_tree(tree.root), end =" ") 
        print()
