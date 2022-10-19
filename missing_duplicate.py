# Sum of missing and duplicate number in a list

list1 = [2, 3, 4, 4]
n = len(list1)

sum1 = sum(list1)
sum2 = sum(set(list1))

sum3 = n*(n+1)//2
missing = sum3-sum2
duplicate = sum1-sum2
print(missing+duplicate)
