import unittest


def longest_palindromic_substring(string: str) -> str:
    """
    Manacher’s algorithm which finds Longest Palindromic Substring.
    Source: https://en.wikipedia.org/wiki/Longest_palindromic_substring
    """
    if string == "":
        return ""

    # create string with separators: "aba" -> "a|b|a"
    new_string = "|".join(list(string))

    left = right = 0  # start/end index of longest palindrome so far
    # length[i] shows the length of palindromic substring with center i
    length = [1] * len(new_string)
    start = max_length = 0

    # for each character in new_string find the corresponding max palindrome length
    #   and store the length and left, right boundary
    for i, _ in enumerate(new_string):
        k = 1 if i > right else min(length[left + right - i] // 2, right - i + 1)
        while (
            i - k >= 0
            and i + k < len(new_string)
            and new_string[k + i] == new_string[i - k]
        ):
            k += 1

        length[i] = 2 * k - 1

        # update the right and left index if string ends after the previously right      
        if i + k - 1 > right:
            left = i - k + 1  # noqa: E741
            right = i + k - 1

        if max_length < length[i]:
            max_length = length[i]
            start = i

    s = new_string[start - max_length // 2 : start + max_length // 2 + 1]
    return "".join(s.split("|"))


class TestLongestPalindrome(unittest.TestCase):
    def test_longest_palindromic_substring(self):
        self.assertEqual(longest_palindromic_substring("abbbaba"), "abbba")
        self.assertEqual(longest_palindromic_substring("ababa"), "ababa")
        self.assertEqual(longest_palindromic_substring(""), "")
        self.assertEqual(longest_palindromic_substring("a"), "a")
        self.assertEqual(longest_palindromic_substring("aa"), "aa")
        self.assertEqual(longest_palindromic_substring("abc"), "b")


if __name__ == "__main__":
    unittest.main()
