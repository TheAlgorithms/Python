#Here are the two approaches to solve/sort any array of integers in range [0,2] (inclusive)

#Implementation using counting sort:
def dutch_national_flag(arr):
    counts = [0, 0, 0]

    for num in arr:
        counts[num] += 1
    
    i = 0
    for j in range(3):
        for _ in range(counts[j]):
            arr[i] = j
            i += 1
    
    return arr
#we use a counting sort algorithm to sort the array.first create a counts array of size 3, initialize all elements to 0, and loop through the input array arr, incrementing the count of each element in counts.

# We then loop through the counts array and overwrite the values in arr with the correct number of occurrences of each element. We use an index variable i to keep track of where we are in arr, and loop through the counts array, using another loop to repeat the process for each occurrence of each element. We overwrite the value at index i in arr with the current value of j (which represents the current element being processed), increment i, and repeat until all occurrences of all elements have been processed.

#Implementation using two pointers:
def dutch_national_flag(arr):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    return arr

# In this implementation, we use three pointers: low, mid, and high. The low pointer represents the index of the first element in the array that is greater than 0, mid represents the index of the first unprocessed element, and high represents the index of the last element in the array that is less than 2.

# We initialize low and mid to 0 and high to len(arr) - 1. Then we loop through the array until mid is greater than high. We check the value of arr[mid] and swap it with the value at arr[low] if it's 0, swap it with the value at arr[high] if it's 2, and leave it as is if it's 1. We then update the pointers accordingly and repeat until all elements have been processed.
