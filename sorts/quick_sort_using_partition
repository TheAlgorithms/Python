# Implimentation of quick sort algorithm using first element as pivot element.


def partition(array, first, last):
    pivot = array[first]
    i = first + 1
    j = last

    while True:
        while i <= j and array[j] >= pivot:
            j = j - 1

        while i <= j and array[i] <= pivot:
            i = i + 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
        else:
            break
    array[first], array[j] = array[j], array[first]
    return j

def quick_sort(array, first, last):          
    if first >= last:                         
        return

    a = partition(array, first, last)
    quick_sort(array, first, a-1)
    quick_sort(array, a+1, last)

array = []
inp=int(input('Enter the number of elements in the array : '))
for i in range(inp):
    inp1=int(input(f'Enter element {i+1}: '))
    array.append(inp1)

quick_sort(array, 0, len(array) - 1)
print(array)
