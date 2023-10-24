# class node to store data and next
class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    # defining getter and setter for data and next
    def getdata(self):
        return self.data

    def setdata(self, data):
        self.data = data

    def getnextnode(self):
        return self.next

    def setnextnode(self, node):
        self.next = node


# class Linked List
class linkedlist:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def getsize(self):
        return self.size

    def addnode(self, data):
        node = node(data, self.head)
        self.head = node
        # incrementing the size of the linked list
        self.size += 1
        return True

    # delete a node from linked list
    def removenode(self, value):
        prev = None
        curr = self.head
        while curr:
            if curr.getdata() == value:
                if prev:
                    prev.setnextnode(curr.getnextnode())
                else:
                    self.head = curr.getnextnode()
                return True

            prev = curr
            curr = curr.getnextnode()

        return False

    # find a node in the linked list
    def findnode(self, value):
        curr = self.head
        while curr:
            if curr.getdata() == value:
                return True
            else:
                curr = curr.getnextnode()
        return False

    # print the linked list
    def printll(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getnextnode()


myList = linkedlist()
print("Inserting")
print(myList.addnode(5))
print(myList.addnode(15))
print(myList.addnode(25))

myList.printll()

print(myList.getsize())

print(myList.findnode(25))

print(myList.removenode(25))

myList.printll()
