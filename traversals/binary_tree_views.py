''' This is a pure python implementation of various views of a tree.
    Values passed to functions are refrential.
'''
from collections import defaultdict

class treeNode:                                         #Create Tree Node
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def insert(root,val):                                   # Insert Node value
    while root is not None:
        if root.data < val:
            if not root.right:
                root.right=treeNode(val)
                break
            else:
                root = root.right
        else:
            if root.left is None:
                root.left=treeNode(val)
                break
            else:
                root = root.left

def verticalView(root,idx,h):                           # Updates variable h(dictionary)
    if root:
        h[idx].append(root.data)
        verticalView(root.left,idx-1,h)
        verticalView(root.right,idx+1,h)
        
def horizontalView(root,idx,h):                         #Updates variable h(dictionary)
    if root:
        h[idx].append(root.data)
        horizontalView(root.left,idx+1,h)
        horizontalView(root.right,idx+1,h)

def sideView(root,rightSide=False):                     # Returns list containing sideview having elements from 0 to n level of tree
    h = defaultdict(list)
    horizontalView(root,0,h)
    side = []
    idx = -1 if rightSide else 0
    for _,data in h.items():
        side.append(data[idx])
    return side

def upDownView(root,bottom=False):                      # Returns list from left to right elements of a tree either from above or bottom
    h = defaultdict(list)
    verticalView(root,0,h)
    res = []
    idx = -1 if bottom else 0
    for i in sorted(h):
        res.append(h[i][idx])
    return res

def printData(ans):                                     # Utility Function to print values for a given view
    print("\n\n************** Result ***************")
    if type(ans) is list:
        for i in ans:
            print(i)
    else:
        for i in sorted(ans):
            print(ans[i])
    print("*************************************\n\n")
if __name__ == '__main__':
    
    root = treeNode(input('Enter root value\t\t\t'))
    while True:
        n = input('Enter Node data / Enter q to exit\t')
        if n=='q':
            break
        insert(root,n)

    print()
    while True:
        option = input('Enter:- \n\ttop\n\tbottom\n\thorizontal\n\tleft\n\tright\n\tvertical\n\nto see the particular view of your tree / Enter q to exit\t')
        
        if option=='vertical':
            h = defaultdict(list)
            verticalView(root,0,h)
            printData(h)
        elif option=='horizontal':
            h = defaultdict(list)
            horizontalView(root,0,h)
            printData(h)
        elif option=='left':
            printData(sideView(root))
        elif option=='right':
            printData(sideView(root,True))
        elif option=='top':
            printData(upDownView(root))
        elif option=='bottom':
            printData(upDownView(root,True))
        elif option=='q':
            break
        else:
            print('Invalid Choice')
