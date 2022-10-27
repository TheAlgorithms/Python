import unittest

from sorts.radix_sort import radix_sort


# testing the radix_sort function
class TestRadixSort(unittest.TestCase):
    # Full test
    def test_radix_sort(self):
        self.assertEqual(radix_sort([0, 5, 2, 3, 2]), [0, 2, 2, 3, 5])
        self.assertEqual(radix_sort([0, 5, 2, 3, 2]), sorted([0, 5, 2, 3, 2]))
        self.assertEqual(radix_sort([]), sorted([]))
        self.assertEqual(radix_sort([-2, -45, -5]), sorted([-2, -45, -5]))
        self.assertEqual(radix_sort([-23, 0, 6, -4, 34]), sorted([-23, 0, 6, -4, 34]))
        self.assertEqual(
            radix_sort(["d", "a", "b", "e", "c"]), sorted(["d", "a", "b", "e", "c"])
        )

    def test_radix_sort_random(self):
        import random

        collection = random.sample(range(-50, 50), 100)
        self.assertEqual(radix_sort(collection), sorted(collection))

    def test_radix_sort_string(self):
        import random
        import string

        collection = random.choices(string.ascii_letters + string.digits, k=100)
        self.assertEqual(radix_sort(collection), sorted(collection))


# main
if __name__ == "__main__":
    unittest.main()
