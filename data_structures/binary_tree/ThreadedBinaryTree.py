class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        self.lthread = True
        self.rthread = True

class ThreadedTree:
    def __init__(self):
        self.root = None

    def Insert(self , key):
        ptr = self.root
        if ptr!=None and ptr.data == key:
            return 'DUPLICATE KEY!!!'
        while ptr!=None:
            if key<ptr.data :
                if ptr.lthread == False :
                    ptr = ptr.left
                else :
                    break
            else :
                if ptr.rthread == False :
                    ptr = ptr.right
                else :
                    break

        temp = Node(key)
        if ptr == None :
            self.root = temp

        elif key < ptr.data :            #Left Child
            temp.left = ptr.left
            temp.right = ptr
            ptr.lthread = False
            ptr.left = temp

        else :
            temp.left = ptr
            temp.right = ptr.right
            ptr.rthread = False
            ptr.right = temp


    def LeftMost(self , currnode):
        if currnode == None : return None
        while currnode.lthread == False :
            currnode = currnode.left
        return currnode

    def InOrder(self):
        curr = self.LeftMost(self.root)
        while curr!=None :
            print(curr.data,end = '  ')
            if curr.rthread :
                curr = curr.right
            else :
                curr = self.LeftMost(curr.right)

if __name__ == '__main__':

    t = ThreadedTree()
    t.Insert(6)
    t.Insert(3)
    t.Insert(8)
    t.Insert(1)
    t.Insert(5)
    t.Insert(7)
    t.Insert(11)
    t.Insert(9)
    t.Insert(13)
    t.InOrder()
        
        
