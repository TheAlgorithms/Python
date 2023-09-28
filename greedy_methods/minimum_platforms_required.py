"""
This is a pure Python implementation of the greedy algorithm
reference: https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1#

For doctests run following command:
python3 -m doctest -v minimum_platforms_required.py

Objective
First we will sort both arrays. When there is sorted events, it will be easy to maintain 
the count of trains that have arrived but not departed. The total platforms needed at one 
time can be found by taking the difference between arrivals and departures at that time and 
the maximum value of all times will be the final answer.


Approach
Sort both the arrays. So, that it is easy to maintain the count of trains by comparing, 
If(arr[i]<=dep[j]) means if arrival time is less than or equal to the departure time then-
we need one more platform. So increment count as well as increment i. If(arr[i]>dep[j]) 
means the arrival time is more than the departure time then- we have one extra platform 
which we can reduce. So decrement count but increment j. Update the ans with max(ans, count)
after each iteration of the while loop.

Time Complexity: Sorting takes O(nlogn) and traversal of arrays takes O(n)
		 so O(nlogn) + O(n) is approx. O(nlogn).
Space complexity: O(1)  (No extra space used).
"""

def countPlatforms(arrival_times: list, departure_times: list) -> int:
    """Function to count the minimum number of platforms required.

    Args:
        arrival_times (list): List of arrival times.
        departure_times (list): List of departure times.

    Returns:
        int: Minimum number of platforms required.

    Examples:
    >>> countPlatforms([900, 945, 955, 1100, 1500, 1800], [920, 1200, 1130, 1150, 1900, 2000])
    3
    """
    arrival_times.sort()
    departure_times.sort()

    platforms_needed = 1
    count = 1
    i = 1
    j = 0

    while i < len(arrival_times) and j < len(departure_times):
        if arrival_times[i] <= departure_times[j]:  # one more platform needed
            count += 1
            i += 1
        else:  # one platform can be reduced
            count -= 1
            j += 1
        platforms_needed = max(platforms_needed, count)  # updating the value with the current maximum

    return platforms_needed

if __name__ == "__main__":
    arr = [900, 945, 955, 1100, 1500, 1800]
    dep = [920, 1200, 1130, 1150, 1900, 2000]
    print("Minimum number of Platforms required ", countPlatforms(arr, dep))


