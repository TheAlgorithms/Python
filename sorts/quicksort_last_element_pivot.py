# Shree Ganeshaya Namah:
# Shambhu

#Auther: Pradhuman Goswami

# Checkout the wiki page for this algorithm here https://en.wikipedia.org/wiki/Quicksort

# Description

# Quick sort is a sorting algorithm that makes use of the divide and conquer technique.
# In this, we take any element such as the first, middle or preferably last element as a pivot
# Then we divide the the array into two separate arrays; the lesser and the greater elements essentially
# Then by using recursion we sort it and return the array.
# So, what are we waiting for? Let's do it without further ado.


def quick(arr: list)-> list:
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    l = []
    g = []
    for i in arr[:-1]:
        if i <= pivot:
            l.append(i)
        else:
            g.append(i)
    return quick(l) + [pivot] + quick(g)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    assert quick([4, 5, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert quick([0, 1, -10, 15, 2, -2]) == [-10, -2, 0, 1, 2, 15]
