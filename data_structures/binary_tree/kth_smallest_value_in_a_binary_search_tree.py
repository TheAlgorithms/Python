from typing import Optional

    
class Node:
    """
    A Node has data variable and pointers to Nodes to its left and right.
    """

    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


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
    return temp[k - 1]


if __name__ == "__main__":
    tree = Node(5)
    tree.left = Node(3)
    tree.right = Node(6)
    tree.left.left = Node(2)
    tree.left.right = Node(4)
    tree.left.left.left = Node(1)
    k = 2  
    print("The " + str(k) + "-th Smallest Value in the BST is: " + str(kthSmallest(tree, k)))
