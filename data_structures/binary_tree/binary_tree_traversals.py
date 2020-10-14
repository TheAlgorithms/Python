class Node:
    """
    A Node has data variable and pointers toits left and right nodes.
    """
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

def preOrder(root):
    """
    PreOrder traversal: visit root node then its left subtree followed by right subtree.
    """
    if(root!=None):
        print(root.data,end=" ")
        preOrder(root.left)
        preOrder(root.right)
        
def postOrder(root):
    """
    PostOrder traversal: visit left subtree followed by right subtree and then root node.
    """
    if(root!=None):
        postOrder(root.left)
        postOrder(root.right)
        print(root.data,end=" ")
        
def inOrder(root):
    """
    InOrder traversal: visit its left subtree followed by root node and then right subtree.
    """
    if(root!=None):
        inOrder(root.left)
        print(root.data,end=" ") 
        inOrder(root.right)

def Height(root):
    """
    Recursive function for calculating height of the binary tree.
    """
    if(root==None):
        return 0
    leftHeight=Height(root.left)
    rightHeight=Height(root.right)
    if leftHeight>rightHeight:
        return leftHeight+1
    else:
        return rightHeight+1
    
def levelOrder1(root):
    """
    Print whole binary tree in Level Order Traverse.
    Level Order traverse: Visit nodes of the tree level-by-level.
    """
    if root==None:
        return
    temp=root
    que=[temp]
    while(len(que)>0):
        print(que[0].data,end=" ")
        temp=que.pop(0)
        if temp.left!=None:
            que.append(temp.left)
        if temp.right!=None:
            que.append(temp.right)

def levelOrder2(root,level):
    """
    Level-wise traversal:
    Print all nodes present at the given level of the binary tree.
    """
    if root==None:
        return root
    if level==1:
        print(root.data,end=" ")
    elif level>1:
        levelOrder2(root.left,level-1)
        levelOrder2(root.right,level-1)  

def printLeftToRight(root,level):
    """
    Print elements on particular level from left to right direction of the binary tree.
    """
    if root==None:
        return
    if level==1:
        print(root.data,end=" ")
    elif level>1:
        printLeftToRight(root.left,level-1)
        printLeftToRight(root.right,level-1)

def printRightToLeft(root,level):
    """
    Print elements on particular level from right to left direction of the binary tree.
    """
    if root==None:
        return
    if level==1:
        print(root.data,end=" ")
    elif level>1:
        printRightToLeft(root.right,level-1)
        printRightToLeft(root.left,level-1)
    
def ZigZag(root):
    """
    ZigZag traverse: Print node left to right and right to left, alternatively.
    """
    flag=0
    height=Height(root)
    for h in range(1,height+1):
        if flag==0:
            printLeftToRight(root,h)
            flag=1
        else:
            printRightToLeft(root,h)
            flag=0

def main(): # Main function for testing.
    """
    Create binary tree.
    """
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)

    """
    All Traversals of the binary are as follows:
    """
    print("In order Traversal is : ")
    inOrder(root)
    print("\nPre order Traversal is : ")
    preOrder(root)
    print("\nPost order Traversal is : ")
    postOrder(root)
    print("\nHeight of Tree is : ")
    height=Height(root)
    print(height)
    print("\nComplete Level Order Traversal is : ")
    levelOrder1(root)
    print("\nLevel-wise order Traversal is : ")
    for h in range(1,height+1):
        levelOrder2(root,h)
    print("\nZigZag order Traversal is : ")
    ZigZag(root)

if __name__ == "__main__":
    main()
