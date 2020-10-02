
from typing import Optional

        
class Node:
    """
    A Node has data variable and pointers to Nodes to its left and right.
    """

    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        
def display(tree: Optional[Node]) -> None:  # In Order traversal of the tree
    """
    >>> root = Node(1)
    >>> root.left = Node(0)
    >>> root.right = Node(2)
    >>> display(root)
    0
    1
    2
    >>> display(root.right)
    2
    """
    if tree:
        display(tree.left)
        print(tree.data)
        display(tree.right)

def kthSmallest(root: Node, k: int) -> int: 
    """
    In a BST, the Inorder Traversal returns ascending order of the data when traversed.
    Thus, store Inorder traversal in a list and return the k-1 th Index which is the Kth Smallest number in a BST.
    
    """
    stack = []
    temp = []
    while True:
        if root is not None:
            stack.append(root)
            root = root.left
        else:
            if len(stack) == 0:
                break
            root = stack.pop()
            temp.append(root.data)
            root = root.right
    return (temp[k-1])

def main() -> None:  # Main function for testing.
    tree = Node(5)
    tree.left = Node(3)
    tree.right = Node(6)
    tree.left.left = Node(2)
    tree.left.right = Node(4)
    tree.left.left.left = Node(1)
    k = int(input("Enter the value of K:"))
    print("The {}th Smallest Value in the BST is:".format(k), kthSmallest(tree, k))
    print("Tree is: ")
    display(tree)


if __name__ == "__main__":
    main()
