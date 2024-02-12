"""Topological Sort."""

testCases = [
    {
        #     a
        #    / \
        #   b  c
        #  / \
        # d  e
        "edges": {
            "a": ["c", "b"],
            "b": ["d", "e"],
            "c": [],
            "d": [],
            "e": [],
        },
        "vertices": ["a", "b", "c", "d", "e"],
    },
    {
        #            a
        #          / | \
        #         b  c  f
        #        / \   / \
        #       d   e g   h
        #            /
        #           i
        "edges": {
            "a": ["b", "c", "f"],
            "b": ["d", "e"],
            "c": [],
            "d": [],
            "e": [],
            "f": ["g", "h"],
            "g": ["i"],
            "h": [],
            "i": [],
        },
        "vertices": ["a", "b", "c", "d", "e", "f", "g", "h", "i"],
    },
    {
        #                        a
        #                      /   \
        #                     b     c
        #                    /     / \
        #                   d     e   f
        #                  /
        #                 g
        #                /
        #               h
        #              /
        #             i
        #            /
        #           j
        #          /
        #         k
        "edges": {
            "a": ["b", "c"],
            "b": ["d"],
            "c": ["e", "f"],
            "d": ["g"],
            "e": [],
            "f": [],
            "g": ["h"],
            "h": ["i"],
            "i": ["j"],
            "j": ["k"],
            "k": [],
        },
        "vertices": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"],
    },
    {
        #
        #                  a
        #                /   \
        #              b      c
        #             / \    / \
        #            d   e  f   g
        "edges": {
            "a": ["b", "c"],
            "b": ["d", "e"],
            "c": ["f", "g"],
            "d": [],
            "e": [],
            "f": [],
            "g": [],
        },
        "vertices": ["a", "b", "c", "d", "e", "f", "g"],
    },
    {
        #
        #                  a
        #                /   \
        #              b      c
        #             / \    / \
        #            d   e  f   g
        #           / \   \      \
        #          h   i   j      k
        #         /     \
        #        l       m
        #       /
        #      n
        #
        #
        "edges": {
            "a": ["b", "c"],
            "b": ["d", "e"],
            "c": ["f", "g"],
            "d": ["h", "i"],
            "e": ["j"],
            "f": [],
            "g": ["k"],
            "h": ["l"],
            "i": ["m"],
            "j": [],
            "k": [],
            "l": ["n"],
            "m": [],
            "n": [],
        },
        "vertices": ["a", "b", "c", "d", "e", "f", "g"],
    },
    {
        #                        a
        #                      /
        #                     b
        #                    /
        #                   c
        #                  /
        #                 d
        #                /
        #               e
        #              /
        #             f
        #            /
        #           g
        #          /
        #         h
        "edges": {
            "a": ["b"],
            "b": ["c"],
            "c": ["d"],
            "d": ["e"],
            "e": ["f"],
            "f": ["g"],
            "g": ["h"],
            "h": [],
        },
        "vertices": ["a", "b", "c", "d", "e", "f", "g", "h"],
    },
    {
        #            a
        #          / | \
        #         b  c  d
        #        /       \
        #       e         f
        #      /           \
        #     g             h
        #    /               \
        #   i                 j
        #  /                   \
        # k                     l
        "edges": {
            "a": ["b", "c", "d"],
            "b": ["e"],
            "c": [],
            "d": ["f"],
            "e": ["g"],
            "f": ["h"],
            "g": ["i"],
            "h": ["j"],
            "i": ["k"],
            "j": ["l"],
            "k": [],
            "l": [],
        },
        "vertices": ["a", "b", "c", "d", "e", "f", "g", "h", "i"],
    },
    {
        #     a
        #    / \
        #   b   c
        #  /     \
        # d       e
        "edges": {
            "a": ["b", "c"],
            "b": ["d"],
            "c": ["e"],
            "d": [],
            "e": [],
        },
        "vertices": ["a", "b", "c", "d", "e"],
    },
    {
        #   a     h
        #  / \     \
        # b   c     i
        # |   |     |
        # d   e     j
        # |   |
        # g   f
        "edges": {
            "a": ["b", "c"],
            "b": ["d"],
            "c": ["e", "f"],
            "d": ["g"],
            "e": [],
            "f": [],
            "g": [],
            "h": ["i"],
            "i": ["j"],
            "j": [],
        },
        "vertices": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    },
    {
        #   a     h     k
        #  / \     \     \
        # b   c     i     l
        # |   |     |     |
        # d   e     j     m
        # |   |
        # g   f
        "edges": {
            "a": ["b", "c"],
            "b": ["d"],
            "c": ["e"],
            "d": ["g"],
            "e": ["f"],
            "f": [],
            "g": [],
            "h": ["i"],
            "i": ["j"],
            "j": [],
            "k": ["l"],
            "l": ["m"],
            "m": [],
        },
        "vertices": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"],
    },
]


def topological_sort(start: str, visited: list[str], sort: list[str]) -> list[str]:
    """Perform topological sort on a directed acyclic graph."""
    current = start
    # add current to visited
    visited.append(current)
    neighbors = edges[current]
    for neighbor in neighbors:
        # if neighbor not in visited, visit
        if neighbor not in visited:
            sort = topological_sort(neighbor, visited, sort)
    # if all neighbors visited add current to sort
    sort.append(current)
    # if all vertices haven't been visited select a new one to visit
    if len(visited) != len(vertices):
        for vertice in vertices:
            if vertice not in visited:
                sort = topological_sort(vertice, visited, sort)
    # return sort
    return sort


if __name__ == "__main__":
    for idx, testCase in enumerate(testCases, start=1):
        print(f"Test Case {idx}:")
        edges = testCase["edges"]
        vertices = testCase["vertices"]
        sort = topological_sort("a", [], [])
        print(sort)
