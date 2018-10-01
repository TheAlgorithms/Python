import unittest


class TestSort(unittest.TestCase):
    """Base class of sorting tests."""

    def __init__(self, *args, **kwargs):
        try:
            # pylint: disable=E1003
            super(unittest.TestCase, self).__init__(*args, **kwargs) # Python 2
        except TypeError:
            super().__init__(*args, **kwargs) # Python 3
        self.canSortDuplicateValues = True
        self.canSortNegativeValues = True

    def runSortingSuite(self, function, doesSortInPlace=False):
        """Check that a sorting function correctly sorts across a suite of tests."""
        if self.canSortDuplicateValues:
            self.assertSorts(function, [1, 5, 3, 2, 2], doesSortInPlace, message="Should sort a list containing duplicate values")

        if self.canSortNegativeValues:
            self.assertSorts(function, [-5, -3, -6, 2], doesSortInPlace, message="Should sort a list containing negative values")
        
        self.assertSorts(function, [], doesSortInPlace, message="Should sort an empty list")
        self.assertSorts(function, [2, 1], doesSortInPlace, message="Should sort a basic list")
        self.assertSorts(function, [1, 5, 3, 2], doesSortInPlace, message="Should sort a list containing only positive values")
        self.assertSorts(function, [5, 3, 2, 0], doesSortInPlace, message="Should sort a list containing non-negative values")
        

    def assertSorts(self, function, collection, doesSortInPlace, message=""):
        """Assert that a function sorts a collection in ascending order."""
        expected = sorted(collection)
        result = function(collection)
        if doesSortInPlace:
            self.assertEqual(expected, collection, message)
        else:
            self.assertEqual(expected, result, message)