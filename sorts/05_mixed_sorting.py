# Mixed sorting

"""
Given a list of integers nums, sort the array such that:

All even numbers are sorted in increasing order
All odd numbers are sorted in decreasing order
The relative positions of the even and odd numbers remain the same
Example 1
Input

nums = [8, 13, 11, 90, -5, 4]
Output

[4, 13, 11, 8, -5, 90]
Explanation

The even numbers are sorted in increasing order, the odd numbers are sorted in 
decreasing number, and the relative positions were 
[even, odd, odd, even, odd, even] and remain the same after sorting.
"""

# solution

import unittest


def mixed_sorting(nums):
    positions = []
    odd = []
    even = []
    sorted_list = []
    for i in nums:
        if i%2 == 0:
            even.append(i)
            positions.append("E")
        else:
            odd.append(i)
            positions.append("O")
    even.sort()
    odd.sort()
    odd.reverse()
    j,k = 0,0
    for i in range(len(nums)):
        if positions[i] == "E":
            while j < len(even):
                sorted_list.append(even[j])
                j += 1
                break
        else:
            while k < len(odd):
                sorted_list.append(odd[k])
                k += 1
                break
            
    return sorted_list


# DO NOT TOUCH THE BELOW CODE


class TestMixedSorting(unittest.TestCase):
    def test_1(self):
        self.assertEqual(mixed_sorting(
            [8, 13, 11, 90, -5, 4]), [4, 13, 11, 8, -5, 90])

    def test_2(self):
        self.assertEqual(mixed_sorting([1, 2, 3, 6, 5, 4]), [5, 2, 3, 4, 1, 6])


if __name__ == '__main__':
    unittest.main(verbosity=2)
