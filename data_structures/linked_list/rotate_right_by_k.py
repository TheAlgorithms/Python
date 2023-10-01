from __future__ import annotations
from doctest import testmod


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


def insert_node(head: Node, data: int) -> Node:
    """
    Returns new head of linked list after inserting new node
    """
    new_node = Node(data)
    if head == None:
        head = new_node
        return head
    temp_node = head
    while temp_node.next != None:
        temp_node = temp_node.next
    temp_node.next = new_node
    return head


def right_rotate_by_k(head: Node, k: int) -> Node:
    """
    This function receives head and k as input parameters and returns head of linked list after rotation to the right by k places
    """
    if head == None or head.next == None:
        return head
    for _ in range(k):
        temp_node = head
        while temp_node.next.next != None:
            temp_node = temp_node.next
        end = temp_node.next
        temp_node.next = None
        end.next = head
        head = end
    return head


# utility function to print list
def print_list(head: Node) -> None:
    """
    Prints the entire linked list iteratively
    """
    while head.next != None:
        print(head.data, end="->")
        head = head.next
    print(head.data)
    return


def main() -> None:
    head = None

    head = insert_node(head, 1)
    head = insert_node(head, 2)
    head = insert_node(head, 3)
    head = insert_node(head, 4)
    head = insert_node(head, 5)

    print("Original list: ", end="")
    print_list(head)

    k = 2

    new_head = right_rotate_by_k(head, k)

    print("After", k, "iterations: ", end="")
    print_list(new_head)


if __name__ == "__main__":
    testmod(name="main", verbose=True)
    testmod(name="insert_node", verbose=True)
    testmod(name="print_list", verbose=True)
    main()
