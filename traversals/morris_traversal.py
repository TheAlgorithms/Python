"""
Morris(InOrder) travaersal is a tree traversal algorithm that does not employ the use of recursion or a stack.
In this traversal, links are created as successors and nodes are printed using these links.
Finally, the changes are reverted back to restore the original tree.

"""



class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None



def Morris_traversal(root):
    """
    Traverse through the tree and returns a inorder traversal of tree
    Time: O(V+E)
    Space: O(1) #ignoring InorderTraversal list
    """
    InorderTraversal = []
    # set current to root of binary tree
    curr = root

    while(curr is not None):
        if(curr.left is None):
            InorderTraversal.append(curr.data)
            curr = curr.right
        else:
            # find the previous (prev) of curr
            prev = curr.left
            while(prev.right is not None and prev.right != curr):
                prev = prev.right
            
            # make curr as right child of its prev
            if(prev.right is None):
                prev.right = curr
                curr = curr.left
            
            #firx the right child of prev
            else:
                prev.right = None 
                InorderTraversal.append(curr.data)
                curr = curr.right
    

    return InorderTraversal



root = Node(4)
temp = root
temp.left = Node(2)
temp.right = Node(8)
temp = temp.left
temp.left = Node(1)
temp.right = Node(5) 

print(Morris_traversal(root))
