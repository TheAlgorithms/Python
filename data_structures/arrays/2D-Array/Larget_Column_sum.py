# number of row and column are same here always
def lar_col_Sum(li):
    n = len(li)
    m = len(li[0])
    # m = len(li[0]) means len of first column because all list have same num of elements
    max_sum = -1
    max_col_index = -1
    for j in range(m):
        sum = 0
        for i in range(n):
            sum += li[i][j]
        if sum > max_sum:
            max_col_index = j
            max_sum = sum
    return max_sum, max_col_index


li = [[1, 2, 3, 4], [8, 7, 6, 5], [9, 10, 11, 12]]
lar_sum, lar_col_index = lar_col_Sum(li)
print(lar_sum, lar_col_index)
