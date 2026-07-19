from searches.simple_binary_search import binary_search


def test_binary_search_leftmost_duplicate():
    assert binary_search([1, 2, 2, 2, 3], 2) == 1


def test_binary_search_all_duplicates():
    assert binary_search([1, 1, 1, 1], 1) == 0


def test_binary_search_not_found():
    assert binary_search([1, 2, 3], 4) == -1


def test_binary_search_single_element():
    assert binary_search([5], 5) == 0

