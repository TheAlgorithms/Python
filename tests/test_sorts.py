from sorts.heap_sort import heap_sort


def test_heap_sort():
    assert heap_sort([]) == []
    assert heap_sort([1]) == [1]
    assert heap_sort([5, 2, 5, 1]) == [1, 2, 5, 5]
    assert heap_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
