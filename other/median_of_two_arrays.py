# This code finds the median of two arrays, even if they are not sorted initially
def findMedianArrays(nums1, nums2):
    list3 = nums1 + nums2
    list3 = nums1 + nums2
    list3.sort()
    if len(list3) % 2 == 1:
        a = int(len(list3) / 2)
    if len(list3) % 2 == 1:
        a = int(len(list3) / 2)
        return list3[a]
    else:
        a = int(len(list3) / 2)
        return  (list3[a] + list3[a - 1]) / 2
        a = int(len(list3) / 2)
        return (list3[a] + list3[a - 1]) / 2


def main():
    from doctest import testmod

    testmod()
    n1 = list(map(int, input('Enter elements of an array: ').split()))
    n2 = list(map(int, input('Enter elements of another array: ').split()))
    print('The median of two arrays is: ', findMedianArrays(n1, n2))
    n1 = list(map(int, input("Enter elements of an array: ").split()))
    n2 = list(map(int, input("Enter elements of another array: ").split()))
    print("The median of two arrays is: ", findMedianArrays(n1, n2))


if __name__ == "__main__":
    main()
    
