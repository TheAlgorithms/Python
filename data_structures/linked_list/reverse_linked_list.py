"""
Linked List is described as a bunch of nodes connected to one another.
For this scenario, this is intended for a single Linked List.
"""

from typing import Any, Optional


class Node:
    """
    This class forms the backbone of a data structure called Linked List.
    """

    def __init__(self, item: Any, next: Any = None) -> None:
        self.item = item
        self.next = next

    def __repr__(self) -> str:
        """
        This is here for debugging/testing purposes. This is used to convert the
        nodes and its branch to string.
        """
        if self.next is not None:
            return f"{str(self.item)}, {self.next.__repr__()}"
        else:
            return str(self.item)


def reverse_linked_list(input: Optional[Node]) -> Optional[Node]:
    """
    This function reverse the order of the given linked list.
    >>> reverse_linked_list(Node(1, Node(2, Node(3))))
    3, 2, 1
    >>> reverse_linked_list(None) # it returns None
    >>> reverse_linked_list(Node('First', Node('Second')))
    Second, First
    """
    # If input is None, return None.
    if input is None:
        return None

    # This algorithm works by popping items from input, and then pushing
    # the popped item to output.

    temp = input  # backup the input. We don't want to change the input.

    # Pop the first node.
    output = Node(temp.item)
    temp = temp.next

    # Pop data off temp and push them into output until temp has no more data.
    while temp is not None:
        output = Node(temp.item, output)
        temp = temp.next

    # Return the output
    return output


if __name__ == "__main__":
    """
    Running this file independently will perform assertion.

    Input and Expected tests:
    - [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]
    - [-9, 100, 7, 5555, 0] -> [0, 5555, 7, 100, -9]
    - [-100, -200, -300] -> [-300, -200, -100]
    - None -> None
    - [10] -> [10]
    - [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 0] ->
      [0, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    """

    import doctest

    doctest.testmod()

    input = [
        Node(1, Node(2, Node(3, Node(4, Node(5))))),
        Node(-9, Node(100, Node(7, Node(5555, Node(0))))),
        Node(-100, Node(-200, Node(-300))),
        None,
        Node(10),
        Node(
            10,
            Node(
                20,
                Node(
                    30,
                    Node(
                        40,
                        Node(
                            50,
                            Node(60, Node(70, Node(80, Node(90, Node(100, Node(0)))))),
                        ),
                    ),
                ),
            ),
        ),
    ]

    expected = [
        Node(5, Node(4, Node(3, Node(2, Node(1))))),
        Node(0, Node(5555, Node(7, Node(100, Node(-9))))),
        Node(-300, Node(-200, Node(-100))),
        None,
        Node(10),
        Node(
            0,
            Node(
                100,
                Node(
                    90,
                    Node(
                        80,
                        Node(
                            70,
                            Node(60, Node(50, Node(40, Node(30, Node(20, Node(10)))))),
                        ),
                    ),
                ),
            ),
        ),
    ]

    # Assert them here.
    for i, e in zip(input, expected):
        result = reverse_linked_list(i)
        assert str(result) == str(
            e
        ), f"Assert Failed. Result: [{str(result)}]. Expected: [{str(e)}]"

    # Indicate successful test.
    print("Assertion for Reverse Linked List is successful.")
