from typing import Optional, List

class Node:
    def __init__(self, info: int) -> None:
        self.info: int = info
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None

    def __str__(self) -> str:
        """
        >>> str(Node(5))
        '5'
        """
        return str(self.info)

class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def create(self, val: int) -> None:
        """
        >>> bst = BinarySearchTree()
        >>> bst.create(10)
        >>> bst.root.info
        10
        >>> bst.create(5)
        >>> bst.root.left.info
        5
        """
        if self.root is None:
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

def height(node: Optional[Node]) -> int:
    """
    >>> height(None)
    -1
    >>> n = Node(3)
    >>> height(n)
    0
    >>> n.left = Node(2)
    >>> n.right = Node(5)
    >>> n.right.right = Node(6)
    >>> height(n)
    2
    """
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))

def tree_height_from_list(data: List[int]) -> int:
    """
    >>> tree_height_from_list([3,2,5,6])
    2
    >>> tree_height_from_list([1])
    0
    >>> tree_height_from_list([5,1,10,15,7])
    3
    """
    bst = BinarySearchTree()
    for x in data:
        bst.create(x)
    return height(bst.root)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
