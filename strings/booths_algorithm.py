class BoothsAlgorithm:
    """
    Booth's Algorithm finds the lexicographically minimal rotation of a string.

    Time Complexity: O(n) - Linear time where n is the length of input string
    Space Complexity: O(n) - Linear space for failure function array

    For More Visit - https://en.wikipedia.org/wiki/Booth%27s_multiplication_algorithm
    """

    def find_minimal_rotation(self, string: str) -> str:
        """
        Find the lexicographically minimal rotation of the input string.

        Args:
            string (str): Input string to find minimal rotation.

        Returns:
            str: Lexicographically minimal rotation of the input string.

        Raises:
            ValueError: If the input is not a string or is empty.

        Examples:
            >>> ba = BoothsAlgorithm()
            >>> ba.find_minimal_rotation("baca")
            'abac'
            >>> ba.find_minimal_rotation("aaab")
            'aaab'
            >>> ba.find_minimal_rotation("abcd")
            'abcd'
            >>> ba.find_minimal_rotation("dcba")
            'adcb'
            >>> ba.find_minimal_rotation("aabaa")
            'aaaab'
        """
        if not isinstance(string, str) or not string:
            raise ValueError("Input must be a non-empty string")

        n = len(string)
        s = string + string  # Double the string to handle all rotations
        f = [-1] * (2 * n)  # Initialize failure function array with twice the length
        k = 0  # Starting position of minimal rotation

        for j in range(1, 2 * n):
            sj = s[j]
            i = f[j - k - 1]

            while i != -1 and sj != s[k + i + 1]:
                if sj < s[k + i + 1]:
                    k = j - i - 1
                i = f[i]

            if i == -1 and sj != s[k]:
                if sj < s[k]:
                    k = j
                f[j - k] = -1
            else:
                f[j - k] = i + 1

        return s[k : k + n]


if __name__ == "__main__":
    ba = BoothsAlgorithm()
    print(ba.find_minimal_rotation("bca"))  # output is 'abc'
