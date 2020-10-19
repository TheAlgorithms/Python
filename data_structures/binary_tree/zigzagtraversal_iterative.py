class Node:
    """
    A Node has data variable and pointers to its left and right nodes.
    """

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def make_tree() -> Node:
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    return root

def zigzag_iterative(root: Node):
    """
    ZigZag traverse by iterative method: Print node left to right and right to left, alternatively.
    """
    if root == None: 
        return 
  
    # two stacks to store alternate levels  
    s1 = [] # For levels to be printed from right to left  
    s2 = [] # For levels to be printed from left to right  
  
    # append first level to first stack 's1'  
    s1.append(root)  
  
    # Keep printing while any of the stacks has some nodes  
    while not len(s1) == 0 or not len(s2) == 0: 
          
        # Print nodes of current level from s1 and append nodes of next level to s2  
        while not len(s1) == 0: 
            temp = s1[-1]  
            s1.pop()  
            print(temp.data, end = " ")  
  
            # Note that is left is appended before right    
            if temp.left: 
                s2.append(temp.left)
            if temp.right:  
                s2.append(temp.right)
  
        # Print nodes of current level from s2 and append nodes of next level to s1  
        while not len(s2) == 0: 
            temp = s2[-1]  
            s2.pop()  
            print(temp.data, end = " ")  
  
            # Note that is rightt is appended before left   
            if temp.right:  
                s1.append(temp.right)
            if temp.left: 
                s1.append(temp.left)  

def main():  # Main function for testing.
    """
    Create binary tree.
    """
    root = make_tree()
    print("\nZigzag order traversal(iterative) is: ")
    zigzag_iterative(root)
    print()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
    
