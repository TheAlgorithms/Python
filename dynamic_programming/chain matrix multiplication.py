from doctest import testmod

T = dict()

def matrix_mult(m, i, j):
    ''' 
    This program returns the minimum number of multiplications
    needed to multiply the chain. Matrices A, B, C, D can be
    multiplied in the ways such as (ABC)D, (AB)(CD), A(BC)D, etc.
    So, for finding the method with minimum number of
    multiplications, this functions proves to be useful. 
    Define input and expected output: 
    >>> matrix_mult([50, 20, 1, 10, 100], 0, 4)
    7000
    >>> matrix_mult([50, 20, 1, 10, 100, 20], 0, 5)
    5000
    '''
    if (i, j) not in T:
        if j == i + 1:
            T[i, j] = 0
        else:
            T[i, j] = float("inf")  # makes T[i,j] equal to infinty.
            for k in range(i + 1, j):
                T[i, j] = min(T[i, j], matrix_mult(m, i, k) + matrix_mult(m, k, j) + m[i] * m[j] * m[k])

    return T[i, j]

# call the testmod function 
if __name__ == '__main__': 
    testmod(name ='matrix_mult', verbose = True)
