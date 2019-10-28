def bubbleSort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1] :
                a[j], a[j+1] = a[j+1], a[j]
l= [64, 34, 25, 12, 22, 11, 90]
bubbleSort(l)
print ("Sorted array is:")
for i in range(len(l)):
    print ("%d" %l[i])
