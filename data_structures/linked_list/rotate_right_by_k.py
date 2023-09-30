class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# function to insert node at the end of the linked list
def insertNode(head, data):
    """Returns new head of linked list after inserting new node"""
    newNode = Node(data)
    if head == None:
        head = newNode
        return head
    tempNode = head
    while tempNode.next != None:
        tempNode = tempNode.next
    tempNode.next = newNode
    return head


# function to rotate list by k times
def rightRotateByK(head, k):
    """This function receives head and k as input parameters and returns head of linked list after rotation to the right by k places"""
    if head == None or head.next == None:
        return head
    for _ in range(k):
        tempNode = head
        while tempNode.next.next != None:
            tempNode = tempNode.next
        end = tempNode.next
        tempNode.next = None
        end.next = head
        head = end
    return head


# utility function to print list
def printList(head):
    """Prints the entire linked list iteratively"""
    while head.next != None:
        print(head.data, end="->")
        head = head.next
    print(head.data)
    return


if __name__ == "__main__":
    head = None
    # inserting Nodes 1,2,3,4,5 to form a linked list for example
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 3)
    head = insertNode(head, 4)
    head = insertNode(head, 5)

    print("Original list: ", end="")
    printList(head)

    k = 2
    # calling function for rotating right of the nodes by k times
    newHead = rightRotateByK(head, k)

    print("After", k, "iterations: ", end="")
    printList(newHead)  # list after rotating nodes
