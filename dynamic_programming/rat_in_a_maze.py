def is_safe(maze, x, y, n):
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 1

def solve_maze_util(maze, x, y, n, solution):
    if x == n - 1 and y == n - 1:
        solution[x][y] = 1
        return True
    if is_safe(maze, x, y, n):
        solution[x][y] = 1
        if solve_maze_util(maze, x + 1, y, n, solution):
            return True
        if solve_maze_util(maze, x, y + 1, n, solution):
            return True
        solution[x][y] = 0
        return False
    return False

def solve_maze(maze, n):
    solution = [[0] * n for _ in range(n)]
    if not solve_maze_util(maze, 0, 0, n, solution):
        print("No solution exists")
        return
    for row in solution:
        print(*row)

if __name__ == "__main__":
    n = int(input())
    maze = [list(map(int, input().split())) for _ in range(n)]
    solve_maze(maze, n)
