class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def PrintTree ( self ) :
       if self.left :
           self.left.PrintTree ()
       print ( self.data, end= ' ' ) ,
       if self.right :
           self.right.PrintTree ()

class Solution:
    '''
    Function to invert the tree
    '''
    def invertTree(self, root):
       if root == None:
           return
       root.left, root.right = self.invertTree(root.right),self.invertTree(root.left)
       return root
