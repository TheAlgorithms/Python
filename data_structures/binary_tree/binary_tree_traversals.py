# https://en.wikipedia.org/wiki/Tree_traversal


class Node:
    """
    A Node has data variable and pointers to its left and right nodes.
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
    Pre-order traversal visits root node, left subtree, right subtree.
    >>> preorder(make_tree())
    [1, 2, 4, 5, 3]
    """
    return [root.data] + preorder(root.left) + preorder(root.right) if root else []


def postorder(root: Node):
    """
    Post-order traversal visits left subtree, right subtree, root node.
    >>> postorder(make_tree())
    [4, 5, 2, 3, 1]
    """
    return postorder(root.left) + postorder(root.right) + [root.data] if root else []


def inorder(root: Node):
    """
    In-order traversal visits left subtree, root node, right subtree.
    >>> inorder(make_tree())
    [4, 2, 5, 1, 3]
    """
    return inorder(root.left) + [root.data] + inorder(root.right) if root else []


def height(root: Node):
    """
    Recursive function for calculating the height of the binary tree.
    >>> height(None)
    0
    >>> height(make_tree())
    3
    """
    return (max(height(root.left), height(root.right)) + 1) if root else 0


def level_order_1(root: Node):
    """
    Print whole binary tree in Level Order Traverse.
    Level Order traverse: Visit nodes of the tree level-by-level.
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
    return que


def level_order_2(root: Node, level: int):
    """
    Level-wise traversal: Print all nodes present at the given level of the binary tree
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
    print(f"  In-order Traversal is {inorder(root)}")
    print(f" Pre-order Traversal is {preorder(root)}")
    print(f"Post-order Traversal is {postorder(root)}")
    print(f"Height of Tree is {height(root)}")
    print("Complete Level Order Traversal is : ")
    level_order_1(root)
    print("\nLevel-wise order Traversal is : ")
    for h in range(1, height(root) + 1):
        level_order_2(root, h)
    print("\nZigZag order Traversal is : ")
    zigzag(root)
    print()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
