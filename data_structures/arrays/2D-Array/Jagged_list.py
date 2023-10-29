# list/arr with no fixed number rows nd columns
# str = input().split()
n = int(input())
li = [[int(j) for j in input().split()] for i in range(n)]
print(li)
