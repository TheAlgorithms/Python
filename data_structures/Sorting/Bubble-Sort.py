a = [10,7,100,60,3,89]
def bSort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                # Swaping elements
                a[j], a[j+1] = a[j+1], a[j]
              
bSort(a)
print("Sorted array is:")
print(a)
