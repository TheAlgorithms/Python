# Author : Lakshit21 (https://github.com/Lakshit21)
# Check Code on : https://cses.fi/problemset/result/5753335/
# Date : 1st Oct 2023

# references
# https://cp-algorithms.com/string/z-function.html
# https://cp-algorithms.com/string/prefix-function.html


def isequal(index_1: int, index_2: int, s: str) -> bool:
    """
    Check if two characters at the given indices in a string are equal.

    Args:
        index_1 (int): The index of the first character.
        index_2 (int): The index of the second character.
        s (str): The string in which to compare characters.

    Returns:
        bool: If same character then return True, else return False

    Examples:
    >>> isequal(1,2,"caab")
    True
    >>> isequal(1,2,"cadb")
    False
    """
    return s[index_1] == s[index_2]


class StringMatch:
    def __init__(
        self, function_method_name: str = "Z_FUNCTION", separator: str = "\uFFFF"
    ) -> None:
        """
        Initialize the StringMatch class.

        Args:
            function_method_name (str): The string matching algorithm to use.
            separator (str): The separator character to merge text and pattern.

        Note:
            You can specify the matching algorithm using 'function_method_name'.
        """
        self.__separator = separator  # default is '\uFFFF' least used Unicode

        # Dictionary mapping method names to corresponding functions
        self.__function_dictionary = {
            "Z_FUNCTION": self.__zfun_match,
            "PI_FUNCTION": self.__pifun_match,
        }
        # to be added...

        if function_method_name in self.__function_dictionary:
            self.use_function = self.__function_dictionary[function_method_name]
        else:  # Default to Z-function
            self.use_function = self.__zfun_match

    def match(self, text: str, pattern: str) -> tuple[int, list[int]]:
        """
        Perform string matching on the given text using the selected algorithm.

        Args:
            text (str): The text to search within.
            pattern (str): The pattern to search for in the text.

        Returns:
            tuple: A tuple containing the occurrence count and occurrence indices.

        Examples:
        >>> print(StringMatch().match("aaaaaaaaaa","a"))
        (10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        >>> print(StringMatch().match("joeuljjo","jo"))
        (2, [0, 6])
        >>> print(StringMatch().match("abababbab","ab"))
        (4, [0, 2, 4, 7])
        >>> print(StringMatch().match("abaaabaa","aaba"))
        (1, [3])
        >>> print(StringMatch().match("becodecode","becode"))
        (1, [0])
        >>> print(StringMatch().match("bbcws","xwfaq"))
        (0, [])
        """
        # assume the text and pattern do not contain separator

        occurrence_count, occurrence_indices = self.use_function(
            text=text, pattern=pattern
        )

        return occurrence_count, occurrence_indices

    def __zfun_match(self, text: str, pattern: str) -> tuple[int, list[int]]:
        """
        Perform string matching using the Z-function algorithm.

        Args:
            text (str): The text to search within.
            pattern (str): The pattern to search for in the text.

        Returns:
            tuple: A tuple containing the occurrence count and occurrence indices.

        Examples:
        >>> print(StringMatch().match("aaaaaaaaaa","a"))
        (10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        >>> print(StringMatch().match("joeuljjo","jo"))
        (2, [0, 6])
        >>> print(StringMatch().match("abababbab","ab"))
        (4, [0, 2, 4, 7])
        >>> print(StringMatch().match("abaaabaa","aaba"))
        (1, [3])
        >>> print(StringMatch().match("becodecode","becode"))
        (1, [0])
        >>> print(StringMatch().match("bbcws","xwfaq"))
        (0, [])
        """
        merged_string = self.__merge_text_and_pattern(text=text, pattern=pattern)

        z = self.__z_function(merged_string)

        offset = len(pattern) + 1

        pattern_count = 0
        pattern_indices = []
        for i in range(len(text)):
            j = i + offset
            if z[j] == len(pattern):
                pattern_count += 1
                pattern_indices.append(i)

        return pattern_count, pattern_indices

    def __pifun_match(self, text: str, pattern: str) -> tuple[int, list[int]]:
        """
        Perform string matching using the Pi-function algorithm.

        Args:
            text (str): The text to search within.
            pattern (str): The pattern to search for in the text.

        Returns:
            tuple: A tuple containing the occurrence count and occurrence indices.

        >>> print(StringMatch(function_method_name='PI_FUNCTION').match("aaaaaa","a"))
        (6, [0, 1, 2, 3, 4, 5])
        """
        merged_string = self.__merge_text_and_pattern(text=text, pattern=pattern)

        pi = self.__pi_function(merged_string=merged_string)

        offset = len(pattern) + 1

        pattern_count = 0
        pattern_indices = []
        for i in range(len(text)):
            j = i + offset
            if pi[j] == len(pattern):
                pattern_count += 1
                pattern_indices.append(j - 2 * (len(pattern)))

        return pattern_count, pattern_indices

    def __merge_text_and_pattern(self, text: str, pattern: str) -> str:
        """
        Merge the text and pattern using a separator character.

        Args:
            text (str): The text to search within.
            pattern (str): The pattern to search for in the text.

        Returns:
            str: The merged string.

        Examples:
        >>> print(StringMatch()._StringMatch__merge_text_and_pattern("A","B"))
        B￿A
        """
        merged_string = pattern
        merged_string += self.__separator
        merged_string += text

        return merged_string

    def __z_function(self, merged_string: str) -> list[int]:
        """
        Calculate the Z-function values for a given string.

        Args:
            merged_string (str): The string for which Z-function.

        Returns:
            list: A list of Z-function values for the input string.

        Examples:
        >>> print(StringMatch(separator='$')._StringMatch__z_function("abaabca"))
        [0, 0, 1, 2, 0, 0, 1]
        """
        s = merged_string

        n = len(s)

        z = [0] * n

        l, r = 0, 0

        for i in range(1, n):
            if i < r:
                z[i] = min(r - i, z[i - l])
            while i + z[i] < n and isequal(z[i], i + z[i], s):
                z[i] += 1
            if i + z[i] > r:
                l, r = i, i + z[i]

        return z

    def __pi_function(self, merged_string: str) -> list[int]:
        """
                Calculate the Pi-function values for a given string.

                Args:
                    merged_string (str): The string for which Pi-function.

                Returns:
                    list: A list of Pi-function values for the input string.

                Examples:
        >>> print(StringMatch()._StringMatch__pi_function("abaabca"))
        [0, 0, 1, 1, 2, 0, 1]
        """
        s = merged_string

        n = len(s)

        pi = [0] * n

        for i in range(1, n):
            j = pi[i - 1]
            while j > 0 and not isequal(i, j, s):
                j = pi[j - 1]
            if isequal(i, j, s):
                j += 1
            pi[i] = j

        return pi


if __name__ == "__main__":
    import doctest

    print(StringMatch().match("aaaaaaaaaa", "a"))
    print(StringMatch().match("joeuljjo", "jo"))
    print(StringMatch().match("abababbab", "ab"))
    print(StringMatch().match("abaaabaa", "aaba"))
    print(StringMatch().match("becodecode", "becode"))
    print(StringMatch().match("bbcws", "xwfaq"))
    print(StringMatch(function_method_name="PI_FUNCTION").match("aaaaaaaaaa", "a"))
    print(StringMatch(function_method_name="PI_FUNCTION").match("joeuljjo", "jo"))
    print(StringMatch(function_method_name="PI_FUNCTION").match("abababbab", "ab"))
    print(StringMatch(function_method_name="PI_FUNCTION").match("abaaabaa", "aaba"))
    print(StringMatch(function_method_name="PI_FUNCTION").match("bbcws", "xwfaq"))

    doctest.testmod()
