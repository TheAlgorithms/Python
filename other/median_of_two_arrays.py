# This code finds the median of two arrays, even if they are not sorted initially
def find_median_arrays(nums1, nums2):
    list3 = nums1 + nums2
    list3 = nums1 + nums2
    list3.sort()
    if divmod(len(list3), 2).[1] == 1:
        a = int(len(list3) / 2)
        return list3[a]
    else:
        a = int(len(list3) / 2)
    return  (list3[a] + list3[a - 1]) / 2
  

if __name__ == "__main__":
    n1 = [int(x) for x in input("Enter the elements of first array: ").split()]
    n2 = [int(x) for x in input("Enter the elements of second array: ").split()]
    m = find_median_arrays(n1, n2)
    print(f'The median of two arrays is: {m}')    
