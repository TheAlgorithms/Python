from __future__ import annotations

def saddle_points(M: list[list]) -> str:
    """
    >>> M = [[1,2,3],[4,5,6],[7,8,9]]
    >>> saddle_points(M)
    ('Saddle point(s) is/are: ', {(2, 0)}, 'Value(s) is/are: ', [7])
    >>> M = [[4,4,2],[3,3,7],[8,8,8]]
    >>> saddle_points(M)
    ('Saddle point(s) is/are: ', {(2, 0), (2, 1), (2, 2)}, 'Value(s) is/are: ', [8, 8, 8])
    >>> M = [[6,4,8],[7,3,2],[2,1,2]]
    >>> saddle_points(M)
    ('Saddle point(s) is/are: ', {(0, 1)}, 'Value(s) is/are: ', [4])
    """
    """
    A function to list the saddle point(s) of a given matrix.
    Wikipedia definition: A saddle point of a matrix is an element which is both the largest element in its column and the smallest element in its row.
    Link: https://en.wikipedia.org/wiki/Saddle_point
    """
    

    SP = []
    N = list(zip(*M))
    points = set()
    for i, row in enumerate(M):
        for j, x in enumerate(row):
            if (x == min(row) and x == max(N[j])): 
                    points.add((i, j))
    L = list(points)
    for i in range(len(L)):
        SP.append(M[(L[i])[0]][(L[i])[1]])
    return "Saddle point(s) is/are: ", points, "Value(s) is/are: ", SP

if __name__ == "__main__":
    #print(saddle_points([[4,2,3],[8,5,6],[7,8,9]]))
    import doctest
    doctest.testmod()
