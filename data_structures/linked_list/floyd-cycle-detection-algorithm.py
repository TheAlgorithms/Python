class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


# initialize a new head for the linked list
head = None

# detect if there is a loop
# in the linked list
def detectLoop(head):
    slowPointer = head
    fastPointer = head

    while slowPointer != None and fastPointer != None and fastPointer.next != None:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
        if slowPointer == fastPointer:
            return 1

    return 0


# inserting new values
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

# adding a loop for the sake
# of this example
temp = head
while temp.next != None:
    temp = temp.next

temp.next = head

# loop added;
if detectLoop(head):
    print("Loop exists in the Linked List")
else:
    print("Loop does not exists in the Linked List")
