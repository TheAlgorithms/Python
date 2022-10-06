#Shree Ganeshaya Namah:
#Shambhu


#Quick sort is a sorting algorithm that makes use of the divide and conquer technique.
#In this, we take any element such as the first, middle or preferably last element as a pivot
#Then we divide the the array into two separate arrays; the lesser and the greater elements essentially
#Then by using recursion we sort it and return the array.
#So, what are we waiting for? Let's do it without further ado.

def quick(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[-1]
    l = []
    g = []
    for i in arr[:-1]:
        if i<=pivot:
            l.append(i)
        else:
            g.append(i)
    #time for recursion
    return quick(l)+[pivot]+quick(g)

arr = [10,20,13,11,9,4,2,1,3,5,19,22,21,18]
print(quick(arr))
