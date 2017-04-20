class BinarySearchTree:
    def __init__(self):
        """ create an empty binary search tree """
        self.root = None
        
    def put(self, key, value):
        """ add a new mapping between key and value to the BST """
        if self.root:
            self.root.put(key,value)
        else:
            self.root = TreeNode(key,value)
        
    def get(self, key):
        """ retrieve the value associated with the given key """
        if self.root:
            return self.root.get(key)
        else:
            return None
    
    def has_key(self, key):
        """ check if the node with the given key is in the tree """

        # the following assumes None is never stored with a key 
        
        return not self.get(key) is None      
    
    def delete(self, key):
        """ delete the node with the given key if it exists """
        if self.root:
            self.root = self.root.delete(key)
            
    def __iter__(self):
        """ returns an iterator for the binary search tree """

        class EmptyIterator:
            def next(self):
                raise StopIteration
            
        if self.root:
            # if the tree is not empty, just return the root's iterator
            return iter(self.root)
        else:
            # otherwise return the iterator that immediately raises
            # a StopIteration exception 
            return EmptyIterator()
        
            
class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None 
        
    def __iter__(self):
        """ return the iterator that iterates through the elements in the BST 
        rooted at this node in an inorder sequence """
        
        if self.left:
            # The following iterates through all the nodes in the left subtree. 
            
            # The first thing that python does when the for loop is encountered
            # is to obtain an iterator object for the left subtree.  
            # This is done ("under the covers") by recursively calling 
            # the __iter__ method on the left child. 
            for elt in self.left:         
                yield elt
                
        # at this point we "visit" the current node
        yield (self.key, self.val)
        
        if self.right:
            # we now visit all the nodes in the right subtree 
            for elt in self.right:
                yield elt
            
    def put(self, key, val):
        """ add a new mapping between key and value in the tree """
        if self.key == key:
            self.val = val              # replace existing value
        elif self.key > key:            # key belongs in left subtree 
            if self.left:
                self.left.put(key,val)
            else:                       # left subtree is empty
                self.left = TreeNode(key,val)
        else:                           # key belongs in right subtree 
            if self.right:
                self.right.put(key,val)
            else:                       # right subtree is empty
                self.right = TreeNode(key,val)
                
    def get(self, key):
        """ get the value associated with the key """
        if self.key == key:
            return self.val
        
        if self.key > key:              # key should be in the left subtree
            if self.left:
                return self.left.get(key)
            else:
                return None
        else:                           # key should be in the right subtree
            if self.right:
                return self.right.get(key)
            else:
                return None
            
    def delete(self, key):
        """ delete the node with the given key and return the 
        root node of the tree """
            
        if self.key == key:
            # found the node we need to delete
            
            if self.right and self.left: 
                
                # get the successor node and its parent 
                [psucc, succ] = self.right._findMin(self)
                
                # splice out the successor
                # (we need the parent to do this) 
                
                if psucc.left == succ:
                    psucc.left = succ.right
                else:
                    psucc.right = succ.right
                                
                # reset the left and right children of the successor
                
                succ.left = self.left
                succ.right = self.right
                
                return succ                
                
            else:
                # "easier" case
                if self.left:
                    return self.left    # promote the left subtree
                else:
                    return self.right   # promote the right subtree 
        else:
            if self.key > key:          # key should be in the left subtree
                if self.left:
                    self.left = self.left.delete(key)
                # else the key is not in the tree 
                    
            else:                       # key should be in the right subtree
                if self.right:
                    self.right = self.right.delete(key)
                    
        return self
    
    def _findMin(self, parent):
        """ return the minimum node in the current tree and its parent """

        # we use an ugly trick: the parent node is passed in as an argument
        # so that eventually when the leftmost child is reached, the 
        # call can return both the parent to the successor and the successor
        
        if self.left:
            return self.left._findMin(self)
        else:
            return [parent, self]
        
        
def preorder(root):
    if root:
        print root.key
        preorder(root.left)
        preorder(root.right)

        
def postorder(root):
    if root:        
        postorder(root.left)
        postorder(root.right)
        print root.key
        
def inorder(root):
    if root:
        inorder(root.left)
        print root.key
        inorder(root.right)
        
        
def print_tree(root):
    '''Print the tree rooted at root.'''
    print_helper(root, "")


def print_helper(root, indent):
    '''Print the tree rooted at BTNode root. Print str indent (which
    consists only of whitespace) before the root value; indent more for the
    subtrees so that it looks nice.'''
    if root is not None:
        print_helper(root.right, indent + "   ")
        print indent + str(root.key)
        print_helper(root.left, indent + "   ")


tree = BinarySearchTree()
line = raw_input("command> ")
while line != "quit":
    cmdlist = line.split()
    if cmdlist != []:
        cmd = cmdlist[0]
        if cmd == "has_key":
            print tree.has_key(int(cmdlist[1]))
        elif cmd == "put":
            if len(cmdlist) == 2:
                val = "default"
            else:
                val = cmdlist[2]
            tree.put(int(cmdlist[1]),val)
            print_tree(tree.root)
        elif cmd == "get":
            print tree.get(int(cmdlist[1]))
        elif cmd == "delete":
            tree.delete(int(cmdlist[1]))
            print_tree(tree.root)
        elif cmd == "iterate":
            for elt in tree:
                print elt
        
    line = raw_input("command> ")
        