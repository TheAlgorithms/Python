class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def morris_traversal(root):
    """
    Morris(InOrder) travaersal is a tree traversal algorithm that does not employ
     the use of recursion or a stack. In this traversal, links are created as
    successors and nodes are printed using these links.
    Finally, the changes are reverted back to restore the original tree.
    root = Node(4)
    temp = root
    temp.left = Node(2)
    temp.right = Node(8)
    temp = temp.left
    temp.left = Node(1)
    temp.right = Node(5)
    """
    inorder_traversal = []
    # set current to root of binary tree
    current = root

    while current is not None:
        if current.left is None:
            inorder_traversal.append(current.data)
            current = current.right
        else:
            # find the previous (prev) of curr
            previous = current.left
            while previous.right is not None and previous.right != current:
                previous = previous.right

            # make curr as right child of its prev
            if previous.right is None:
                previous.right = current
                current = current.left

            # firx the right child of prev
            else:
                previous.right = None
                inorder_traversal.append(current.data)
                current = current.right

    return inorder_traversal


def main():
    root = Node(4)
    temp = root
    temp.left = Node(2)
    temp.right = Node(8)
    temp = temp.left
    temp.left = Node(1)
    temp.right = Node(5)
    print(morris_traversal(root))


if __name__ == "__main__":
    main()
