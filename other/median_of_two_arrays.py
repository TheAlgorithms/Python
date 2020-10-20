# This code finds the median of two arrays, even if they are not sorted initially
def find_median_arrays(nums1, nums2):
    all_numbers = nums1 + nums2
    all_numbers.sort()
    div, mod = divmod(len(all_numbers), 2)
    if mod == 1:
        a = int(len(all_numbers) / 2)
        return all_numbers[a]
    else:
        a = int(div)
    return (all_numbers[a] + all_numbers[a - 1]) / 2


if __name__ == "__main__":
    array_1 = [int(x) for x in input("Enter the elements of first array: ").split()]
    array_2 = [int(x) for x in input("Enter the elements of second array: ").split()]
    print(f"The median of two arrays is: {find_median_arrays(array_1, array_2)}")
