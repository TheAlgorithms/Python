import heapq


def swim_in_rising_water(grid: list[list[int]]) -> int:
    """
    Return the minimum time to reach the bottom right square of the grid
    from the top left, where time t allows swimming to cells with
    elevation <= t.

    This is a variant of Dijkstra's shortest path algorithm using a
    priority queue (min-heap) to find the minimum elevation (time) path
    in a grid graph.

    Reference: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

    :param grid: n x n integer matrix where grid[i][j] is the elevation
                 at (i, j)
    :return: Minimum time to reach (n-1, n-1) from (0, 0)

    Examples:
    >>> swim_in_rising_water([[0, 2], [1, 3]])
    3
    >>> grid = [
    ...     [0, 1, 2, 3, 4],
    ...     [24, 23, 22, 21, 5],
    ...     [12, 13, 14, 15, 16],
    ...     [11, 17, 18, 19, 20],
    ...     [10, 9, 8, 7, 6]
    ... ]
    >>> swim_in_rising_water(grid)
    16
    >>> swim_in_rising_water([[0]])  # n=1 edge case
    0
    >>> swim_in_rising_water([[5, 3], [4, 2]])  # Another small grid
    5
    """
    if not grid or not grid[0]:
        raise ValueError("Grid must be a non-empty n x n matrix")

    n = len(grid)
    if n != len(grid[0]):
        raise ValueError("Grid must be square (n x n)")

    # Directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Min-heap: (max_elevation_so_far, row, col)
    min_heap: list[tuple[int, int, int]] = [(grid[0][0], 0, 0)]
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True

    while min_heap:
        max_elev, r, c = heapq.heappop(min_heap)

        # Reached bottom-right
        if r == n - 1 and c == n - 1:
            return max_elev

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                # The time is the max elevation encountered on this path
                new_elev = max(max_elev, grid[nr][nc])
                heapq.heappush(min_heap, (new_elev, nr, nc))

    # Should always reach if grid is valid, but for completeness
    raise ValueError("No path found to bottom-right (grid constraints violated)")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
