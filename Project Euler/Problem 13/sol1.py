'''
Problem Statement:
Work out the first ten digits of the sum of the N 50-digit numbers.
'''

n = int(input().strip())

array = []
for i in range(n):
    array.append(int(input().strip()))

print(str(sum(array))[:10])

