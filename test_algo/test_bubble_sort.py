import random
import unittest

from sorts.bubble_sort import bubble_sort


# testing the bubble_sort function
class TestBubbleSort(unittest.TestCase):
    # Full test
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([0, 5, 2, 3, 2]), [0, 2, 2, 3, 5])
        self.assertEqual(bubble_sort([0, 5, 2, 3, 2]), sorted([0, 5, 2, 3, 2]))
        self.assertEqual(bubble_sort([]), sorted([]))
        self.assertEqual(bubble_sort([-2, -45, -5]), sorted([-2, -45, -5]))
        self.assertEqual(bubble_sort([-23, 0, 6, -4, 34]), sorted([-23, 0, 6, -4, 34]))
        self.assertEqual(
            bubble_sort(["d", "a", "b", "e", "c"]), sorted(["d", "a", "b", "e", "c"])
        )

    def test_bubble_sort_random(self):

        collection = random.sample(range(-50, 50), 100)
        self.assertEqual(bubble_sort(collection), sorted(collection))

    def test_bubble_sort_string(self):
        import string

        collection = random.choices(string.ascii_letters + string.digits, k=100)
        self.assertEqual(bubble_sort(collection), sorted(collection))


if __name__ == "__main__":
    unittest.main()
