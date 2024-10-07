class Solution:
    def __init__(self):
        # Initialize a string direction which represents all the directions.
        self.direction = "DLRU"
        # Arrays to represent changes in rows and columns
        self.dr = [1, 0, 0, -1]
        self.dc = [0, -1, 1, 0]

    # Function to check if cell (r, c) is inside the maze and unblocked
    def is_valid(self, r, c, n, maze):
        return 0 <= r < n and 0 <= c < n and maze[r] == 1

    # Function to get all valid paths
    def solve(self, r, c, maze, n, ans, current_path):
        # If we reach the bottom right cell of the matrix, add the current path to ans and return
        if r == n - 1 and c == n - 1:
            ans.append(current_path)
            return

        # Mark the current cell as blocked
        maze[r] = 0

        for i in range(4):
            # Find the next row based on the current row (r) and the dr[] array
            nextr = r + self.dr[i]
            # Find the next column based on the current column (c) and the dc[] array
            nextc = c + self.dc[i]

            # Check if the next cell is valid or not
            if self.is_valid(nextr, nextc, n, maze):
                current_path += self.direction[i]
                # Recursively call the solve function for the next cell
                self.solve(nextr, nextc, maze, n, ans, current_path)
                current_path = current_path[:-1]

        # Mark the current cell as unblocked
        maze[r] = 1

    def find_path(self, maze, n):
        # List to store all the valid paths
        ans = []

        # Check if the top left cell is unblocked
        if maze[0][0] == 1:
            current_path = ""
            self.solve(0, 0, maze, n, ans, current_path)
        return ans


# Main function


def main():
    n = 4

    m = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]

    obj = Solution()
    result = obj.find_path(m, n)

    if not result:
        print(-1)
    else:
        for path in result:
            print(path, end=" ")
        print()


if __name__ == "__main__":
    main()
