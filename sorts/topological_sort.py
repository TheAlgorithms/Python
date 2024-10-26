edges: dict[str, list[str]] = {
    "a": ["c", "b"],
    "b": ["d", "e"],
    "c": [],
    "d": [],
    "e": [],
}
vertices: list[str] = ["a", "b", "c", "d", "e"]

def topological_sort(start: str, visited: list[str], sort: list[str]) -> list[str]:
    visited.append(start)
    current = start
    for neighbor in edges[start]:
        if neighbor not in visited:
            topological_sort(neighbor, visited, sort)
    sort.append(current)
    return sort

if __name__ == "__main__":
    sort = topological_sort("a", [], [])
    sort.reverse() #Top down approach
    print(sort)
