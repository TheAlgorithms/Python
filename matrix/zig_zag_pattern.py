'''
This programs prints an input 2D matrix
in zig-zag fashion.
'''

from __future__ import annotations

def get_zig_zag_pattern(matrix):
    
    """
    >>> get_zig_zag_pattern([[12,22],[31,42]])
    [[12], [22, 31], [42]]
    >>> get_zig_zag_pattern([[1]])
    [[1]]
    >>> get_zig_zag_pattern([0])
    Traceback (most recent call last):
        ...
    TypeError: object of type 'int' has no len()
    
    """
    #Storing dimensions of the input matrix
    rows=len(matrix)
    cols=len(matrix[0])
    result=[[] for i in range(rows+cols-1)]
 
    for i in range(rows):
        for j in range(cols):
            ind=i+j
            if(ind%2 ==0):
 
                #adding at beginning
                result[ind].insert(0,matrix[i][j])
            else:
 
                #adding at end
                result[ind].append(matrix[i][j])
                
    #returns resultant matrix(in zig-zag fashion)
    return result
            
if __name__ == "__main__":
    
    import doctest
    doctest.testmod()
    
    result=get_zig_zag_pattern([
            [ 1, 2, 3,],
            [ 4, 5, 6 ],
            [ 7, 8, 9 ],
        ])
    for i in result:
        for j in i:
            print(j,end=" ")
    
    
