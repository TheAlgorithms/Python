"""Topological Sort."""

#     a
#    / \
#   b  c
#  / \
# d  e
edges: dict[str, list[str]] = {
    "a": ["c", "b"],
    "b": ["d", "e"],
    "c": [],
    "d": [],
    "e": [],
}
vertices: list[str] = ["a", "b", "c", "d", "e"]


class Topo:
    def topo_sort(self):
        visited = set()
        stack = []

        def dfs(node):
            visited.add(node)

            for neighbor in edges[node]:
                if neighbor not in visited:
                    dfs(neighbor)

            stack.append(node)

            return stack

        result = dfs("a")
        return result[::-1]


if __name__ == "__main__":
    topo = Topo()
    sort = topo.topo_sort()
    print(sort)
