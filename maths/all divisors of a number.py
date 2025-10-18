n = int(input("Enter you number here "))
i = 1
list1 = []
while (i**2 <= n):
    if n % i == 0:
        list1.append(i)
        if i != n//i:
            list1.append(n//i)
    i += 1
list1.sort()
print(list1)
