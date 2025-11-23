from searches.binary_search import binary_search


def test_binary_search_with_duplicates():
    arr = [1, 2, 2, 2, 3, 4]
    result = binary_search(arr, 2)
    # It should return a valid index (1, 2, or 3)
    assert result in (1, 2, 3)


def test_binary_search_unique_elements():
    arr = [1, 2, 3, 4, 5]
    assert binary_search(arr, 3) == 2


def test_binary_search_not_found():
    arr = [1, 2, 3, 4, 5]
    assert binary_search(arr, 6) == -1
