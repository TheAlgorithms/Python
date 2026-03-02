import sys
import os
from hypothesis import given, strategies as st

# Add root directory to python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from searches.binary_search import binary_search

# Strategy to generate a sorted list of integers
sorted_list_strategy = st.lists(st.integers(), min_size=0).map(sorted)

@given(
    arr=sorted_list_strategy,
    # Pick a random integer as a potential target
    target=st.integers() 
)
def test_binary_search_property_based(arr, target):
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
        assert arr[result] == target, f"Index {result} pointed to {arr[result]}, not {target}."
        
        # Property: Verify it is the FIRST occurrence
        # Only check if the target is actually at the result index
        for i in range(result):
            assert arr[i] != target, f"Found target {target} at index {result}, but earlier occurrence at {i}."
    else:
        assert result == -1, f"Target {target} was not in {arr}, but found at index {result}."