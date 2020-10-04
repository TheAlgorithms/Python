# Program to print the elements of a linked list in reverse


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        """Returns a visual representation of the node and all its following nodes."""
        string_rep = ""
        temp = self
        while temp:
            string_rep += f"<{temp.data}> ---> "
            temp = temp.next
        string_rep += "<END>"
        return string_rep


def make_linked_list(elements_list):
    """Creates a Linked List from the elements of the given sequence
    (list/tuple) and returns the head of the Linked List."""

    # if elements_list is empty
    if not elements_list:
        raise Exception("The Elements List is empty")

    # Set first element as Head
    head = Node(elements_list[0])
    current = head
    # Loop through elements from position 1
    for data in elements_list[1:]:
        current.next = Node(data)
        current = current.next
    return head


def reverse_list(head_node):
    """Prints the elements of the given Linked List in reverse order"""
    # use 3 variable prev, next,head_node
    # If reached end of the List
    prev= None
    next_node= None
    if head_node is None:
        print("List Is Empty!!!")
        return None
    while head_node is not None:
        next_node= head_node.next
        head_node.next= prev
        prev= head_node
        head_node= next_node
    
    cur_node = prev
    print("Printing the reversed list ::")
    while cur_node is not None:
        print(cur_node.data)
        cur_node= cur_node.next
    
    # This prev is head of new reversed Linked list
    return prev
    # reverse them 


list_data = [14, 52, 14, 12, 43]
linked_list = make_linked_list(list_data)
print("Linked List:")
print(linked_list)
print("Elements in Reverse:")
reverse_list(linked_list)
