class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

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

def topView(root):
    #Write your code here
    q = [root]
    spread = [0]
    stack = [root]
    low = 0
    high = 0
    while q:
        n = len(q)
        for i in range(n):
            node = q.pop(0)
            s = spread.pop(0)
            if node.left:
                spread.append(s-1)
                q.append(node.left)
                if s-1 < low:
                    stack = [node.left] + stack
                    low = s-1
            if node.right:
                q.append(node.right)
                spread.append(s+1)
                if s+1>high:
                    stack.append(node.right)
                    high = s+1

    for i in stack:
        print(i.info,end=' ') 



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)