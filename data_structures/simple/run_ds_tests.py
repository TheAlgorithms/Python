"""Smoke test runner for the `data_structures.simple` package."""

import sys

from data_structures.simple.linked_list import LinkedList
from data_structures.simple.stack import ListStack, LinkedStack
from data_structures.simple.queue import Queue
from data_structures.simple.bst import BinarySearchTree
from data_structures.simple.graph import Graph
from data_structures.simple.trie import Trie
from data_structures.simple.union_find import UnionFind
from data_structures.simple.min_heap import MinHeap


def run() -> None:
    failures = []

    try:
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.prepend(0)
        assert ll.to_list() == [0, 1, 2]
        assert ll.find(1) is not None
        assert ll.delete(1) is True
        assert ll.to_list() == [0, 2]
        print("LinkedList: OK")
    except Exception as e:
        failures.append(("LinkedList", e))

    try:
        s = ListStack()
        s.push(1)
        s.push(2)
        assert s.peek() == 2
        assert s.pop() == 2

        ls = LinkedStack()
        ls.push("a")
        ls.push("b")
        assert ls.peek() == "b"
        assert ls.pop() == "b"
        print("Stacks: OK")
    except Exception as e:
        failures.append(("Stacks", e))

    try:
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        assert q.peek() == 1
        assert q.dequeue() == 1
        print("Queue: OK")
    except Exception as e:
        failures.append(("Queue", e))

    try:
        bst = BinarySearchTree()
        for v in [3, 1, 4, 2]:
            bst.insert(v)
        assert bst.search(2)
        assert bst.inorder() == [1, 2, 3, 4]
        print("BST: OK")
    except Exception as e:
        failures.append(("BST", e))

    try:
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        order_bfs = g.bfs(1)
        assert 1 in order_bfs
        order_dfs = g.dfs(1)
        assert 1 in order_dfs
        print("Graph: OK")
    except Exception as e:
        failures.append(("Graph", e))

    try:
        t = Trie()
        t.insert("hello")
        assert t.search("hello")
        assert t.starts_with("hel")
        print("Trie: OK")
    except Exception as e:
        failures.append(("Trie", e))

    try:
        uf = UnionFind()
        for x in [1, 2, 3]:
            uf.make_set(x)
        uf.union(1, 2)
        assert uf.find(1) == uf.find(2)
        print("UnionFind: OK")
    except Exception as e:
        failures.append(("UnionFind", e))

    try:
        h = MinHeap()
        h.push(5)
        h.push(1)
        h.push(3)
        assert h.peek() == 1
        assert h.pop() == 1
        print("MinHeap: OK")
    except Exception as e:
        failures.append(("MinHeap", e))

    if failures:
        print("\nFAILURES:")
        for name, exc in failures:
            print(f"- {name}: {exc}")
        sys.exit(2)
    else:
        print("\nAll data_structures.simple smoke tests passed.")


if __name__ == "__main__":
    run()
