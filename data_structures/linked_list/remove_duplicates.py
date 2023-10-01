class Node:
    def __init__(self, data: int = None):
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


def create(arr: list[int]) -> Node:
    """
    Creates a linked list from an array and returns the head of the linked list.

    Args:
        arr (list[int]): The array of integers.

    Returns:
        Node: The head of the linked list.

    Example:
        >>> arr = [1, 3, 5, 7, 9, 11, 11, 15, 17, 19]
        >>> head = create(arr)
        >>> head.data
        1
        >>> head.next.data
        3
    """
    if not arr:
        raise ValueError("The array is empty")

    head = Node(arr[0])
    current = head

    for data in arr[1:]:
        current.next = Node(data)
        current = current.next

    return head


def display(head: Node) -> str:
    """
    Display the elements of the linked list.

    Args:
        head (Node): The head of the linked list.

    Returns:
        str: A visual representation of the linked list.

    Example:
        >>> arr = [1, 3, 5, 7, 9]
        >>> head = create(arr)
        >>> display(head)
        '<1> ---> <3> ---> <5> ---> <7> ---> <9> ---> <END>'
    """
    result = ""
    current = head
    while current:
        result += f"<{current.data}> ---> "
        current = current.next
    result += "<END>"
    return result


def count(head: Node) -> int:
    """
    Count the number of nodes in the linked list.

    Args:
        head (Node): The head of the linked list.

    Returns:
        int: The count of nodes in the linked list.

    Example:
        >>> arr = [1, 3, 5, 7, 9]
        >>> head = create(arr)
        >>> count(head)
        5
    """
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count


def delete(head: Node, index: int) -> int:
    """
    Delete a node at a given index from the linked list and return its value.

    Args:
        head (Node): The head of the linked list.
        index (int): The index at which the node should be deleted (1-based index).

    Returns:
        int: The value of the deleted node.

    Example:
        >>> arr = [1, 3, 5, 7, 9]
        >>> head = create(arr)
        >>> delete(head, 3)
        5
        >>> display(head)
        '<1> ---> <3> ---> <7> ---> <9> ---> <END>'
    """
    if index < 1 or index > count(head):
        return -1

    if index == 1:
        value = head.data
        head = head.next
        return value
    else:
        current = head
        for _ in range(index - 2):
            current = current.next
        value = current.next.data
        current.next = current.next.next
        return value


def remove_duplicates(head: Node):
    """
    Remove duplicates from a sorted linked list.

    Args:
        head (Node): The head of the sorted linked list.

    Example:
        >>> arr = [1, 3, 3, 5, 5, 7]
        >>> head = create(arr)
        >>> remove_duplicates(head)
        >>> display(head)
        '<1> ---> <3> ---> <5> ---> <7> ---> <END>'
    """
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 11, 15, 17, 19]
    head = create(arr)
    remove_duplicates(head)
    print("Linked List:")
    print(display(head))
