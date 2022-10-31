class Node: 
    def __init__(self,data): 
        self.data=data 
        self.prev=None 
        self.next=None 

        
class CDLL: 
    def __init__(self): 
        self.head=None 
        self.tail=None 
        
    def find(self,val): 
        if(self.head==None): 
            return False 
        temp=self.head 
        while(temp.next!=self.head): 
            if(temp.data==val): 
                return True 
            temp=temp.next 
        if(temp.data==val): 
            return True 
        return False   
    
    def append(self,val): 
        node=Node(val)
        if(self.head==None):       
            self.head=self.tail=node  
            self.head.prev=self.tail
            self.tail.next=self.head    
            return 
        node.next=self.head 
        self.head.prev=node 
        node.prev=self.tail 
        self.tail.next=node 
        self.tail=node 
        
    def push(self,val): 
        node=Node(val) 
        if(self.head==None): 
            self.head=self.tail=node
            self.head.prev=self.tail 
            self.tail.next=self.head
            return 
        node.prev=self.tail 
        self.tail.next=node
        node.next=self.head 
        self.head.prev=node 
        self.head=node 
        
    def pop(self): 
        if(self.head==None): 
            return 
        if(self.head==self.tail): 
            self.head=None 
            return 
        temp=self.head
        while(temp.next.next!=self.head): 
            temp=temp.next 
        temp.next=self.head
        self.head.prev=temp 
        self.tail=temp 
        
    def popFront(self): 
        if(self.head==None): 
            return 
        if(self.head==self.tail): 
            self.head=None 
            return 
        self.tail.next=self.head.next    
        self.head=self.head.next 
        
    def traverse(self): 
        if(self.head==None): 
            print("None")
            return 
        temp=self.head 
        while(temp.next!=self.head): 
            print(temp.data,end=" <-> ") 
            temp=temp.next 
        print(temp.data,end=" <-> ")
        print()

        
 # Modify the below lines of code, as per requirement.
li=CDLL()
li.append(5)
li.append(4)
li.push(6)
li.push(7)
li.push(8)
li.pop()
li.popFront()
li.traverse()
