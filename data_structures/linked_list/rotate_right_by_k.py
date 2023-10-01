from __future__ import annotations


class Node:
    def __init__(self, data:int):
        self.data = data
        self.next = None


def insertNode(head:Node, data:int) -> Node:
    '''
    Returns new head of linked list after inserting new node
    '''
    newNode = Node(data)
    if head == None:
        head = newNode
        return head
    tempNode = head
    while tempNode.next != None:
        tempNode = tempNode.next
    tempNode.next = newNode
    return head

def rightRotateByK(head:Node, k:int) -> Node:
    '''
    This function receives head and k as input parameters and returns head of linked list after rotation to the right by k places
    '''
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
def printList(head:Node) -> None:
    '''
    Prints the entire linked list iteratively
    '''
    while head.next != None:
        print(head.data, end='->')
        head = head.next
    print(head.data)
    return

def main():
    from doctest import testmod

    testmod()
    head = None
    
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 3)
    head = insertNode(head, 4)
    head = insertNode(head, 5)


    print("Original list: ", end='')
    printList(head)

    k = 2
    
    newHead = rightRotateByK(head, k)


    print("After", k, "iterations: ", end='')
    printList(newHead)   


if __name__ == '__main__':
    main()
    