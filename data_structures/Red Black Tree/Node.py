class Node:
    def __init__(self,info=None,color=None):
        self.info = info
        self.color = color
        self.lchild = None
        self.rchild = None
        self.parent = None