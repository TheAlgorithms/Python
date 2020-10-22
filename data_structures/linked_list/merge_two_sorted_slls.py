#Define class Node to represent a single node in a LinkedList
#value is the value, or data, of the node
#next is a pointer to the next linked node in the Singly LinkedList
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


#Keep track of a LinkedList using its head node
def mergeLists(list1head, list2head):
    dummy = Node(0)

    #Keep track of the current Node that we will append the next todo
    #The current represents the tail of our output list
    current=dummy

    while True:
        #If one of the lists is completely empty
        #Append the rest of the second LinkedList
        if list1head is None:
            current.next=list2head
            break
        if list2head is None:
            current.next=list1head
            break

        #Comparing the value of the next node in the two LinkedLists
        #Append the node with the smaller value to our current list
        if list1head.value<=list2head.value:
            current.next=list1head
            list1head=list1head.next
        else:
            current.next=list2head
            list2head=list2head.next

        current=current.next

    # Remove the dummy node before returning the LinkedList
    dummy=dummy.next()
    return dummy
