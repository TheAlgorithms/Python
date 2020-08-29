"""Adding two integers of same length using Linked lists

Example add 321 + 248 = 569

(1)->(2)->(3) + (8)->(4)->(2) = (5)->(6)->(9) """


# node definition
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        # self.head=None

# linkedlist definition
class LL:
    def __init__(self):
        self.head=None

    # method to print the linked list
    def printLL(self):
        temp =self.head
        while(temp):
            print(temp.data ,end=" ")
            temp =temp.next

    # method to push a new node onto the linked list
    def push(self, newdata):
        newnode = Node(newdata)
        newnode.next = self.head
        self.head = newnode

    # method to add the nodes
    def add(self):
        carry = []  #to store carry generated if any
        carry.append(0)
        temp1 = llist.head
        temp2 = ll2.head
        while (temp1 and temp2):
            sums = temp1.data + temp2.data + carry[-1] #adding the latest element appended to the carry list
            if (sums >= 0 and sums <= 9):
                res.push(sums)
                carry.append(0)
            else:
                res.push(sums % 10)
                carry.append(int(sums / 10))

            temp1 = temp1.next
            temp2 = temp2.next

        if (carry[-1] != 0):  #if carry is generated : nonzero
            res.push(carry[-1]) #add it to the res list

llist = LL() #linkedlist 1
ll2=LL() #linkedlist 2
res=LL() #linkedlist representing addition of the nodes taken as an integer


# adding 321 and 248
llist.push(3)
llist.push(2)
llist.push(1)

ll2.push(2)
ll2.push(4)
ll2.push(8)

#Test case for carry generation handling
# llist.push(9)
# llist.push(9)
# llist.push(9)
# ll2.push(0)
# ll2.push(0)
# ll2.push(1)

llist.add()
res.printLL()
