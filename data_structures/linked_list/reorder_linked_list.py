# Given a singly linked list L0 -> L1 -> … -> Ln-1 -> Ln. 
# Reorder the nodes in the list so that the new formed list is : L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 … 
# Time Complexity : O(n) 
# Auxiliary Space : O(1) 

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


# Function for rearranging a linked list with high and low value 
def reorder(head):
    # Base case
    if (head == None):
        return head

    # Two pointer variable
    prev, curr = head, head.next

    while (curr):

        # swapping data
        if (prev.data > curr.data):
            prev.data, curr.data = curr.data, prev.data

        # swapping data
        if (curr.next and curr.next.data > curr.data):
            curr.next.data, curr.data = curr.data, curr.next.data

        prev = curr.next

        if (not curr.next):
            break

        curr = curr.next.next

    return head


# Function to insert a node in the linked list at the beginning 
def push(head, val):
    temp = Node(val)
    temp.data = val
    temp.next = head
    head = temp
    return head


# Function to display node of linked list 
def show(head):
    curr = head

    while (curr != None):
        print(curr.data, end=" ")
        curr = curr.next


# Driver code
if __name__ == '__main__':
    head = None

    # Create a linked list
    # 1 . 5 . 7 . 8 . 9 
    head = push(head, 9)
    head = push(head, 8)
    head = push(head, 7)
    head = push(head, 5)
    head = push(head, 1)

    # Rearranging a linked list with high and low value
    head = reorder(head)

    # Display the linked List 
    show(head)
