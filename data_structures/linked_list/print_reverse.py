from __future__ import annotations


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        """Returns a visual representation of the node and all its following nodes."""
        string_rep = []
        temp = self
        while temp:
            string_rep.append(f"{temp.data}")
            temp = temp.next
        return "->".join(string_rep)


def make_linked_list(elements_list: list):
    """Creates a Linked List from the elements of the given sequence
    (list/tuple) and returns the head of the Linked List.
    >>> make_linked_list([])
    Traceback (most recent call last):
        ...
    Exception: The Elements List is empty
    >>> make_linked_list([7])
    7
    >>> make_linked_list(['abc'])
    abc
    >>> make_linked_list([7, 25])
    7->25
    """
    if not elements_list:
        raise Exception("The Elements List is empty")

    current = head = Node(elements_list[0])
    for i in range(1, len(elements_list)):
        current.next = Node(elements_list[i])
        current = current.next
    return head


def print_reverse(head_node: Node) -> None:
    """Prints the elements of the given Linked List in reverse order
    >>> print_reverse([])
    >>> linked_list = make_linked_list([69, 88, 73])
    >>> print_reverse(linked_list)
    73
    88
    69
    """
    if head_node is not None and isinstance(head_node, Node):
        print_reverse(head_node.next)
        print(head_node.data)


def main():
    from doctest import testmod

    testmod()

    linked_list = make_linked_list([14, 52, 14, 12, 43])
    print("Linked List:")
    print(linked_list)
    print("Elements in Reverse:")
    print_reverse(linked_list)


if __name__ == "__main__":
    main()
