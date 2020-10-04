# python3

#Find the minimum number of operations  needed to get a positive integer n from 1
#using only three operations:  add 1, multiply by 2, and multiply by 3.
import math
def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    global opCount
    opCount = [0, 0] + [math.inf] * (n - 1)
    for i in range(2, n + 1):
        temp1 = opCount[i - 1] + 1
        if i % 2 == 0:
            temp2 = opCount[i // 2] + 1
        elif i % 2 != 0:
            temp2 = math.inf
        if i % 3 == 0:
            temp3 = opCount[i // 3] + 1
        elif i % 3 != 0:
            temp3 = math.inf
        temp = min(temp1, temp2, temp3)
        opCount[i] = temp

    return opCount[-1]

def path_tracer(n):
    path = [n]
    while True:
        if n == 1:
            break
        elif n % 3 == 0 and opCount[n // 3] == opCount[n] - 1:
            path.append(n // 3)
            n = n // 3
        elif n % 2 == 0 and opCount[n // 2] == opCount[n] - 1:
            path.append(n // 2)
            n = n // 2
        else:
            path.append(n - 1)
            n = n - 1

    path1 = map(str, reversed(path))
    actPath = ' '.join(path1)
    return actPath

if __name__ == '__main__':
    input_n = int(input())
    op = compute_operations(input_n)
    pth = path_tracer(input_n)
    print(op)
    print(pth)
