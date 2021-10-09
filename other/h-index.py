# Problem Link: https://leetcode.com/problems/h-index/

'''
AUTHOR: github.com/shreayan98c

PROBLEM STATEMENT:
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith
paper, return compute the researcher's h-index.
According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n papers have at least h
citations each, and the other n − h papers have no more than h citations each.
If there are several possible values for h, the maximum one is taken as the h-index.

EXAMPLES:

Example 1:
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5
citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations
each, their h-index is 3.

Example 2:
Input: citations = [1,3,1]
Output: 1

HINT: For instance, an h-index of 17 means that the scientist has published at least 17 papers that have each been cited
at least 17 times

LOGIC:
1. The h-index is calculated by counting the number of publications for which an author has been cited by other authors
at least that same number of times.
2. First sort the citations list in reverse order.
3. Now traverse the reverse sorted list of the citations - At each index, it will give us a track of how many
publications have been counted yet and what is the number of citations at the current index.
4. If our number of publications that have been counted is greater than the current citation, we will be incrementing
the result by 1 since the current publication has to be included in the h - index.
5. Return the total number of the publications counted in the previous step.

COMPLEXITY:
Time Complexity: O(n), n is the length of the citations list given as the input.
Space Complexity: O(1), no list is created or stored in the memory, just one variable to keep a track of the result.
'''
from typing import List


class Solution:

    def h_index(self, citations: List[int]) -> int:
        """
        Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith
        paper, return compute the researcher's h-index. A scientist has an index h if h of their n papers have at least h
        citations each, and the other n − h papers have no more than h citations each.

        Testcases:
        soln = Solution()
        soln.h_index([3,0,6,1,5])
        3

        soln = Solution()
        soln.h_index([3,0,6,1,5])
        3
        """
        return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))
