from __future__ import print_function

__author__ = 'Nikhil Kumar'


class BIT(object):
    '''
    Binary indexed tree is a simple data structure that is helpful in situations when we have lots
    of queries which want to apply certain operation over a range of indexes in array. For example,
    lets assume we have an array of length N. There can be two types of queries:
        1. Change the value stored at an index i. (This is called a point update operation)
        2. Find the sum of a prefix of length k. (This is called a range sum query)
    In a traditional array, operation 1 would take O(1) time, while operation 2 would take O(N)
    time in worst case. And if we have 1 million queries of type 2, we will end up wasting lot
    of time.
    To come out of such cases, we use binary indexed trees(BlsIT). ( segment trees is other solution )
    I may run of space if i try to explain BIT here, but consider going to following links:

    https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/tutorial/
    https://cs.stackexchange.com/questions/10538/bit-what-is-the-intuition-behind-a-binary-indexed-tree-and-how-was-it-thought-a

    In general, it's a simple array where we store partial sums. Every index which is a power of 2,
    stores sum of numbers from the original array from index 1 to pow(2, index). For example an index of 8 in BIT would
    store complete sum of original array from index 1 to index 8. Then applying same logic
    recursively to other indexes and cleverly manipulating bits in indexes, we construct and query
    BIT. visit the links for more information.

    Running time:
        Update operation:  O(logN)
        Query operation:  O(logN)

    if you know about segment trees, you may find this data structure similar.
    The only reason we use BIT over segment tree becasue it takes less time to code it and
    it takes less space in memory.
    '''

    def __init__(self, arr):
        self.input = arr
        self.length = len(self.input)
        self.bit = [0] * (self.length + 1)  # we will use indexes from 1 ..N

    def construct(self):
        """
        constructs BIT.
        """
        for i in range(1, self.length + 1):
            self.update(i, self.input[i - 1])

    def update(self, index, val):
        """
        given and index and a value to update, update the element at the given index by value.
        """

        while index <= self.length:
            self.bit[index] += val
            index += (index & -index)  # this is a bit manipulation trick. visit the url for more.

    def query(self, index):
        """
        given an index, return sum of numbers in given array in interval [1, index] .
        """
        msum = 0
        while index > 0:
            msum += self.bit[index]
            index -= (index & -index)  # this is a bit manipulation trick. visit the url for more.
        return msum


def test_query(bit):
    """
    This runs query operations on BIT.
    Each query operation takes O(logN) time which is fast enough.
    """

    # testing query operations.
    print("running queries.")
    for i in range(1, len(arr) + 1):
        query_index = i
        print('sum from index 1 to index {0} is {1}'.format(query_index, bit.query(query_index)))


if __name__ == '__main__':

    arr = [8, 9, 10, 5, 6]  # lets take an example array.
    '''
    (if we assume the input array starts at index 1)
    BIT for this array would look like this. The square brackets at each value represent the range
    for which the sum is stored in BIT.

            32[1, 4]
           / \
    [1,2]17   6[5, 5]
          / \
    [1,1]8  [3,3]10

    '''
    bit = BIT(arr)
    bit.construct()
    delta = 5  # this is a constant value by which we shall update each element of the input array.

    test_query(bit)  # runs query operations.

    # update operations.
    print ("running updates")
    for i in range(len(arr)):
        update_index = i + 1
        print('updating index {0} by {1}'.format(update_index, delta))
        bit.update(update_index, delta)  # this is fast. runs in O(logN).

    test_query(bit)  # again run queries after an update.
