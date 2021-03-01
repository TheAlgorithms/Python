
"""
    To find determinant of NxN Matrix i have used Row Reduction method
    
    you can see wikipedia of this Method
    https://en.wikipedia.org/wiki/Row_echelon_form
    
    Enter the size of the matrix in first line, 
    then Enter columns of Matrix till next 'N' line 
    and each line contains 'N' space separated Numbers
    3
    1 2 3
    4 5 6
    7 8 4
    determinat:  15.0

    4
    1 2 3 7
    4 5 6 6
    7 8 1 5
    1 2 3 4
    determinat:  -72.0

    5
    1 2 3 7 13
    4 5 6 6 90
    7 8 1 5 76
    1 2 3 4 12
    9 6 3 7 4
    determinat:  19848.0

    6
    1 2  3 7  13 23
    4 44 6 6  90 12
    7 8  1 5  6  98
    1 2  3 4  12 4
    9 6  3 7  4  9
    2 47 8 91 36 9
    determinat:  -20981553.999999993
    
"""

from copy import deepcopy
print('''Enter the size of the matrix in first line, 
then Enter columns of Matrix till next 'N' line 
and each line contains 'N' space separated Numbers : ''')
N = int(input())
a = []
for i in range(R):
    t = list(map(int, input().split())) 
    a.append(t)

b = deepcopy(a) 

n = 0 
m = 1 
c1 = 1
c2 = 0
for k in range(1, (2*(N-1)) + 1):
    for i in range(c1, N):
        for j in range(0, N):
            if (a[c1 - 1][c2]) != 0:
                b[i][j] = (a[i][j] - ((a[m][n]) * ((a[c2][j]) / (a[c1 - 1][c2]))))
        m = m + 1

    a = deepcopy(b)
    n = n + 1
    m = n + 1
    c1 = c1 + 1
    c2 = c2 + 1

d = float(1)
for i in range(0, N):
        for j in range(0, N):
            if i==j:
                d=d*a[i][j]

print("determinat: ", d)
