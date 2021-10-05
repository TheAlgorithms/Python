class node(object):
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

class BST:
    def __init__(self): 
        self.root = None

    def create(self, x):  
        if self.root == None:
            self.root = node(x)
        else:
            current = self.root
            while True:
                if current.data > x:
                    if current.left != None:
                        current = current.left
                    else:
                        current.left = node(x)
                        break
                elif current.data < x:
                    if current.right:
                        current = current.right
                    else:
                        current.right = node(x)
                        break
                else:
                    break

def heightOfTree(root):
    if not root:
        return -1
    return 1 + max(heightOfTree(root.right), heightOfTree(root.left))

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        ar = list(map(int, input().split()))
        tree = BST()
        for i in range(n):
            tree.create(ar[i])
            print(heightOfTree(tree.root), end =" ") 
        print()