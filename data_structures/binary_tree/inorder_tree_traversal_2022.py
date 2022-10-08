"""
Illustrate how to implement inorder traversal in binary search tree.
Author: Gurneet Singh
https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
"""

'''
5 items had no tests:
    __main__
    __main__.BinaryTreeNode
    __main__.BinaryTreeNode.__init__
    __main__.inorder
    __main__.insert
0 tests in 5 items.
0 passed and 0 failed.
Test passed.
Printing values of binary search tree in Inorder Traversal.
6
10
14
15
20
25
60
'''
class BinaryTreeNode:
    '''Defining the structure of BinaryTreeNode'''
    def __init__(self, data: int) -> None:
        self.data = data    
        self.left_Child = None
        self.right_Child = None

def insert(node : None , new_Value : int) -> BinaryTreeNode:    # if binary search tree is empty, make a new node and declare it as root
    if node is None:
        node = BinaryTreeNode(new_Value)
        return node

    # binary search tree is not empty, so we will insert it into the tree
    # if new_Value is less than value of data in node, add it to left subtree and proceed recursively
    if new_Value < node.data:
        node.left_Child = insert(node.left_Child, new_Value)
    else:
        # if new_Value is greater than value of data in node, add it to right subtree and proceed recursively
        node.right_Child = insert(node.right_Child, new_Value)
    return node


def inorder(node : None) -> None:    # if node is None,return
    if node == None:
        return
    # traverse left subtree
    inorder(node.left_Child)
    # traverse current node
    print(node.data)
    # traverse right subtree
    inorder(node.right_Child)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    root = insert(None, 15)
    insert(root, 10)
    insert(root, 25)
    insert(root, 6)
    insert(root, 14)
    insert(root, 20)
    insert(root, 60)
    print("Printing values of binary search tree in Inorder Traversal.")
    inorder(root)