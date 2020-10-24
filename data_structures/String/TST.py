
class Node(object):
    def __init__(self, char):
        self.char = char
        self.left = self.middle = self.right = None
        self.value = None


class TernarySearchTree(object):
    def __init__(self):
        self.root = None

    def put(self, key, value):
        self.root = self.recursive(key, value)(self.root, 0)

    def get(self, key):
        node = self.recursive(key)(self.root, 0)
        if node:
            return node.value
        return -1

    def recursive(self, key, value=None):

        def putter(node, index):
            char = key[index]

            if node is None:
                node = Node(char)
            if char < node.char:
                node.left = putter(node.left, index)
            elif char > node.char:
                node.right = putter(node.right, index)
            elif index < len(key) - 1:
                node.middle = putter(node.middle, index+1)
            else:
                node.value = value

            return node

        def getter(node, index):
            char = key[index]

            if node is None:
                return None

            if char < node.char:
                return getter(node.left, index)
            elif char > node.char:
                return getter(node.right, index)
            elif index < len(key) - 1:
                return getter(node.middle, index+1)
            else:
                return node

        if value:
            return putter
        else:
            return getter


tst = TernarySearchTree()
tst.put('apple', 1)
tst.put('admin', 2)
tst.put('cute', 3)

tst.get('cute')

def fib(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a
print(fib(10))
