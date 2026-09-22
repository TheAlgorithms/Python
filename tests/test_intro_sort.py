import pytest

from sorts.intro_sort import sort


@pytest.mark.parametrize(
    ("values", "expected"),
    (([3, 1, 2], [1, 2, 3]), (["b", "a", "c"], ["a", "b", "c"])),
)
def test_sort_comparable(values, expected) -> None:
    assert sort(values) == expected


def test_sort_rejects_incomparable_values() -> None:
    with pytest.raises(TypeError):
        sort([1, "a"])
