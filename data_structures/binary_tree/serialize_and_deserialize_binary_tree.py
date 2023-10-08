from collections.abc import Generator

"""
    The class Node is used to create nodes of the Binary Tree.

    Agrs : Takes value x to create an object of Node with value x.

    Returns : Creates new object of Node.
"""


class Node:
    def __init__(self, data: int) -> None:
        self.value = data
        self.left: Node | None = None
        self.right: Node | None = None


def make_tree() -> Node:
    r"""
    The Tree has :

                                  20
                                /   \
                                2   13
                             /  \   /   \
                    null -   N  N   4   5
                                    / \  / \
                                    N N  N  N - null
    """
    root = Node(20)
    root.left = Node(2)
    root.right = Node(13)
    root.right.left = Node(4)
    root.right.right = Node(5)
    return root
    """
    Serialize Function takes root as a parameter and returns a String.

    Agrs:
            root : Takes root node as a parameter.

    Returns: A string of preorder traversal of nodes in tree
             with null values of leaf nodes.
    """


def serialize(root: Node | None) -> str | None:
    """
    >>> serialize(make_tree())
    '20,2,N,N,13,4,N,N,5,N,N'
    """
    result = []

    def depth_first_search(node: Node) -> None:
        if not node:
            result.append("N")
            return
        result.append(str(node.value))
        depth_first_search(node.left)
        depth_first_search(node.right)

    depth_first_search(root)
    return ",".join(result)

    """
    Deserialize Function takes String as a parameter and returns root of tree.

    Agrs :
            String : Takes string of all node values with null values
            of leaf nodes separated by comma as a parameter.

    Returns : Root of the tree created after deserialing the string.
    """


def deserialize(data: str | None) -> Node | None:
    """
    >>> root = deserialize("20,2,N,N,13,4,N,N,5,N,N")
    >>> list(preorder(root))
    [20, 2, 13, 4, 5]
    """
    global index
    index = 0
    node_values = data.split(",")

    def depth_first_search() -> Node | None:
        global index
        if node_values[index] == "N":
            index += 1
            return None
        root = Node(int(node_values[index]))
        index += 1
        root.left = depth_first_search()
        root.right = depth_first_search()
        return root

    return depth_first_search()

    # This method is written to traverse the tree created by deserialize method.


def preorder(root: Node | None) -> Generator[int, None, None]:
    """
    >>> list(preorder(make_tree()))
    [20, 2, 13, 4, 5]
    >>> list(preorder(None))
    []
    """
    if root:
        yield root.value
        yield from preorder(root.left)
        yield from preorder(root.right)


def main() -> None:  # Main function for testing.
    # Create binary tree.
    root = make_tree()
    serialized_string = serialize(root)
    print(f"Serialized string : {serialized_string}")
    deserialized_root = deserialize(serialized_string)
    print(f"The Deserialized Tree : {list(preorder(deserialized_root))}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
