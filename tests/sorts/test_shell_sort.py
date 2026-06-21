from sorts.shell_sort import shell_sort


def test_shell_sort_basic():
    assert shell_sort([5, 2, 9, 1]) == [1, 2, 5, 9]


def test_shell_sort_empty():
    assert shell_sort([]) == []


def test_shell_sort_one_element():
    assert shell_sort([3]) == [3]


def test_shell_sort_sorted():
    assert shell_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_shell_sort_duplicates():
    assert shell_sort([4, 3, 3, 1]) == [1, 3, 3, 4]
