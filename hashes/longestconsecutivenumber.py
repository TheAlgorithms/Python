# using hash set


def longestConsecutive(nums):
    if len(nums) == 0:
        return 0
    set = set(nums)
    count = 1
    for num in nums:
        if num - 1 not in set:
            tempCount = 1
            while num + 1 in set:
                tempCount += 1
                num += 1
            count = max(count, tempCount)
        if count > len(nums) / 2:
            break
    return count


size = int(input())
nums = list(map(int, input().split()))
nums.sort()
print(longestConsecutive(nums))
