''' This is a pure python implementation of various views of a tree.
    Values passed to functions are refrential.
'''
from collections import defaultdict

class treeNode:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def insert(root,val):
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

def verticalView(root,idx,h):
    if root:
        h[idx].append(root.data)
        verticalView(root.left,idx-1,h)
        verticalView(root.right,idx+1,h)
        
def horizontalView(root,idx,h):
    if root:
        h[idx].append(root.data)
        horizontalView(root.left,idx+1,h)
        horizontalView(root.right,idx+1,h)

def sideView(root,rightSide=False):
    h = defaultdict(list)
    horizontalView(root,0,h)
    side = []
    idx = -1 if rightSide else 0
    for _,data in h.items():
        side.append(data[idx])
    return side

def upDownView(root,bottom=False):
    h = defaultdict(list)
    verticalView(root,0,h)
    res = []
    idx = -1 if bottom else 0
    for i in sorted(h):
        res.append(h[i][idx])
    return res

def printData(ans):
    if type(ans) is list:
        for i in ans:
            print(i)
    else:
        for i in sorted(ans):
            print(ans[i])
if __name__ == '__main__':
    
    root = treeNode(input('Enter root value\t\t\t'))
    while True:
        n = input('Enter Node data / Enter q to exit\t')
        if n=='q':
            break
        insert(root,n)

    print()
    option = input('Enter:- \n\ttop\n\tbottom\n\thorizontal\n\tleft\n\tright\n\tvertical\n\nto see the particular view of your tree\t')

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
    else:
        print('Invalid Choice')
