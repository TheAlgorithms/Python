from typing import List, Optional


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


def create(A: List[int]) -> Optional[Node]:
    """
    Create a linked list from an array.

    Args:
        A (List[int]): The input array.

    Returns:
        Optional[Node]: The head of the linked list.

    Example:
        >>> A = [1, 3, 5, 7, 9, 11, 11, 15, 17, 19]
        >>> head = create(A)
        >>> display(head)
        1 3 5 7 9 11 15 17 19
    """
    if not A:
        return None

    head = Node(A[0])
    last = head

    for data in A[1:]:
        last.next = Node(data)
        last = last.next

    return head


def display(head: Optional[Node]) -> None:
    """
    Display the elements of a linked list.

    Args:
        head (Optional[Node]): The head of the linked list.

    Example:
        >>> A = [1, 3, 5, 7, 9, 11, 11, 15, 17, 19]
        >>> head = create(A)
        >>> display(head)
        1 3 5 7 9 11 11 15 17 19
    """
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


def count(head: Optional[Node]) -> int:
    """
    Count the number of nodes in a linked list.

    Args:
        head (Optional[Node]): The head of the linked list.

    Returns:
        int: The count of nodes.

    Example:
        >>> A = [1, 3, 5, 7, 9, 11, 11, 15, 17, 19]
        >>> head = create(A)
        >>> count(head)
        10
    """
    count = 0
    while head:
        count += 1
        head = head.next
    return count


def delete(head: Optional[Node], index: int) -> int:
    """
    Delete a node at a given index from a linked list.

    Args:
        head (Optional[Node]): The head of the linked list.
        index (int): The index at which the node should be deleted (1-based index).

    Returns:
        int: The data of the deleted node, or -1 if the index is out of range.

    Example:
        >>> A = [1, 3, 5, 7, 9, 11, 11, 15, 17, 19]
        >>> head = create(A)
        >>> delete(head, 3)
        5
    """
    if index < 1 or index > count(head):
        return -1

    if index == 1:
        data = head.data
        head = head.next
        return data
    else:
        prev = head
        current = head
        for _ in range(index - 1):
            prev = current
            current = current.next
        data = current.data
        prev.next = current.next
        return data


def remove_duplicates(head: Optional[Node]) -> None:
    """
    Remove duplicate elements from a sorted linked list.

    Args:
        head (Optional[Node]): The head of the linked list.

    Example:
        >>> A = [1, 3, 3, 5, 5, 7, 7, 9]
        >>> head = create(A)
        >>> remove_duplicates(head)
        >>> display(head)
        1 3 5 7 9
    """
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next


if __name__ == "__main__":
    print("Linked List!")

    A = [1, 3, 5, 7, 9, 11, 11, 15, 17, 19]
    head = create(A)

    remove_duplicates(head)
    display(head)
