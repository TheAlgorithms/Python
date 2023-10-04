class node:

    def __init__(self,char,freq):

        self.char = char
        self.freq = freq

        self.left = None
        self.right = None

        self.code = ""
def buildTree(freq):
    nodes = []

    for char in freq:
        nodes.append(node(char,freq[char]))
    
    while len(nodes)>1:
        nodes.sort(key=lambda x:x.freq)

        left = nodes.pop(0)
        right = nodes.pop(0)

        parent = node('None',left.freq+right.freq)

        parent.left = left
        parent.right = right

        nodes.append(parent)
    
    return nodes[0]

def traverse(node,code):
    
    if node is not None:
        node.code = code
        traverse(node.left,code+'0')
        traverse(node.right,code+'1')

def printCodes(node):
    if node is not None:
        if node.char!='None':
            print(f"The code for {node.char} is {node.code}")
        printCodes(node.left)
        printCodes(node.right)

def assignCode(tree):
    traverse(tree,"")

freq = {'a':5,'b':9,'c':12,'d':13,'e':16,'f':45}

tree = buildTree(freq)

assignCode(tree)

printCodes(tree)