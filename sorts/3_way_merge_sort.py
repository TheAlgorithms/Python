def merge(garray, low, mid1, mid2, high, destarray):
    i = low
    j = mid1
    k = mid2
    l = low
    while ((i < mid1) and (j < mid2) and (k < high)):
        if(garray[i] < garray[j]):
            if(garray[i] < garray[k]):
                destarray[l] = garray[i]
                l += 1
                i += 1
            else:
                destarray[l] = garray[k]
                l += 1
                k += 1
        else:
            if(garray[j] < garray[k]):
                destarray[l] = garray[j]
                l += 1
                j += 1
            else:
                destarray[l] = garray[k]
                l += 1
                k += 1
    while ((i < mid1) and (j < mid2)):
        if(garray[i] < garray[j]):
            destarray[l] = garray[i]
            l += 1
            i += 1
        else:
            destarray[l] = garray[j]
            l += 1
            j += 1
    while ((j < mid2) and (k < high)):
        if(garray[j] < garray[k]):
            destarray[l] = garray[j]
            l += 1
            j += 1
        else:
            destarray[l] = garray[k]
            l += 1
            k += 1
    while ((i < mid1) and (k < high)):
        if(garray[i] < garray[k]):
            destarray[l] = garray[i]
            l += 1
            i += 1
        else:
            destarray[l] = garray[k]
            l += 1
            k += 1 
    while (i < mid1):
        destarray[l] = garray[i]
        l += 1
        i += 1
    while (j < mid2):
        destarray[l] = garray[j]
        l += 1
        j += 1
    while (k < high):
        destarray[l] = garray[k]
        l += 1
        k += 1
""" Performin the merge sort algorithm on the 
given array of values in the rangeof indices 
[low, high). low is minimum index, high is 
maximum index (exclusive) """
def mergeSort3WayRec(gArray, low, high, destArray):
    if (high - low < 2):
        return
    mid1 = low + ((high - low) // 3)
    mid2 = low + 2 * ((high - low) // 3) + 1
    mergeSort3WayRec(destArray, low, mid1, gArray)
    mergeSort3WayRec(destArray, mid1, mid2, gArray)
    mergeSort3WayRec(destArray, mid2, high, gArray)
    merge(destArray, low, mid1, mid2, high, gArray)
def mergeSort3Way(gArray, n):
    if (n == 0):
        return 
    fArray = []
    fArray = gArray.copy()
    mergeSort3WayRec(fArray, 0, n, gArray)
    gArray = fArray.copy()
    return gArray
data =[]
for i in range(10):
    data.append(int(input()))
data = mergeSort3Way(data, 10)
print("After 3 way merge sort: ", end="")
for i in range(10):
    print(f"{data[i]} ", end="")