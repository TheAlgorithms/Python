class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def pushAtHead(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    # **deletion code starts**
    def deleteNode(self, key):
        temp = self.head
        while temp.next:
            if temp.next.data == key:       #if next node is the node what we want to delete
                temp.next = temp.next.next  #breaking the link of node which has to be deleted
            temp = temp.next                #if condition not satisy then go to next node
    # **deletion code ends**
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("NULL")

if __name__=='__main__':
    myObj = LinkedList()
    myObj.pushAtHead(4)
    myObj.pushAtHead(3)       
    myObj.pushAtHead(2)       
    myObj.pushAtHead(1)
    myObj.pushAtHead(0)
    print("List before deleting the node: ")
    myObj.printList()
    myObj.deleteNode(3)
    print("List after deleting the node: ")
    myObj.printList()

