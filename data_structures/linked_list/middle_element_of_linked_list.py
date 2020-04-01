# From Google Find the middle element of a linked list.....

#Node Setup
class Node:

    def __init__(self, data, next):

        self.data = data
        self.next = next

# setup some nodes and connect them to each other
# the linked list looks like:
# (head) n5 -> n4 -> n3 -> n2 -> n1 -> None

if __name__ == "__main__":
    node1 = Node("hello", None)
    node2 = Node("Deniel", node1)
    node3 = Node("Blue", node2)
    node4 = Node("Green", node3)
    node5 = Node("Me", node4)

    # assign a node to the head which functions
    # as the entry into our linked list

    head = node5

    # setup pointers to both start
    # at the head of the linked list

    fastPointer = head
    slowPointer = head

    # loop through the linked list
    # when fastPointer reaches the end of the list
    # then slowPointer will be at the middle node

    while fastPointer.next != None and fastPointer.next.next != None:
        fastPointer = fastPointer.next.next
        slowPointer = slowPointer.next

    # slowPointer is now at the middle node in the linked list
    print(slowPointer.data)
