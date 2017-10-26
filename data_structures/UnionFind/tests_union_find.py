from union_find import UnionFind
import unittest


class TestUnionFind(unittest.TestCase):
    def test_init_with_valid_size(self):
        uf = UnionFind(5)
        self.assertEqual(uf.size, 5)

    def test_init_with_invalid_size(self):
        with self.assertRaises(ValueError):
            uf = UnionFind(0)

        with self.assertRaises(ValueError):
            uf = UnionFind(-5)

    def test_union_with_valid_values(self):
        uf = UnionFind(10)

        for i in range(11):
            for j in range(11):
                uf.union(i, j)

    def test_union_with_invalid_values(self):
        uf = UnionFind(10)

        with self.assertRaises(ValueError):
            uf.union(-1, 1)

        with self.assertRaises(ValueError):
            uf.union(11, 1)

    def test_same_set_with_valid_values(self):
        uf = UnionFind(10)

        for i in range(11):
            for j in range(11):
                if i == j:
                    self.assertTrue(uf.same_set(i, j))
                else:
                    self.assertFalse(uf.same_set(i, j))

        uf.union(1, 2)
        self.assertTrue(uf.same_set(1, 2))

        uf.union(3, 4)
        self.assertTrue(uf.same_set(3, 4))

        self.assertFalse(uf.same_set(1, 3))
        self.assertFalse(uf.same_set(1, 4))
        self.assertFalse(uf.same_set(2, 3))
        self.assertFalse(uf.same_set(2, 4))

        uf.union(1, 3)
        self.assertTrue(uf.same_set(1, 3))
        self.assertTrue(uf.same_set(1, 4))
        self.assertTrue(uf.same_set(2, 3))
        self.assertTrue(uf.same_set(2, 4))

        uf.union(4, 10)
        self.assertTrue(uf.same_set(1, 10))
        self.assertTrue(uf.same_set(2, 10))
        self.assertTrue(uf.same_set(3, 10))
        self.assertTrue(uf.same_set(4, 10))

    def test_same_set_with_invalid_values(self):
        uf = UnionFind(10)

        with self.assertRaises(ValueError):
            uf.same_set(-1, 1)

        with self.assertRaises(ValueError):
            uf.same_set(11, 0)


if __name__ == '__main__':
    unittest.main()
