class Node:
    """
    A class representing a node in a linked list.

    Attributes:
        data (int): The data stored in the node.
        next (Node | None): A reference to the next node in the linked list.

    >>> head = Node(4)
    >>> head.next = Node(2)
    >>> head.next.next = Node(1)
    >>> head.next.next.next = Node(3)
    >>> sorted_head = merge_sort_linked_list(head)
    >>> print_linked_list(sorted_head)
    1 2 3 4
    """

    def __init__(self, data: int):
        self.data = data
        self.next: Node | None = None


def get_middle(head: Node) -> Node:
    """
    Find the middle node of the linked list using the slow and fast pointer technique.

    Parameters:
        head: The head node of the linked list.

    Returns:
        The middle node of the linked list.

    Example:
    >>> head = Node(1)
    >>> head.next = Node(2)
    >>> head.next.next = Node(3)
    >>> get_middle(head).data
    2
    """

    if head is None:
        return head

    slow = head  # one node at a time
    fast = head  # two nodes at a time
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge(left: Node | None, right: Node | None) -> Node | None:
    """
    Merge two sorted linked lists into one sorted linked list.

    Parameters:
        left: The head of the first sorted linked list.
        right: The head of the second sorted linked list.

    Returns:
        The head of the merged sorted linked list.

    Example:
    >>> left = Node(1)
    >>> left.next = Node(3)
    >>> right = Node(2)
    >>> right.next = Node(4)
    >>> merged = merge(left, right)
    >>> print_linked_list(merged)
    1 2 3 4
    """

    if left is None:
        return right
    if right is None:
        return left

    if left.data <= right.data:
        result = left
        result.next = merge(left.next, right)
    else:
        result = right
        result.next = merge(left, right.next)

    return result


def print_linked_list(head: Node | None) -> None:
    """
    Print the linked list in a single line.

    Parameters:
        head: The head node of the linked list.

    Example:
    >>> head = Node(1)
    >>> head.next = Node(2)
    >>> head.next.next = Node(3)
    >>> print_linked_list(head)
    1 2 3
    """

    current = head
    first = True  # To avoid printing space before the first element
    while current:
        if not first:
            print(" ", end="")
        print(current.data, end="")
        first = False
        current = current.next
    print()


def merge_sort_linked_list(head: Node | None) -> Node | None:
    """
    Sort a linked list using the Merge Sort algorithm.

    Parameters:
        head: The head node of the linked list to be sorted.

    Returns:
        The head node of the sorted linked list.

    Example:
    >>> head = Node(4)
    >>> head.next = Node(2)
    >>> head.next.next = Node(1)
    >>> head.next.next.next = Node(3)
    >>> sorted_head = merge_sort_linked_list(head)
    >>> print_linked_list(sorted_head)
    1 2 3 4

    >>> head = Node(1)
    >>> head.next = Node(2)
    >>> head.next.next = Node(3)
    >>> head.next.next.next = Node(4)
    >>> sorted_head = merge_sort_linked_list(head)
    >>> print_linked_list(sorted_head)
    1 2 3 4

    >>> head = Node(10)
    >>> head.next = Node(3)
    >>> head.next.next = Node(5)
    >>> head.next.next.next = Node(1)
    >>> sorted_head = merge_sort_linked_list(head)
    >>> print_linked_list(sorted_head)
    1 3 5 10
    """

    # Base Case: 0 or 1 node
    if head is None or head.next is None:
        return head

    # Split the linked list into two halves
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None  # Split the list into two parts

    left = merge_sort_linked_list(head)  # Sort the left half
    right = merge_sort_linked_list(next_to_middle)  # Sort the right half
    sorted_list = merge(left, right)  # Merge the sorted halves
    return sorted_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
