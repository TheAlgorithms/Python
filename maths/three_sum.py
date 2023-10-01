"""
The "Three Sum" problem is a commonly encountered problem in computer science and data analysis.

1. **Data Analysis**: In data analysis and statistics, the Three Sum problem can be used to identify sets of data points that, when combined, result in a specific outcome or condition. For example, it can be applied to financial data to find combinations of transactions that balance an account.

2. **Optimization**: In optimization problems, such as resource allocation or scheduling, the Three Sum problem can help identify combinations of resources or tasks that result in a desired outcome. This is valuable in industries like logistics and project management.

3. **Algorithmic Research**: Researchers and algorithm designers often use the Three Sum problem as a benchmark for evaluating the efficiency and performance of algorithms. It serves as a challenging problem to test new algorithmic techniques.

4. **Cryptography**: Some cryptographic protocols involve operations on large numbers or sets of numbers. The Three Sum problem can be used as part of cryptographic algorithms to verify or validate certain conditions.

In summary, the Three Sum problem has practical applications in various fields, including data analysis, optimization, algorithmic research, pattern recognition, and cryptography. Its versatility makes it a valuable problem for both theoretical analysis and real-world problem-solving.
"""

def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Find all unique triplets in a sorted array of integers that sum up to zero.

    Args:
        nums: A sorted list of integers.

    Returns:
         A list of lists containing unique triplets that sum up to zero.

    Example:
        >>> three_sum([-1, 0, 1, 2, -1, -4])
        [[-1, -1, 2], [-1, 0, 1]]
        >>> three_sum([1, 2, 3, 4])
        []

    """
    nums.sort()
    ans = []
    for i in range(len(nums) - 2):
        if i == 0 or (nums[i] != nums[i - 1]):
            low, high, c = i + 1, len(nums) - 1, 0 - nums[i]
            while low < high:
                if nums[low] + nums[high] == c:
                    ans.append([nums[i], nums[low], nums[high]])

                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1

                    low += 1
                    high -= 1
                elif nums[low] + nums[high] < c:
                    low += 1
                else:
                    high -= 1
    return ans


# Run the doctests
if __name__ == "__main__":
    import doctest

    doctest.testmod()
