from math import log

class SparseTable:

    def __init__(self, arr):  # create Sparse Table using given Array
        self.arr = arr
        self.size = len(self.arr)     # length of the Array
        self.stable = [[0 for j in range(int(log(self.size, 2)) + 1)] for i in range(self.size)]

        for i in range(self.size):     # initialize first column with corresponding row number
            self.stable[i][0] = i

        j = 1
        while (1 << j) <= self.size:   # Build the Sparse table
            i = 0
            while (i + (1 << j) - 1) < self.size:
                if arr[self.stable[i][j - 1]] > arr[self.stable[i + (1 << (j - 1))][j - 1]]:
                    self.stable[i][j] = self.stable[i][j - 1]
                else:
                    self.stable[i][j] = self.stable[i + (1 << (j - 1))][j - 1]
                i += 1
            j += 1

    def max_query(self,l ,r):   # Range Maximum Query  :  [l,r)
        length = r-l+1
        k = int(log(length, 2))
        ans = max(self.arr[self.stable[l][k]], self.arr[self.stable[l + length - (1 << k)][k]])
        return ans              # return the mximum number in the range

if __name__ == '__main__':

    arr = [1,2,3,4,5,6,7,8,9]
    s_obj = SparseTable(arr)
    print(s_obj.max_query(2,5))
    print(s_obj.max_query(1,8))

