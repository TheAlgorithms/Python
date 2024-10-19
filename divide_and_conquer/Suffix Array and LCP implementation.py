class SuffixArray:
    def __init__(self, input_string):
        """
        Initialize the SuffixArray with the input string and generate the suffix and LCP arrays.
        """
        self.input_string = input_string
        self.suffix_array = self._create_suffix_array()
        self.lcp_array = self._create_lcp_array()

    def _create_suffix_array(self):
        """
        Create the suffix array for the given input string.
        Returns the suffix array, which is a list of indices representing the starting positions of sorted suffixes.
        """
        length = len(self.input_string)
        sorted_suffixes = sorted(range(length), key=lambda i: self.input_string[i:])
        return sorted_suffixes

    def _create_lcp_array(self):
        """
        Construct the LCP (Longest Common Prefix) array based on the suffix array.
        LCP[i] stores the length of the longest common prefix between suffixes at suffix_array[i] and suffix_array[i-1].
        """
        length = len(self.input_string)
        suffix_array = self.suffix_array
        rank = [0] * length
        lcp = [0] * length

        # Generate the rank array where rank[i] indicates the position of the suffix starting at index i
        for index, suffix in enumerate(suffix_array):
            rank[suffix] = index

        lcp_length = 0
        for i in range(length):
            if rank[i] > 0:
                previous_suffix = suffix_array[rank[i] - 1]
                while (i + lcp_length < length) and (previous_suffix + lcp_length < length) and \
                        self.input_string[i + lcp_length] == self.input_string[previous_suffix + lcp_length]:
                    lcp_length += 1
                lcp[rank[i]] = lcp_length
                if lcp_length > 0:
                    lcp_length -= 1
        return lcp

    def display_arrays(self):
        """
        Print the suffix array and LCP array for the input string.
        """
        print("Suffix Array:")
        for idx in self.suffix_array:
            print(f"{idx}: {self.input_string[idx:]}")

        print("\nLCP Array:")
        for i in range(1, len(self.lcp_array)):
            print(f"LCP between {self.input_string[self.suffix_array[i-1]:]} and {self.input_string[self.suffix_array[i]:]}: {self.lcp_array[i]}")

# Example usage:
if __name__ == "__main__":
    input_text = "banana"
    suffix_array_instance = SuffixArray(input_text)

    # Show the suffix and LCP arrays
    suffix_array_instance.display_arrays()
