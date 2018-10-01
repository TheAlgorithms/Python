import unittest
from .test_sort import TestSort
from ..bucket_sort import bucketSort


class TestBucketSort(TestSort):    
    def test_sort(self):
        self.runSortingSuite(bucketSort)