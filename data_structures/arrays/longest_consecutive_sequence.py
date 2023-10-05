"""
author: Sarthak Sharma https://github.com/Sarthak950  https://sarthak950.netlify.app
date:   4 OCT 2023
Longest Consecutive Sequence Problem from LeetCode

"""

def longestConsecutiveSequence(self, nums: List[int]) -> int:
    # Create a map of all numbers in the array to their index
    nmap = defaultdict(int)
    for i in range(len(nums)):
        if nums[i] not in nmap:
            nmap[nums[i]] = i
    # Create a seen array to keep track of whether a number has been seen before
    seen, ans = [0] * len(nums), 0
    # Iterate through each number in the array
    for n in nums:
        # Set curr to the current number, and count to 1
        curr, count = n, 1
        # If we've already seen this number, skip it
        if seen[nmap[n]]:
            continue
        # Otherwise, iterate through all consecutive numbers after curr
        while curr + 1 in nmap:
            # Increment curr
            curr += 1
            # Check if we've seen this number before
            ix = nmap[curr]
            if seen[ix]:
                # If we have, add it to the count and break out of the loop
                count += seen[ix]
                break
            else:
                # Otherwise, add it to the seen array and increment the count
                seen[ix] = 1
                count += 1
        # Add the count to the seen array and update the answer
        seen[nmap[n]], ans = count, max(ans, count)
    # Return the answer
    return ans


"""
Idea
1.  First, we put all the numbers into a dictionary, and note the index of each number.
    This is to make sure the lookup time when we check if a number is in the list is O(1).
    We also initialize a seen list for later use.

2.  Then, we loop through the numbers, and for each number n, we check if it's already in seen list.
    If so, we skip it. Otherwise, we start counting the length of the consecutive sequence starting from n.
    This is done by checking if n+1 is in the dictionary. If so, we increment the counter, and set the seen status of n to 1.
    Otherwise, we set the seen status of n to 1, and break the loop.
    This is because if n+1 is not in the dictionary, then the consecutive sequence starting from n is over.
    And we don't need to count the length of the consecutive sequence starting from n+1, since we will eventually count it when we reach n+1.

"""
