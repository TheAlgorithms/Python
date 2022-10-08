# Find second largest element in the array
# Time Complexity: O(n)

number = [1,2,3,2,5,7,3,9,7,6,9]
num=list(set(number))
if num[0]>num[1]:
    m, m2 = num[0], num[1]
else:
    m, m2 = num[1], num[0]

for x in num[2:]:
    if x>m2:
        if x>m:
            m2, m = m, x
        else:
            m2 = x
print(m2)

#Output: 7
