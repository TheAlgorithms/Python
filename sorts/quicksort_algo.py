def quicksort(n, first, last):
    pivot = n[(first + last) // 2]
    i = first
    j = last
    while i < j:
        while n[i] <= pivot:
            i += 1
        while n[j] > pivot:
            j -= 1
        if i < j:
            (n[i], n[j]) = (n[j], n[i])
        quicksort(n, first, j - 1)
        quicksort(n, j + 1, last)


n = input("Enter the list of numbers seperated by spaces:").split()
n = [int(x) for x in n]
quicksort(n, 0, len(n) - 1)
print(n)
