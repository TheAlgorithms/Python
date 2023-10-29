# str = input().split()
# n, m = int(str[0]), int(str[1])
# li = [[int(j) for j in input().split()]for i in range(n)]
# print(li)
# <------------------------------------------------------------------------------>
# above code is tyo take input in 2d array
# below code is to set the given list as 2d in list
# str = input().split()
# n, m = int(str[0]), int(str[1])
# b = input().split()
# li = [[int(b[m*i+j]) for j in range(m)] for i in range(n)]
# print(li)

str = input().split()
n, m = int(str[0]), int(str[1])
b = str[2:]
# b = str[2:] is given in format to run the loop from index 2 as sometimes list is given as 3 4 1 2 3 4 5 6 7 8 9 10
# 11 12 in which 3 & 4 are the number of rows and columns
li = [[int(b[m * i + j]) for j in range(m)] for i in range(n)]
print(li)
