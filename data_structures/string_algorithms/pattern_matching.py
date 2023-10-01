# Author : Lakshit21 (https://github.com/Lakshit21)
# Check Code on : https://cses.fi/problemset/result/5753335/
# Date : 1st Oct 2023


class StringMatch:
    def __init__(self, function_method_name="Z_FUNCTION", separator="\uFFFF"):
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
            self.Function = self.__function_dictionary[function_method_name]
        else:  # Default to Z-function
            self.Function = self.__zfun_match

    def match(self, text: str, pattern: str):
        """
        Perform string matching on the given text using the selected algorithm.

        Args:
            text (str): The text to search within.
            pattern (str): The pattern to search for in the text.

        Returns:
            tuple: A tuple containing the occurrence count and occurrence indices.
        """

        def is_valid_text():
            return all(char != self.separator for char in text)
            # for char in text:
            #     if char == self.__separator:
            #         return False
            # return True

        def is_valid_pattern():
            return all(char != self.separator for char in pattern)
            # for char in text:
            #     if char == self.__separator:
            #         return False
            # return True

        if not is_valid_text():
            print("Err : Text ")
            return

        if not is_valid_pattern():
            print("Err : Pattern ")
            return

        occurrence_count, occurrence_indices = self.Function(text=text, pattern=pattern)

        return occurrence_count, occurrence_indices

    def __zfun_match(self, text: str, pattern: str):
        """
        Perform string matching using the Z-function algorithm.

        Args:
            text (str): The text to search within.
            pattern (str): The pattern to search for in the text.

        Returns:
            tuple: A tuple containing the occurrence count and occurrence indices.
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

    def __pifun_match(self, text: str, pattern: str):
        """
        Perform string matching using the Pi-function algorithm.

        Args:
            text (str): The text to search within.
            pattern (str): The pattern to search for in the text.

        Returns:
            tuple: A tuple containing the occurrence count and occurrence indices.
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

    def __merge_text_and_pattern(self, text: str, pattern: str):
        """
        Merge the text and pattern using a separator character.

        Args:
            text (str): The text to search within.
            pattern (str): The pattern to search for in the text.

        Returns:
            str: The merged string.
        """
        merged_string = pattern
        merged_string += self.__separator
        merged_string += text

        return merged_string

    def __z_function(self, merged_string: str):
        """
        Calculate the Z-function values for a given string.

        Args:
            merged_string (str): The string for which Z-function.

        Returns:
            list: A list of Z-function values for the input string.
        """
        s = merged_string

        n = len(s)

        z = [0] * n

        l, r = 0, 0

        def isequal(index_1: int, index_2: int):
            return s[index_1] == s[index_2]

        for i in range(1, n):
            if i < r:
                z[i] = min(r - i, z[i - l])
            while i + z[i] < n and isequal(z[i], i + z[i]):
                z[i] += 1
            if i + z[i] > r:
                l, r = i, i + z[i]

        return z

    def __pi_function(self, merged_string: str):
        """
        Calculate the Pi-function values for a given string.

        Args:
            merged_string (str): The string for which Pi-function.

        Returns:
            list: A list of Pi-function values for the input string.
        """
        s = merged_string

        n = len(s)

        pi = [0] * n

        def isequal(index_1: int, index_2: int):
            return s[index_1] == s[index_2]

        for i in range(1, n):
            j = pi[i - 1]
            while j > 0 and not isequal(i, j):
                j = pi[j - 1]
            if isequal(i, j):
                j += 1
            pi[i] = j

        return pi


"""
usage:

0. import file :)

1. Create Object Of the Class StringMatch with custom fields

obj = StringMatch(function_method_name='PI_FUNCTION', separator'$' )

2. provide text and pattern to the object method @match

text = "Hello It's Python"
pattern = "Python"
frq, List = obj.match(text=text, pattern=pattern)

"""
