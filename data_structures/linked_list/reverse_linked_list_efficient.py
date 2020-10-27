class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

    
    def __repr__(self):
        # Returns a visual representation of the node and all its following nodes.
        string_rep = []
        temp = self
        while temp:
            string_rep.append(f"{temp.data}")
            temp = temp.next
        return "->".join(string_rep)

def make_linked_list(elements_list):
    """Creates a Linked List from the elements of the given sequence
    (list/tuple) and returns the head of the Linked List.
    >>> make_linked_list([7])
    7
    >>> make_linked_list(['abc'])
    abc
    >>> make_linked_list([7, 25])
    7->25
    """
    current = head = Node(elements_list[0])
    for i in range(1, len(elements_list)):
        current.next = Node(elements_list[i])
        current = current.next
    return head


def reverse_linked_list_efficient(head):
    """Prints the elements of the given Linked List in reverse order
    >>> linked_list = make_linked_list([69, 88, 73])
    >>> reverse_linked_list_efficient(linked_list)
    73->88->69
    """
    if head==None:
        return None
    temp1, temp2 = None, head
    while temp2!=None:
        temp3 = temp2.next
        temp2.next = temp1
        temp1 = temp2
        temp2 = temp3
    head = temp1
    return head

def main():
    from doctest import testmod
    testmod()
    linked_list = make_linked_list([1,2,3,4,5])
    print('Linked List:', linked_list)
    linked_list = reverse_linked_list_efficient(linked_list)
    print('Reversed Linked List:', linked_list)

if __name__ == "__main__":
    main()