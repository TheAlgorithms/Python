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


def preorder(root: Node):
    """
    PreOrder traversal visits
    1. root node
    2. left subtree
    3. right subtree.
    >>> preorder(make_tree())
    1 2 4 5 3
    """
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root: Node):
    """
    PostOrder traversal visits
    1. left subtree
    2. right subtree
    3. root node
    >>> postorder(make_tree())
    4 5 2 3 1
    """
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


def inorder(root: Node):
    """
    InOrder traversal visit
    1. left subtree
    2. root node
    3. right subtree
    >>> inorder(make_tree())
    4 2 5 1 3
    """
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def height(root: Node):
    """
    Recursive function for calculating the height of the binary tree.
    >>> height(make_tree())
    3
    """
    if not root:
        return 0
    left_Height = height(root.left)
    right_Height = height(root.right)
    return max(left_Height, right_Height) + 1


def level_order_1(root: Node):
    """
    Print whole binary tree in Level Order Traverse.
    Level Order traverse: Visit nodes of the tree level-by-level.
    >>> level_order_1(make_tree())
    1 2 3 4 5
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


def level_order_2(root: Node, level: int):
    """
    Level-wise traversal: Print all nodes present at the given level of the binary tree
    >>> tree = make_tree()
    >>> level_order_2(tree, 2)
    2 3
    >>> level_order_2(tree, 3)
    4 5
    """
    if not root:
        return root
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        level_order_2(root.left, level - 1)
        level_order_2(root.right, level - 1)


def print_left_to_right(root: Node, level: int):
    """
    Print elements on particular level from left to right direction of the binary tree.
    >>> print_left_to_right(make_tree(), 2)
    2 3
    """
    if not root:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        print_left_to_right(root.left, level - 1)
        print_left_to_right(root.right, level - 1)


def print_right_to_left(root: Node, level: int):
    """
    Print elements on particular level from right to left direction of the binary tree.
    >>> print_right_to_left(make_tree(), 2)
    3 2
    """
    if not root:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        print_right_to_left(root.right, level - 1)
        print_right_to_left(root.left, level - 1)


def zigzag(root: Node):
    """
    ZigZag traverse: Print node left to right and right to left, alternatively.
    >>> zigzag(make_tree())
    1 3 2 4 5
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
    root = make_tree()
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
    level_order_1(root)
    print("\nLevel-wise order Traversal is : ")
    for h in range(1, height_tree + 1):
        level_order_2(root, h)
    print("\nZigZag order Traversal is : ")
    zigzag(root)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
