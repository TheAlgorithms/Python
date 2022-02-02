from doctest import testmod

def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    """
    >>> print(uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
    2
    >>> print(uniquePathsWithObstacles([[0,1],[0,0]]))
    1
    """
    if obstacleGrid[0][0] == 1:
        return 0
        
    rows = len(obstacleGrid)
    cols = len(obstacleGrid[0])
        
    table = [[0 for i in range(cols)]for j in range(rows)]
        
    table[0][0] = 1
        
    for i in range(1,cols):
        if obstacleGrid[0][i] == 1:
            table[0][i] = 0
        else:
            table[0][i] = table[0][i-1]
                
    for i in range(1,rows):
        if obstacleGrid[i][0] == 1:
            table[i][0] = 0
        else:
            table[i][0] = table[i-1][0]
                
    for i in range(1,rows):
        for j in range(1,cols):
            if obstacleGrid[i][j] == 1:
                table[i][j] = 0
            else:
                table[i][j] = table[i-1][j] + table[i][j-1]
        
    return table[-1][-1]


if __name__ == "__main__":
    
    testmod(name ='uniquePathsWithObstacles', verbose = True)
