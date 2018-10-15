
# Python program for printing vertical order of a given 
# binary tree 
  
# A binary tree node 
class Node: 
    # Constructor to create a new node 
    def __init__(self, key): 
        self.key = key 
        self.left = None
        self.right = None
  
# Utility function to store vertical order in map 'm'  
# 'hd' is horizontal distance of current node from root 
# 'hd' is initially passed as 0 
def getVerticalOrder(root, hd, m): 
  
    # Base Case 
    if root is None: 
        return
      
    # Store current node in map 'm' 
    try: 
        m[hd].append(root.key) 
    except: 
        m[hd] = [root.key] 
      
    # Store nodes in left subtree 
    getVerticalOrder(root.left, hd-1, m) 
      
    # Store nodes in right subtree 
    getVerticalOrder(root.right, hd+1, m) 
  
# The main function to print vertical order of a binary 
#tree ith given root 
def printVerticalOrder(root): 
      
    # Create a map and store vertical order in map using 
    # function getVerticalORder() 
    m = dict() 
    hd = 0 
    getVerticalOrder(root, hd, m) 
      
    # Traverse the map and print nodes at every horizontal 
    # distance (hd) 
    for index, value in enumerate(sorted(m)): 
        for i in m[value]: 
            print i, 
        print 
  
  
# Driver program to test above function 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right = Node(8) 
root.right.right.right = Node(9) 
print "Vertical order traversal is"
printVerticalOrder(root) 
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
