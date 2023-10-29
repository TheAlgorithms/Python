li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(li[0])
# [1, 2, 3] is the value we get
print(type(li[0]))
li[0][1] = 4
print(li)
print(id(li))
print(id(li[0]))
print(id(li[1]))
li[1] = "GARVIT"
print(li)
li[1] = [1, 2, 3, 44, 5]
print(li)
print(li[0][5])
# gives error for out of range
