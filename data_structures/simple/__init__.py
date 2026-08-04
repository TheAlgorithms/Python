"""Simple implementations of common data structures.

This subpackage contains small, educational implementations copied from the
`ds_extra` package so they can be accessed via `data_structures.simple`.
"""

from .linked_list import LinkedList
from .stack import ListStack, LinkedStack
from .queue import Queue
from .bst import BinarySearchTree
from .graph import Graph
from .trie import Trie
from .union_find import UnionFind
from .min_heap import MinHeap

__all__ = [
    "LinkedList",
    "ListStack",
    "LinkedStack",
    "Queue",
    "BinarySearchTree",
    "Graph",
    "Trie",
    "UnionFind",
    "MinHeap",
]
