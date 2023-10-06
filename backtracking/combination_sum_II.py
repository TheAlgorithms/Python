"""
The Combination Sum II function is used to generate the nth term of the Count and Say sequence.


Time complexity(Average Case): 0(m)

Constraints:
The input n is a positive integer.
The input n is bounded by 1 <= n <= 30.
This constraint is typically imposed to limit the size of the output string,
as the "Count and Say" sequence grows exponentially with n.
"""

class Solution:
    def count_and_say(self, n: int) -> str:
        """
        Generate the nth term of the "Count and Say" sequence.

        Args:
            n (int): The term number to generate.

        Returns:
            str: The nth term of the "Count and Say" sequence.

        Example:
            >>> solution = Solution()
            >>> solution.count_and_say(1)
            '1'
            >>> solution.count_and_say(4)
            '1211'
        """
        # Base case
        if n == 1:
            return "1"

        # Recursive case
        prev_term = self.count_and_say(n - 1)
        result = ""
        count = 1

        # Iterate through the previous term and generate the current term
        for i in range(len(prev_term)):
            if i < len(prev_term) - 1 and prev_term[i] == prev_term[i + 1]:
                count += 1
            else:
                result += str(count) + prev_term[i]
                count = 1

        return result

# Run doctests
if __name__ == "__main__":
    import doctest
    doctest.testmod()

