from typing import List
import numpy as np


def StrassenR(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

    C: List[List[int]] = None

    if len(A[0]) != len(B):
        print("Las matrices no se pueden multiplicar")
        return

    a = max(len(A), len(A[0]), len(B), len(B[0]))
    A_ = None
    B_ = None

    if(a & (a-1) == 0):
        A_ = np.pad(A, [(0, a - len(A)), (0, a - len(A[0]))], mode='constant')
        B_ = np.pad(B, [(0, a - len(B)), (0, a - len(B[0]))], mode='constant')

    else:
        A_ = np.pad(A, [(0, 2**(int(np.log2(a)) + 1) - len(A)),
                        (0, 2**(int(np.log2(a)) + 1) - len(A[0]))], mode='constant')
        B_ = np.pad(B, [(0, 2**(int(np.log2(a)) + 1) - len(B)),
                        (0, 2**(int(np.log2(a)) + 1) - len(B[0]))], mode='constant')

    C = StrassenRnp(A_, B_)[0:len(A), 0:len(B[0])].tolist()

    return C


def StrassenRnp(A, B):
    if len(A) == 2:
        m1 = (A[0, 0] + A[1, 1])*(B[0, 0] + B[1, 1])
        m2 = (A[1, 0] + A[1, 1])*B[0, 0]
        m3 = A[0, 0]*(B[0, 1] - B[1, 1])
        m4 = A[1, 1]*(B[1, 0] - B[0, 0])
        m5 = (A[0, 0] + A[0, 1])*B[1, 1]
        m6 = (A[1, 0] - A[0, 0])*(B[0, 0] + B[0, 1])
        m7 = (A[0, 1] - A[1, 1])*(B[1, 0] + B[1, 1])

        C = np.zeros((2, 2))

        C[0, 0] = m1 + m4 - m5 + m7
        C[0, 1] = m3 + m5
        C[1, 0] = m2 + m4
        C[1, 1] = m1 - m2 + m3 + m6

        return C

    n = int(len(A)/2)
    m1 = StrassenRnp((A[0:n, 0:n] + A[n:n*2, n:n*2]),
                     (B[0:n, 0:n] + B[n:n*2, n:n*2]))
    m2 = StrassenRnp((A[n:n*2, 0:n] + A[n:n*2, n:n*2]), B[0:n, 0:n])
    m3 = StrassenRnp(A[0:n, 0:n], (B[0:n, n:n*2] - B[n:n*2, n:n*2]))
    m4 = StrassenRnp(A[n:n*2, n:n*2], (B[n:n*2, 0:n] - B[0:n, 0:n]))
    m5 = StrassenRnp((A[0:n, 0:n] + A[0:n, n:n*2]), B[n:n*2, n:n*2])
    m6 = StrassenRnp((A[n:n*2, 0:n] - A[0:n, 0:n]),
                     (B[0:n, 0:n] + B[0:n, n:n*2]))
    m7 = StrassenRnp((A[0:n, n:n*2] - A[n:n*2, n:n*2]),
                     (B[n:n*2, 0:n] + B[n:n*2, n:n*2]))

    C = np.zeros((n*2, n*2))
    c1 = np.pad(m1 + m4 - m5 + m7, [(0, n), (0, n)], mode='constant')
    c2 = np.pad(m3 + m5, [(0, n), (n, 0)], mode='constant')
    c3 = np.pad(m2 + m4, [(n, 0), (0, n)], mode='constant')
    c4 = np.pad(m1 - m2 + m3 + m6, [(n, 0), (n, 0)], mode='constant')

    C = c1 + c2 + c3 + c4

    return C
