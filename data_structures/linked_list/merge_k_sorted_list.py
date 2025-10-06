""" This algorithm merges k sorted linked lists into a single sorted linked list.

Each input linked list is assumed to be sorted in non-decreasing order. The algorithm uses a min-heap (priority queue) to efficiently determine the next smallest node among all the heads of the lists.

At every step:

The smallest element among the current nodes of all lists is extracted from the heap.

That node is appended to the result list.

The next node from the same list (if any) is then pushed into the heap.

This process repeats until all nodes from all lists have been processed.
The final result is a single sorted linked list containing all elements from the input lists.

Solve on:
https://leetcode.com/problems/merge-k-sorted-lists/
"""
from __future__ import annotations
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
import heapq


test_data_odd = (3, 9, -11, 0, 7, 5, 1, -1)
test_data_even = (4, 6, 2, 0, 8, 10, 3, -2)
test_data_mixed = (1, 4, 7), (2, 5, 8), (3, 6, 9)


@dataclass
class Node:
    data: int
    next_node: Node | None


class SortedLinkedList:
    def __init__(self, ints: Iterable[int]) -> None:
        self.head: Node | None = None
        for i in sorted(ints, reverse=True):
            self.head = Node(i, self.head)

    def __iter__(self) -> Iterator[int]:
        node = self.head
        while node:
            yield node.data
            node = node.next_node

    def __len__(self) -> int:
        return sum(1 for _ in self)

    def __str__(self) -> str:
        return " -> ".join([str(node) for node in self])


def merge_two_lists(
    sll_one: SortedLinkedList, sll_two: SortedLinkedList
) -> SortedLinkedList:
    """Merge two sorted linked lists."""
    return SortedLinkedList(list(sll_one) + list(sll_two))


def merge_k_sorted_lists(lists: list[SortedLinkedList]) -> SortedLinkedList:
    """
    Merge k sorted linked lists into one sorted linked list.
    
    >>> SSL = SortedLinkedList
    >>> lists = [SSL([1, 4, 7]), SSL([2, 5, 8]), SSL([3, 6, 9])]
    >>> merged = merge_k_sorted_lists(lists)
    >>> str(merged)
    '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9'
    >>> len(merged)
    9
    """
    # Create a min-heap (stores tuples of value, index, node)
    heap: list[tuple[int, int, Node]] = []
    for i, sll in enumerate(lists):
        if sll.head:
            heapq.heappush(heap, (sll.head.data, i, sll.head))

    dummy = Node(0, None)
    current = dummy

    while heap:
        value, idx, node = heapq.heappop(heap)
        current.next_node = Node(value, None)
        current = current.next_node

        if node.next_node:
            heapq.heappush(heap, (node.next_node.data, idx, node.next_node))

    # Convert to SortedLinkedList for consistency
    result = SortedLinkedList([])
    result.head = dummy.next_node
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    SSL = SortedLinkedList

    # Example usage
    list1 = SSL(test_data_odd)
    list2 = SSL(test_data_even)
    list3 = SSL([-15, -10, -5, 0, 5])
    merged_k = merge_k_sorted_lists([list1, list2, list3])

    print("Merged K Sorted Lists:")
    print(merged_k)

'''
'''