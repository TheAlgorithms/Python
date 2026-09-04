class Node:
    """
    A class representing a node in a linked list.

    Attributes:
        data (int): The data stored in the node.
        next (Node | None): A reference to the next node in the linked list.
    """

    def __init__(self, data: int) -> None:
        self.data = data
        self.next: Node | None = None


def get_middle(head: Node | None) -> Node | None:
    """
    Find the node before the middle of the linked list
    using the slow and fast pointer technique.

    Parameters:
        head: The head node of the linked list.

    Returns:
        The node before the middle of the linked list,
        or None if the list has fewer than 2 nodes.

    Example:
    >>> head = Node(1)
    >>> head.next = Node(2)
    >>> head.next.next = Node(3)
    >>> middle = get_middle(head)
    >>> middle.data
    2
    """
    if head is None or head.next is None:
        return None

    slow: Node | None = head
    fast: Node | None = head.next

    while fast is not None and fast.next is not None:
        if slow is None:
            return None
        slow = slow.next
        fast = fast.next.next

    return slow


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
    """

    # Base Case: 0 or 1 node
    if head is None or head.next is None:
        return head

    # Split the linked list into two halves
    middle = get_middle(head)
    if middle is None or middle.next is None:
        return head

    next_to_middle = middle.next
    middle.next = None  # Split the list into two parts

    # Recursively sort both halves
    left = merge_sort_linked_list(head)
    right = merge_sort_linked_list(next_to_middle)

    # Merge sorted halves
    return merge(left, right)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
