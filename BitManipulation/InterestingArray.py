'''
Problem Constraints
1 <= N <= 100000
1 <= A[i] <= 10 ^ 6


Input Format
The first argument is an integer array A of size N.


Output Format
Return "Yes" if it is possible otherwise return "No".


Example Input
A = [9, 17]


Example Output
Yes


Example Explanation
Following is one possible sequence of operations -
1) Merge i.e 9 XOR 17=24
2) Split 24 into two parts each of size 12
3) Merge i.e 12 XOR 12=0
As there is only 1 element i.e 0. So it is possible.
'''


class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        sum = 0
        n = len(A)
        for i in range(0, n):
            sum += A[i]

        if sum % 2 == 0:
            return "Yes"
        else:
            return "No"
