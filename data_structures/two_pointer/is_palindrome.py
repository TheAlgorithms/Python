"""
Problem Overview:
https://www.geeksforgeeks.org/check-if-a-number-is-palindrome/
Is Palindrome - Easy - Spotify

Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward.
It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters
we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.

"""


class Solution:
    def is_palindrome(self, s: str) -> bool:
        """
        This method checks whether the input string `s` is a palindrome or not.
        It ignores non-alphanumeric characters and is case-insensitive.

        Parameters:
        s (str): The input string to check.

        Returns:
        bool: True if the string is a palindrome, False otherwise.

        >>> Solution().is_palindrome("Was it a car or a cat I saw?")
        True
        >>> Solution().is_palindrome("tab a cat")
        False
        >>> Solution().is_palindrome("")
        True
        >>> Solution().is_palindrome("A")
        True
        """

        """
        Initialize two pointers, left (l) at the start, and right (r) at
        the end of the string.
        """
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters from the left pointer.
            while left < right and not self.is_alpha_numeric(s[left]):
                left += 1
            # Skip non-alphanumeric characters from the right pointer.
            while left < right and not self.is_alpha_numeric(s[right]):
                right -= 1

            # Compare characters at both pointers in a case-insensitive way.
            if s[left].lower() != s[right].lower():
                return False

            # Move both pointers towards the center.
            left, right = left + 1, right - 1

        # If all characters match, it is a palindrome.
        return True

    def is_alpha_numeric(self, c: str) -> bool:
        """
        Helper function to check if a character is alphanumeric (A-Z, a-z, 0-9).

        Parameters:
        c (str): The character to check.

        Returns:
        bool: True if the character is alphanumeric, False otherwise.
        """
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
