"""Python implementation of interpolation search algorithm."""


# Return string describing whether target is found in arr or not.
def interpolation_search(arr, target):
    """Perform interpolation search for target in arr."""
    lo = 0
    mid = -1
    hi = len(arr)-1
    found = False
    # Keep looping until either match found, or search has been exhausted.
    while found is False:
        # mid formula
        mid = int(lo + ((hi - lo)/(arr[hi]-arr[lo])) * (target-arr[lo]))

        # Search Exhausted
        if (lo == hi) or (arr[lo] == arr[hi]) or mid > len(arr)-1:
            return str(target) + ' not found.'
        # Match Found
        if arr[mid] == target:
            found = True
            return str(arr[mid]) + ' found.'
        # Revise Lo, Hi, Mid
        else:
            if arr[mid] < target:
                hi = mid-1
            elif arr[mid] > target:
                lo = mid+1


# Example with basic data.
# arr must be sorted when using an interpolation search algorithm.
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 2

retstr = interpolation_search(arr=sorted(arr), target=target)
print(retstr)
