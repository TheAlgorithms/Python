class Node:
    '''
    Objective : To create a node of Binary Search Tree.
    '''
    def __init__(self,value):
        '''
        Objective        : To initialize an object of Node.
        Input Parameters :
         self(Implicit Parameter) -> Object of class Node.
                             value-> Number that denotes value of node.
        Output           : None
        '''
        self.data=value
        self.right=None
        self.left=None

def Peek(stack):
    if len(stack)>0:
        return stack[-1]
    return -1

def Front(queue):
    if len(queue)>0:
        return queue[0]
    return -1

class BSTree:
    '''
    Objective : To create a Binary Search Tree.
    '''
    def __init__(self):
        '''
        Objective        : To initialize an object of class BSTree.
        Input Parameters :
         self(Implicit Parameter) -> Object of class BSTree.
        Output           : None
        '''
        self.root=None

    def InsertBST(self,value):
        '''
        Objective        : To insert a node in BST.
        Input Parameters :
         self(Implicit Parameter) -> Object of class BSTree.
                            value -> Value of node.
        Output           : None
        '''
        if self.root==None:
            self.root=Node(value)
        else:
            Root=self.root
            while Root!=None:
                if value<=Root.data:
                    if Root.left!=None:
                        Root=Root.left
                    else:
                        Root.left=Node(value)
                        return
                else:
                    if Root.right!=None:
                        Root=Root.right
                    else:
                        Root.right=Node(value)
                        return

    def InsertBSTRec(self,value,Root=None):
        '''
        Objective        : To insert a node in BST recursively.
        Input Parameters :
         self(Implicit Parameter) -> Object of class BSTree.
                            value -> Value of node.
                             Root -> temporary node to point root node of BST.
        Output           : None
        '''
        if self.root==None: self.root=Node(value)
        else:
            if Root==None: Root=self.root
            if value<=Root.data:
                if Root.left!=None:
                    self.InsertBSTRec(value,Root.left)
                else:
                    Root.left=Node(value)
            else:
                if Root.right!=None:
                    self.InsertBSTRec(value,Root.right)
                else:
                    Root.right=Node(value)

    def SearchBST(self , value , Root = -1):
        '''
        Objective        : To search a node in Binary Search Tree.
        Input Parameters :
         self(Implicit Parameter) -> Object of class BSTree.
                            value -> Value of node to be searched.
        Output           : Node
        '''
        if self.root == None : return self.root
        if Root == None : return Root
        else:
            if Root == -1 : Root = self.root
            if Root.data == value : return Root
            if value < Root.data:
                return self.SearchBST(value , Root.left)
            else:
                return self.SearchBST(value , Root.right)
       
    def DeleteLeafNode(self , node):
        '''
        Objective        : To delete a leaf node in Binary Search Tree.
        Input Parameters :
         self(Implicit Parameter) -> Object of class BSTree.
                            node ->  node to be deleted.
        Output           : None
        '''

        parent = self.root
        while parent.left!=node and parent.right!=node:
            if node.data < parent.data : parent = parent.left
            else : parent = parent.right

        if parent.left == node : parent.left = None
        else : parent.right = None
        del(node)


    def DeleteNodeWithOneChild(self , node):
        '''
        Objective        : To delete a node with one child in Binary Search Tree.
        Input Parameters :
         self(Implicit Parameter) -> Object of class BSTree.
                            node ->  node to be deleted.
        Output           : None
        '''
        if node.left != None :
            node.data = node.left.data
            node.left = None
        else :
            node.data = node.right.data
            node.right = None

    def DeleteNodeWithTwoChild(self , node):
        '''
        Objective        : To delete a node with two children in Binary Search Tree.
        Input Parameters :
         self(Implicit Parameter) -> Object of class BSTree.
                            node ->  node to be deleted.
        Output           : None
        '''
        successor = node.right
        while successor.left != None : successor = successor.left
        node.data = successor.data
        if successor.right == None : self.DeleteLeafNode(successor)
        else : self.DeleteNodeWithOneChild(successor)
        
   
    def DeleteBST(self , value):
        '''
        Objective        : To delete a node in Binary Search Tree.
        Input Parameters :
         self(Implicit Parameter) -> Object of class BSTree.
                            value -> Value of node to be deleted.
        Output           : None
        '''
        currnode = self.SearchBST(value)
        if currnode != None:
            if currnode.left == None and currnode.right == None : self.DeleteLeafNode(currnode)
            elif currnode.left == None or currnode.right == None : self.DeleteNodeWithOneChild(currnode)
            else : self.DeleteNodeWithTwoChild(currnode)
            return currnode
        else :
            return None
        
        
    def InOrderTraversal(self,Root=-1):
        '''
        Objective        : To perform InOrder traversal of BST.
        Input Parameters :
         self(Implicit Parameter) -> Object of class BSTree.
                            value -> Value of node.
                             Root -> temporary node to point root node of BST.
        Output           : None
        '''
        if self.root==None:
            return
        if Root==-1:
            Root=self.root
        if Root.left!=None:
            self.InOrderTraversal(Root.left)
        print(Root.data,end='  ')
        if Root.right!=None:
            self.InOrderTraversal(Root.right)


    def InOrderIterative(self):
        '''
        Objective        : To perform InOrder traversal of BST.
        Input Parameters :
         self(Implicit Parameter) -> Object of class BSTree.
                            value -> Value of node.
        Output           : None
        '''
        stack = []
        Inorder = []
        curr = self.root
        while len(stack)!=0 or curr!=None:
            if curr!=None:
                stack.append(curr)
                curr = curr.left
            else:
                #out = Peek(stack)
                out = stack[-1]
                Inorder.append(out.data)
                curr = out.right
                stack.pop()
        return Inorder
                
        

    def PreOrderTraversal(self,Root=-1):
        '''
        Objective        : To perform PreOrder traversal of BST.
        Input Parameters :
         self(Implicit Parameter) -> Object of class BSTree.
                            value -> Value of node.
                             Root -> temporary node to point root node of BST.
        Output           : None
        '''
        if self.root==None:
            return
        if Root==-1:
            Root=self.root
        print(Root.data,end='  ')
        if Root.left!=None:
            self.PreOrderTraversal(array,Root.left)
        
        if Root.right!=None:
            self.PreOrderTraversal(array,Root.right)

    def PreOrderIterative(self):
        '''
        Objective        : To perform PreOrder traversal of BST.
        Input Parameters :
         self(Implicit Parameter) -> Object of class BSTree.
        Output           : None
        '''
        Stack,Out = [],[]
        Stack.append(self.root)
        while len(Stack)!=0:
            #curr = Peek(Stack)
            curr = Stack[-1]
            Stack.pop()
            Out.append(curr)
            if curr.right:
                Stack.append(curr.right)
            if curr.left:
                Stack.append(curr.left)

        for i in Out:
            print(i.data,end='  ')
        

    def PostOrderTraversal(self,Root=-1):
        '''
        Objective        : To perform PostOrder traversal of BST.
        Input Parameters :
         self(Implicit Parameter) -> Object of class BSTree.
                            value -> Value of node.
                             Root -> temporary node to point root node of BST.
        Output           : None
        '''
        if self.root==None:
            return
        if Root==-1:
            Root=self.root
        if Root.left!=None:
            self.PostOrderTraversal(Root.left)
        
        if Root.right!=None:
            self.PostOrderTraversal(Root.right)
        print(Root.data,end='  ')

    

    def PostOrderIterative(self):
        '''
        Objective        : To perform PostOrder traversal of BST.
        Input Parameters :
         self(Implicit Parameter) -> Object of class BSTree.
                            value -> Value of node.
        Output           : None
        '''
        stack , out =[],[]
        stack.append(self.root)
        while len(stack)!=0:
            #curr = Peek(stack)
            curr = stack[-1]
            stack.pop()
            out.append(curr)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        for i in range(len(out)-1,-1,-1):
            print(out[i].data,end='  ')
            
            
    def LevelByLevelTraversal(self):
        '''
        Objective        : To perform Level by level traversal of BST.
        Input Parameters :
         self(Implicit Parameter) -> Object of class BSTree.
                            value -> Value of node.
        Output           : None
        '''
        queue = []
        queue.append(self.root)
        while len(queue)!=0:
            #curr = Front(queue)
            curr = queue[0]
            print(curr.data,end='  ')
            queue.pop(0)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            
        

    def MirrorImage(self , Root = -1):
        '''
        Objective        : To generate mirror image of BST.
        Input Parameters :
         self(Implicit Parameter) -> Object of class BSTree.
                             Root -> temporary node to point root node of BST.
        Output           : None
        '''
        
        if self.root == None :
            return
        if Root == None :
            return
        else:
            
            if Root == -1 : Root = self.root
            
            tmp = Root.left
            Root.left = Root.right
            Root.right = tmp
            self.MirrorImage(Root.left)
            self.MirrorImage(Root.right)
            
        
    def Height(self , Root = -1):
        '''
        Objective        : To determine height of BST.
        Input Parameters :
         self(Implicit Parameter) -> Object of class BSTree.
        Output           : positive number
        '''
        if self.root == None : return 0
        if Root == None : return 0
        else:
            if Root == -1 : Root = self.root
            return max(self.Height(Root.left) , self.Height(Root.right))+1


    def MaximumNode(self):
        '''
        Objective        : To determine max value node in BST.
        Input Parameters :
         self(Implicit Parameter) -> Object of class BSTree.
        Output           : None
        '''
        if self.root == None : return None
        Root = self.root
        while Root.right!= None:
            Root = Root.right
        return Root.data
        
    def CountNodes(self,Root=-1,count=0):
        '''
        Objective        : To count total nodes in BST.
        Input Parameters :
         self(Implicit Parameter) -> Object of class BSTree.
                             Root -> temporary node to point root node of BST.
                            count -> Temporary variable for counting
        Output           : None
        '''
        '''   
        if self.root==None:
            return 0
        if Root==None:return count
        else:
            if Root==-1:Root=self.root
            count+=1
            count=self.CountNodes(Root.left,count)
            count=self.CountNodes(Root.right,count)
        return count
        '''
        if self.root == None: return 0
        if Root == None : return 0
        else:
            if Root==-1:Root=self.root
            return self.CountNodes(Root.left)+self.CountNodes(Root.right)+1
            

    def CountLeafNodes(self,Root = -1):
        '''
        Objective        : To count leaf nodes in BST.
        Input Parameters :
         self(Implicit Parameter) -> Object of class BSTree.
                             Root -> temporary node to point root node of BST.
        Output           : Positive Number
        '''
        if self.root == None:
            return 0
        if Root == None:
            return 0
        else:
            if Root == -1 : Root = self.root
            if Root.left == None and Root.right == None:return 1
            return self.CountLeafNodes(Root.left) + self.CountLeafNodes(Root.right)
        
def HeapTemp(b,array,Root = -1):
    '''
    Objective        : Recursive Function to change value of root nodes during preorder traversal.
    Input Parameters :
                      b -> Binary Search Tree
                  array -> list of nodes traversed in INORDER
                   Root -> Temporary pointer
    Output           : None
    '''
    if b.root==None:
        return
    if Root==-1:
        Root=b.root
    Root.data = array[0]
    array.pop(0)
    if Root.left!=None:
        HeapTemp(b,array,Root.left)
        
    if Root.right!=None:
        HeapTemp(b,array,Root.right)

        
def MinHeap(b):
    '''
    Objective        : To convert Binary Search Tree to Min Heap.
    Input Parameters :
                  b -> Binary Search Tree
    Output           : None
    '''
    Array = b.InOrderIterative()
    HeapTemp(b,Array)
        
if __name__ == '__main__':
    '''
    print('**************************************BINARY  SEARCH  TREE *******************************')
    B=BSTree()
    ch = 'y'
    while ch in ['y' , 'Y']:
        print('\nFollowing Operations can be performed :')
        print('\n1. Insert a node \n2. Delete a node  \n3. InOrder Traversal  \n4. PreOrder Traversal  \n5. PostOrder Traversal   \n6. Level By Level Traversal   \n7. Height  \n8. Count Total nodes.   \n9. Count Leaf Nodes.  \n10. Search a node.   \n11. Produce Mirror Image  \n12. Exit  ')
        choice = int(input('\nEnter your choice : '))
        if choice == 1:
            try:
                ele = int(input('\nEnter value of node to be inserted : '))
            except:
                print('\nValue of key must be a number !!!')
            B.InsertBST(ele)
        elif choice == 2:
            try:
                ele = int(input('\nEnter value of node to be deleted : '))
            except:
                print('\nValue of key must be a number !!!')
            if B.DeleteBST(ele)!= None : print('\nSUCCESS !! NODE DELETED ')
            else : print('\nFAILURE !! NODE NOT PRESENT')
        elif choice == 3 :
            print('\n IN - ORDER TRAVERSAL:')
            B.InOrderTraversal()
        elif choice == 4 :
            print('\n PRE - ORDER TRAVERSAL:')
            B.PreOrderIterative()
        elif choice == 5 :
            print('\n POST - ORDER TRAVERSAL:')
            B.PostOrderIterative()
        elif choice == 6 :
            print('\n LEVEL BY LEVEL TRAVERSAL : ')
            B.LevelByLevelTraversal()
        elif choice == 7 :
            print('\nHEIGHT OF TREE :  ',B.Height())
        elif choice == 8:
            print('\nTotal number of nodes in BST : ',B.CountNodes())
        elif choice == 9:
            print('\nTotal number of leaf nodes in BST : ',B.CountLeafNodes())
        elif choice == 10:
            val = int(input('\nEnter value of node to be searched : '))
            node = B.SearchBST(val)
            if node != None:
                print('\nSearched Node : ',node.data ,'\nLeft child :',node.left.data if node.left != None else node.left,'\nRight child :',node.right.data if node.right != None else node.right )
            else:
                print('\nNode is not present !! ')
        elif choice == 11:
            B.MirrorImage()
            print('\nIn-Order traversal of mirror BST :\n')
            B.InOrderTraversal()
        else:
            break
        ch = input('\nDo you want to continue(y or Y for yes) ? ')
    '''
    B = BSTree()
    B.InsertBST(15)
    B.InsertBST(10)
    B.InsertBST(18)
    B.InsertBST(8)
    B.InsertBST(12)
    B.InsertBST(16)
    B.InsertBST(20)
    B.LevelByLevelTraversal()
    MinHeap(B)
    print('\nMIN HEAP :\n')
    B.LevelByLevelTraversal()
    
 
   

            
