# This program returns the minimum number of multiplications needed to multiply the chain. Matrices A, B, C, D can be multiplied in the ways such as (ABC)D, (AB)(CD), A(BC)D, etc. So, for finding the method with minimum number of multiplications, this functions proves to be useful.

T = dict()

def matrix_mult(m, i, j):
    if (i, j) not in T:
        if j == i + 1:
            T[i, j] = 0
        else:
            T[i, j] = float("inf")  # makes T[i,j] equal to infinty.
            for k in range(i + 1, j):
                T[i, j] = min(T[i, j], matrix_mult(m, i, k) + matrix_mult(m, k, j) + m[i] * m[j] * m[k])

    return T[i, j]

print(matrix_mult(m=[50, 20, 1, 10, 100], i=0, j=4))
