class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root


def inorder(root):
    if root is None: 
        return
    if root.left is not None:
        inorder(root.left)
    print(root.data)
    if root.right is not None:
        inorder(root.right)
    return

def minimum(root):
    curr = root
    while curr.left != None:
        curr = curr.left
    return curr

def delete(root, data):
    if data < root.data:
        root.left = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minimum(root.right)
        root.data = temp.data
        root.right = delete(root.right,temp.data)
    return root

def main():
    root = Node(5)
    insert(root,4)
    insert(root,3)
    insert(root,6)
    inorder(root)
        
if __name__ =='__main__':
    main()
