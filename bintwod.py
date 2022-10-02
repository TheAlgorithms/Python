def binarySearch(A, p, q, v):
    r = int((p+q)/2)
    print("p = {}, q = {}, r = {}".format(p, q, r))
    if (A[r] == v):
        print("returning {}".format(r))
        return True
    if((p == r) or (q == r)):
        return False
    if (A[r] < v):
        return binarySearch(A, r + 1, q, v)
    if (A[r] > v):
        return binarySearch(A, p, r, v)


def matBinSearch(v, A):
    i = 0
    while A[i][0] < v:
        if binarySearch(A[i], 0, len(A[i]) - 1, v):
            return True
        else : i = i+1
    return False
    
A = [[1, 4, 7, 11, 15],
[2, 5, 8, 12, 19],
[3, 6, 9, 16, 22],
[10, 13, 14, 17, 24],
[18, 21, 23, 26, 30]]

v = 11

if matBinSearch(v, A):
    print("True")