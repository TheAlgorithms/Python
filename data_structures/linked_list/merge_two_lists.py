"""
Algorithm that merges two sorted linked lists into one sorted linked list.

https://en.wikipedia.org/wiki/Linked_list
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

test_data_odd = (3, 9, -11, 0, 7, 5, 1, -1)
test_data_even = (4, 6, 2, 0, 8, 10, 3, -2)


@dataclass
class Node:
    data: int
    next: Optional[Node]


class SortedLinkedList:
    def __init__(self, ints: List[int]) -> None:
        self.head: Optional[Node] = None
        for i in reversed(sorted(ints)):
            self.head = Node(i, self.head)

    def __iter__(self):
        """
        >>> tuple(SortedLinkedList(test_data_odd)) == tuple(sorted(test_data_odd))
        True
        >>> tuple(SortedLinkedList(test_data_even)) == tuple(sorted(test_data_even))
        True
        """
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __len__(self):
        """
        >>> for i in range(3):
        ...     len(SortedLinkedList(range(i))) == i
        True
        True
        True
        >>> len(SortedLinkedList(test_data_odd))
        8
        """
        return len(tuple(iter(self)))

    def __str__(self):
        """
        >>> str(SortedLinkedList([]))
        ''
        >>> str(SortedLinkedList(test_data_odd))
        '-11 -> -1 -> 0 -> 1 -> 3 -> 5 -> 7 -> 9'
        >>> str(SortedLinkedList(test_data_even))
        '-2 -> 0 -> 2 -> 3 -> 4 -> 6 -> 8 -> 10'
        """
        return " -> ".join([str(node) for node in self])


def merge_lists(
    sll_one: SortedLinkedList, sll_two: SortedLinkedList
) -> SortedLinkedList:
    """
    >>> odd = SortedLinkedList(test_data_odd)
    >>> even = SortedLinkedList(test_data_even)
    >>> merged = merge_lists(odd, even)
    >>> len(merged)
    16
    >>> str(merged)
    '-11 -> -2 -> -1 -> 0 -> 0 -> 1 -> 2 -> 3 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10'
    >>> list(merged) == list(sorted(test_data_odd + test_data_even))
    True
    """
    return SortedLinkedList(list(sll_one) + list(sll_two))


def main() -> None:
    sll_one = SortedLinkedList(list(test_data_odd))
    sll_two = SortedLinkedList(list(test_data_even))
    print(merge_lists(sll_one, sll_two))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
