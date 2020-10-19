def GE_pp(A, b):
    '''Gaussian Elimination with partial pivoting for factorizing a
    linear system A x = b into P * A = L * U and b = L^{-1}x * P * b
    Inputs: Matrix A, Vector b
    Outputs: Modified matrix A containing L and U, Modified vector b
    Note: The permutation matrix is not tracked
  
    Please checkout the following URL for more explanation
    URL : https://courses.engr.illinois.edu/cs357/su2013/lectures/lecture07.pdf
    '''
    n = A.shape[0]
    M = np.eye(n)
    for k in range(0, n - 1):    # Loop over columns
        p = k    # Initial pivot index
        for i in range(k, n):    # Search for pivot in current column
            if (abs(A[i, k]) > abs(A[p, k])):
                p = i

        if p != k:    # Interchange rows p and k in A and b
            temp = A[p, :].copy()
            A[p, :] = A[k, :].copy()
            A[k, :] = temp.copy()
            temp1 = b[p]
            b[p] = b[k]
            b[k] = temp1

        if A[k, k] == 0:    # Stop if pivot is zero
            continue

        for i in range(k + 1, n):    # Loop over rows below digonal
            M[i, k] = A[i, k] / A[k, k]    # Multipliers for current column
            A[i, k] = M[i, k]    # Store L "in place" instead of 0
            for j in range(k + 1, n):    # Loop over non-zero columns
                A[i, j] -= M[i, k] * A[k, j]
            
            b[i] -= M[i, k] * b[k]   # Modify right hand side vector
            
    return A, b
