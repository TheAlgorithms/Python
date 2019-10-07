# Node class for node creation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# A function to print a Linked List using recursion
def print_linkedlist_spl(head):

  if head is None:
    return None
   
  return print_linkedlist_spl(head.next), print(head.data, end = " ")    
    
# Converting an input array to a linked list
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


from sys import setrecursionlimit
setrecursionlimit(10000)            # setting recursion limit as 10**4 (at pax)

n = int(input('Enter number of elements: '))
arr=list(int(i) for i in input().strip().split(' ')[:n])          # reading input array
l = ll(arr)                                                   # passing entire input array to linked list creation 
print_linkedlist_spl(l)
