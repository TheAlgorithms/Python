class Node:
    def __init__(self, val):
        self.val = val
        self.next = None  # Specify that next can be a Node or None


def remove(head: Node, n: int) -> Node:
    if head is None:
        return None  # If the head is None, return None

    # Create a dummy node that points to the head
    extra = Node(0)
    extra.next = head
    fast = extra  # Make sure fast can be None
    slow = extra  # Make sure slow can be None

    # Move fast ahead by n nodes
    for _ in range(n):
        if fast is not None:
            fast = fast.next

    # Move until fast reaches the end
    while fast is not None and fast.next is not None:
        fast = fast.next
        slow = slow.next

    # Remove the nth node from the end
    if slow is not None and slow.next is not None:
        slow.next = slow.next.next  # Link slow to the next of the node to be deleted

    return extra.next  # Return the new head, which may be None if the list is empty


def print_list(head: Node) -> None:
    curr = head
    while curr is not None:
        print(curr.val, end=" ")
        curr = curr.next
    print()  # for a new line


# Creating the linked list 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Print the original list
print("Original list:")
print_list(head)

# Remove the 5th node from the end (the head in this case)
head = remove(head, 5)

# Print the modified list
print("List after removing the 5th node from the end:")
print_list(head)
