class Node:
    """
    A Node has data variable and pointers
    to its left and right nodes.
    """

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def make_tree() -> Node:
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    return root


def preorder(root):
    """
    PreOrder traversal: visit root node
    then its left subtree followed
    by right subtree.
    preorder(make_tree())
    1 2 4 5 3 
    """
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    """
    PostOrder traversal: visit left subtree
    followed by right subtree
    and then root node.
    """
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


def inorder(root):
    """
    InOrder traversal: visit its leftsubtree
    followed by root node and
    then right subtree.
    """
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def height(root):
    """
    Recursive function for calculating
    height of the binary tree.
    """
    if not root:
        return 0
    left_Height = height(root.left)
    right_Height = height(root.right)
    if left_Height > right_Height:
        return left_Height + 1
    else:
        return right_Height + 1


def levelorder1(root):
    """
    Print whole binary tree in Level Order Traverse.
    Level Order traverse: Visit nodes
    of the tree level-by-level.
    """
    if not root:
        return
    temp = root
    que = [temp]
    while len(que) > 0:
        print(que[0].data, end=" ")
        temp = que.pop(0)
        if temp.left:
            que.append(temp.left)
        if temp.right:
            que.append(temp.right)


def levelorder2(root, level):
    """
    Level-wise traversal:
    Print all nodes present at the
    given level of the binary tree.
    """
    if not root:
        return root
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        levelorder2(root.left, level - 1)
        levelorder2(root.right, level - 1)


def print_left_to_right(root, level):
    """
    Print elements on particular level
    from left to right direction of
    the binary tree.
    """
    if not root:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        print_left_to_right(root.left, level - 1)
        print_left_to_right(root.right, level - 1)


def print_right_to_left(root, level):
    """
    Print elements on particular level
    from right to left direction of
    the binary tree.
    """
    if not root:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        print_right_to_left(root.right, level - 1)
        print_right_to_left(root.left, level - 1)


def zigzag(root):
    """
    ZigZag traverse: Print node
    left to right and
    right to left, alternatively.
    """
    flag = 0
    height_tree = height(root)
    for h in range(1, height_tree + 1):
        if flag == 0:
            print_left_to_right(root, h)
            flag = 1
        else:
            print_right_to_left(root, h)
            flag = 0


def main():  # Main function for testing.
    """
    Create binary tree.
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    """
    All Traversals of the binary are as follows:
    """
    print("In order Traversal is : ")
    inorder(root)
    print("\nPre order Traversal is : ")
    preorder(root)
    print("\nPost order Traversal is : ")
    postorder(root)
    print("\nHeight of Tree is : ")
    height_tree = height(root)
    print(height_tree)
    print("\nComplete Level Order Traversal is : ")
    levelorder1(root)
    print("\nLevel-wise order Traversal is : ")
    for h in range(1, height_tree + 1):
        levelorder2(root, h)
    print("\nZigZag order Traversal is : ")
    zigzag(root)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
