li = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
n = 3
m = 4
for i in range(n):
    for j in range(m):
        print(li[i][j], end=" ")
    print()
# <=============================================================>
# for jagged list
li = [[1, 2, 3], [4, 5], [6, 7, 8, 9, 10]]
n = 3
for i in li:
    for ele in i:
        print(ele, end=" ")
    print()

li = [[1, 2, 3], [4, 5], [6, 7, 8, 9, 10]]
n = 3
for i in li:
    output = " ".join([str(ele) for ele in i])
    print(output)

# used to join something to a string values
# a = 'ab'.join(['1', '2', '3'])
# print(a)
