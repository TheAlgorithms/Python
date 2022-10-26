'''
This is a pure implementation of recursive depth first search (DFS) algorithm of a 2D matrix using python
'''

VISITED = -1
searched_item_cordinates = {'i': None, 'j': None}

def dfs(matrix: list, item: int, i: int, j: int) -> bool:
    """
    Pure Python implementation of the recursive DFS algorithm of a 2D matrix.
    Examples:
    >>> dfs([[5, 12, 9], [6, 11, 8], [7, 43, 20], [9, 0, 3]], 20, 0, 0)
    True
    >>> dfs([[1, 7, 5], [9, 11, 3], [2, 6, 0]], 7, 0, 0)
    True
    >>> dfs([[9, 4, 3], [2, 0, 10]], 8, 0, 0)
    False
    >>> dfs([[1, 7, 3, 11, 9], [15, 12, 10, 8, 6], [40, 30, 22, 31, 4]], 12, 0, 0)
    True
    """

    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[i]) or matrix[i][j] == VISITED:
        return False
    if matrix[i][j] == item:
        searched_item_cordinates['i'], searched_item_cordinates['j'] = i, j

        return True

    current = matrix[i][j]
    matrix[i][j] = VISITED

    result = dfs(matrix, item, i + 1, j) or dfs(matrix, item, i - 1, j) or dfs(matrix, item, i, j + 1) or dfs(matrix, item, i, j - 1)
    matrix[i][j] = current

    return result

if __name__ == '__main__':
    matrix = []
    num_rows = int(input("Enter number of rows of the matrix: "))
    num_cols = int(input("Enter number of columns of the matrix: "))

    for i in range(num_rows):
        matrix.append([])
        for j in range(num_cols):
            element = int(input("Enter the element of index ("+ str(i) + ', ' + str(j) + '): '))
            matrix[i].append(element)
    
    search_item = int(input("Enter the element to be searched: "))
    result = dfs(matrix, search_item, 0, 0)

    if result:  
        print("Item found in the cordinate: ", searched_item_cordinates)
    else:
        print("Item not found!")
            