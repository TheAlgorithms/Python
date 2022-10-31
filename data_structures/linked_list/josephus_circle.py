'''
Josephus Circle:
Let there be N people standing in a circle waiting to be executed. The counting out begins at some point in the circle and proceeds around the circle in a fixed direction. In each step, a certain number of people are skipped and the next person is executed. The elimination proceeds around the circle (which is becoming smaller and smaller as the executed people are removed), until only the last person remains, who is given freedom. 
'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class circle:
    def __init__(self):
        self.head=None

    def insert(self,data):
        new=node(data)
        new.next=self.head
        temp=self.head
        if self.head==None:
            new.next=new
            self.head=new
        else:
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new

    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
            if temp==self.head:
                break

    def eliminate(self,n,k):
        '''
        This function eliminates the kth number
        from the list
        '''
        temp=self.head
        for _ in range(n-1):
            for _ in range(k):
                temp=temp.next
            prev=temp.next.next
            temp.next=prev
        self.head=temp

list=circle()
n,k=map(int,input().split())
for i in range(1,n+1):
    list.insert(i)
print("Numbers standing in the josephus circle:")
list.print_list()
print("\n")
list.eliminate(n,k)
print("The last standing one is: ",end="")
list.print_list()