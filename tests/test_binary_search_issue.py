from hypothesis import given, strategies as st

from searches.binary_search import binary_search

# Strategy to generate a sorted list of integers
sorted_list_strategy = st.lists(st.integers()).map(sorted)


@given(
    arr=sorted_list_strategy,
    target=st.integers(),
)
def test_binary_search_property_based(arr: list[int], target: int) -> None:
    """
    Property-based test:
    1. If target is in arr, binary_search MUST return an index 'i'
       such that arr[i] == target.
    2. If target is in arr, it MUST be the FIRST occurrence.
    3. If target is not in arr, binary_search MUST return -1.
    """
    result = binary_search(arr, target)

    if target in arr:
        assert result != -1, f"Target {target} was in {arr} but not found."
        assert arr[result] == target, f"Index {result} pointed to {arr[result]}."

        # Property: Verify it is the FIRST occurrence
        # Check that target does not exist at any index before 'result'
        for i in range(result):
            assert arr[i] != target, f"Target at {result}, but earlier at {i}."
    else:
        assert result == -1, f"Target {target} not in {arr}, but found at {result}."
