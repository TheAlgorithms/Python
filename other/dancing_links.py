"""
Dancing Links (DLX) Algorithm for Exact Cover Problem

Author: fab-c14
Reference: Donald Knuth, "Dancing Links" (Algorithm X)
Wikipedia: https://en.wikipedia.org/wiki/Dancing_Links

DLX is an efficient algorithm for solving the Exact Cover problem, such as
tiling, polyomino puzzles, or Sudoku.

This implementation demonstrates DLX for a small exact cover problem.

Usage Example:
>>> universe = [1, 2, 3, 4, 5, 6, 7]
>>> subsets = [
...     [1, 4, 7],
...     [1, 4],
...     [4, 5, 7],
...     [3, 5, 6],
...     [2, 3, 6, 7],
...     [2, 7]
... ]
>>> for solution in dlx(universe, subsets):
...     print(solution)
[0, 3, 4]
[1, 2, 5]
"""

from collections.abc import Iterator


def dlx(universe: list[int], subsets: list[list[int]]) -> Iterator[list[int]]:
    """Yields solutions to the Exact Cover problem using Algorithm X (Dancing Links)."""
    cover: dict[int, set[int]] = {u: set() for u in universe}
    for idx, subset in enumerate(subsets):
        for elem in subset:
            cover[elem].add(idx)
    partial: list[int] = []

    def search() -> Iterator[list[int]]:
        if not cover:
            yield list(partial)
            return
        # Choose column with fewest rows (heuristic)
        c = min(cover, key=lambda col: len(cover[col]))
        for r in list(cover[c]):
            partial.append(r)
            removed: dict[int, set[int]] = {}
            for j in subsets[r]:
                for i in cover[j].copy():
                    for k in subsets[i]:
                        if k == j:
                            continue
                        if k in cover:
                            cover[k].discard(i)
                removed[j] = cover.pop(j)
            yield from search()
            # Backtrack
            for j, s in removed.items():
                cover[j] = s
                for i in cover[j]:
                    for k in subsets[i]:
                        if k != j and k in cover:
                            cover[k].add(i)
            partial.pop()

    yield from search()


if __name__ == "__main__":
    # Example: Solve the cover problem from Knuth's original paper
    universe = [1, 2, 3, 4, 5, 6, 7]
    subsets = [
        [1, 4, 7],
        [1, 4],
        [4, 5, 7],
        [3, 5, 6],
        [2, 3, 6, 7],
        [2, 7],
    ]
    for solution in dlx(universe, subsets):
        print("Solution:", solution)
