from typing import List

# Function to find the minimum number of platforms required.
def find_platform_optimized(arr: List[int], dep: List[int], n: int) -> int:

    count = 0
    max_platforms = 0

    # Find the maximum departure time
    max_departure_time = max(dep)

    # Create a list to store the count of trains at each time
    v = [0] * (max_departure_time + 2)

    # Increment the count at the arrival time and decrement at the departure time
    for i in range(n):
        v[arr[i]] += 1
        v[dep[i] + 1] -= 1

    # Iterate over the list and keep track of the maximum sum seen so far
    for i in range(max_departure_time + 2):
        count += v[i]
        max_platforms = max(max_platforms, count)

    return max_platforms

# Driver Code
if __name__ == '__main__':
    arr = []
    dep = []
    n = int(input())

    for i in range(0, n):
        ele = int(input())
        arr.append(ele)
    for j in range(0, n):
        ele1 = int(input())
        dep.append(ele1)
    print(find_platform_optimized(arr, dep, n))