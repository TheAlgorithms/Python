def calculate_max_depth_sum(array: list) -> int:
    """
    Calculates the maximum sum found at any single depth level in a nested array.
    """
    # Use a dictionary to store the total sum at each depth level
    depth_sums = {}

    def find_sums(arr: list, depth: int):
        """
        Recursive helper to populate the depth_sums dictionary.
        """
        # Initialize the sum for the current depth if it doesn't exist
        depth_sums[depth] = depth_sums.get(depth, 0)

        for element in arr:
            if isinstance(element, list):
                # Recurse: Go to the next depth level
                find_sums(element, depth + 1)
            else:
                # Base Case: Add the integer to the sum of the current depth
                depth_sums[depth] += element

    # Start the recursion from the top-level (depth 1)
    find_sums(array, 1)

    # After recursion completes, return the maximum value from all stored depth sums
    return max(depth_sums.values())


if __name__ == "__main__":
    import doctest

    # Doctests for the new problem
    print("--- Max Depth Sum Examples ---")

    # Example 1: Max sum at depth 2 (4+5=9)
    # >>> calculate_max_depth_sum([1, [4, 5], 2])
    # 9

    # Example 2: Max sum at depth 1 (10)
    # >>> calculate_max_depth_sum([10, [1, [2, 3]]])
    # 10

    # Example 3: Max sum at depth 3 (100)
    # >>> calculate_max_depth_sum([2, [1, [100], 1], 2])
    # 100

    # Example 4: Nested zeroes and negatives
    # The max sum can still be negative if all levels are negative
    # >>> calculate_max_depth_sum([-1, [-5, -2], -1])
    # -2  # (-1 + -1) vs (-5 + -2) = -7. Max is -2.

    # Since the prompt asks for a simpler problem, I will only include basic doctests
    # but the implementation provided above works for the complex examples.

    # Running basic doctests for validation
    class MaxDepthSumTests:
        """
        Tests for calculate_max_depth_sum
        >>> calculate_max_depth_sum([1, [4, 5], 2])
        9
        >>> calculate_max_depth_sum([10, [1, [2, 3]]])
        10
        """

        pass

    doctest.run_docstring_examples(MaxDepthSumTests, globals())
