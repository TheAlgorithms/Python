# Given a singly linked list L0 -> L1 -> … -> Ln-1 -> Ln. 
# Reorder the nodes in the list so that the new formed list is : L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 … 
# Time Complexity : O(n) 
# Auxiliary Space : O(1) 

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

    
# Function for rearranging a linked list with high and low value 
def rearrange(head):
    # Base case
    if (head == None):
        return head
 
    # Two pointer variable
    prev, curr = head, head.next
 
    while (curr):
 
        # Swap function for swapping data
        if (prev.data > curr.data):
            prev.data, curr.data = curr.data, prev.data
 
        # Swap function for swapping data
        if (curr.next and curr.next.data > curr.data):
            curr.next.data, curr.data = curr.data, curr.next.data
 
        prev = curr.next
 
        if (not curr.next):
            break
 
        curr = curr.next.next
 
    return head


# Function to insert a node in the linked list at the beginning 
def push(head, k):
    tem = Node(k)
    tem.data = k
    tem.next = head
    head = tem
    return head

  
# Function to display node of linked list 
def display(head):
    curr = head
 
    while (curr != None):
        print(curr.data, end=" ")
        curr = curr.next
 
 
# Driver code
if __name__ == '__main__':
    head = None
 
    # Let create a linked list
    # 9 . 6 . 8 . 3 . 7
    head = push(head, 7)
    head = push(head, 3)
    head = push(head, 8)
    head = push(head, 6)
    head = push(head, 9)
 
    head = rearrange(head)
 
    display(head)
 
