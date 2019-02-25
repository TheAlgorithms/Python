import pytest

from sorts.bogosort import bogosort


@pytest.mark.timeout(5)
class TestBogosort:
    """Test cases for bogosort, with a 5 second timeout on each. It
    is exceedingly unlikely that any of these would time out, but
    it could technically happen. Do not add any test cases
    sorting large lists, it could take a long time.
    """

    @staticmethod
    def test_sorts_empty_list():
        lst = []
        bogosort(lst)
        assert lst == []

    @staticmethod
    def test_sorts_small_list():
        lst = [0, 5, 3, 2, 2]
        expected = sorted(lst)

        bogosort(lst)

        assert lst == expected

    @staticmethod
    def test_sorts_reversed_list():
        lst = [-45, -5, -2]
        expected = sorted(lst)

        bogosort(lst)

        assert lst == expected
