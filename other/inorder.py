"""
wikipedia 
https://en.wikipedia.org/wiki/Tree_traversal
"""

class BinaryTreeNode:
  def __init__(self, data) -> None:
    self.data = data
    self.leftChild = None
    self.rightChild=None
     
def insert(root,newValue) -> BinaryTreeNode:
    #if binary search tree is empty, make a new node and declare it as root
    if root is None:
        root=BinaryTreeNode(newValue)
        return root
 
    #binary search tree is not empty, so we will insert it into the tree
    #if newValue is less than value of data in root, add it to left subtree and proceed recursively
    if newValue<root.data:
        root.leftChild=insert(root.leftChild,newValue)
    else:
        #if newValue is greater than value of data in root, add it to right subtree and proceed recursively
        root.rightChild=insert(root.rightChild,newValue)
    return root
 
def inorder(root) -> None:
#if root is None,return
        if root==None:
            return
#traverse left subtree
        inorder(root.leftChild)
#traverse current node
        print(root.data)
#traverse right subtree
        inorder(root.rightChild)     
               




if __name__ == "__main__":
  root= insert(None,15)
  insert(root,10)
  insert(root,25)
  insert(root,6)
  insert(root,14)
  insert(root,20)
  insert(root,60)
  print("Printing values of binary search tree in Inorder Traversal.")
  inorder(root)
  
