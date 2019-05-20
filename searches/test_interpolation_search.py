import unittest
from interpolation_search import interpolation_search, interpolation_search_by_recursion

class Test_interpolation_search(unittest.TestCase):
    def setUp(self):
        # un-sorted case
        self.collection1 = [5,3,4,6,7]
        self.item1 = 4
        # sorted case, result exists
        self.collection2 = [10,30,40,45,50,66,77,93]
        self.item2 = 66
        # sorted case, result doesn't exist
        self.collection3 = [10,30,40,45,50,66,77,93]
        self.item3 = 67
        # equal elements case, result exists
        self.collection4 = [10,10,10,10,10]
        self.item4 = 10
        # equal elements case, result doesn't exist
        self.collection5 = [10,10,10,10,10]
        self.item5 = 3
        # 1 element case, result exists
        self.collection6 = [10]
        self.item6 = 10
        # 1 element case, result doesn't exists
        self.collection7 = [10]
        self.item7 = 1

    def tearDown(self):
        pass

    def test_interpolation_search(self):
        self.assertEqual(interpolation_search(self.collection1, self.item1), None)
        
        self.assertEqual(interpolation_search(self.collection2, self.item2), self.collection2.index(self.item2))
        
        self.assertEqual(interpolation_search(self.collection3, self.item3), None)
        
        self.assertEqual(interpolation_search(self.collection4, self.item4), self.collection4.index(self.item4))

        self.assertEqual(interpolation_search(self.collection5, self.item5), None)
        
        self.assertEqual(interpolation_search(self.collection6, self.item6), self.collection6.index(self.item6))
        
        self.assertEqual(interpolation_search(self.collection7, self.item7), None)
        


class Test_interpolation_search_by_recursion(unittest.TestCase):
    def setUp(self):
        # un-sorted case
        self.collection1 = [5,3,4,6,7]
        self.item1 = 4
        # sorted case, result exists
        self.collection2 = [10,30,40,45,50,66,77,93]
        self.item2 = 66
        # sorted case, result doesn't exist
        self.collection3 = [10,30,40,45,50,66,77,93]
        self.item3 = 67
        # equal elements case, result exists
        self.collection4 = [10,10,10,10,10]
        self.item4 = 10
        # equal elements case, result doesn't exist
        self.collection5 = [10,10,10,10,10]
        self.item5 = 3
        # 1 element case, result exists
        self.collection6 = [10]
        self.item6 = 10
        # 1 element case, result doesn't exists
        self.collection7 = [10]
        self.item7 = 1

    def tearDown(self):
        pass

    def test_interpolation_search_by_recursion(self):
        self.assertEqual(interpolation_search_by_recursion(self.collection1, self.item1, 0, len(self.collection1)-1), None)
        
        self.assertEqual(interpolation_search_by_recursion(self.collection2, self.item2, 0, len(self.collection2)-1), self.collection2.index(self.item2))
        
        self.assertEqual(interpolation_search_by_recursion(self.collection3, self.item3, 0, len(self.collection3)-1), None)
        
        self.assertEqual(interpolation_search_by_recursion(self.collection4, self.item4, 0, len(self.collection4)-1), self.collection4.index(self.item4))

        self.assertEqual(interpolation_search_by_recursion(self.collection5, self.item5, 0, len(self.collection5)-1), None)
        
        self.assertEqual(interpolation_search_by_recursion(self.collection6, self.item6, 0, len(self.collection6)-1), self.collection6.index(self.item6))
        
        self.assertEqual(interpolation_search_by_recursion(self.collection7, self.item7, 0, len(self.collection7)-1), None)
 


if __name__ == '__main__':
    unittest.main()
