from math import log

class SparseTable:

    def __init__(self, Arr):  # create Sparse Table using given Array
        self.Arr = Arr
        self.size = len(self.Arr)     # length of the Array
        self.Stable = [[0 for j in range(int(log(self.size, 2)) + 1)] for i in range(self.size)]

        for i in range(self.size):     # initialize first column with corresponding row number
            self.Stable[i][0] = i

        j = 1
        while (1 << j) <= self.size:   # Build the Sparse table
            i = 0
            while (i + (1 << j) - 1) < self.size:
                if Arr[self.Stable[i][j - 1]] > Arr[self.Stable[i + (1 << (j - 1))][j - 1]]:
                    self.Stable[i][j] = self.Stable[i][j - 1]
                else:
                    self.Stable[i][j] = self.Stable[i + (1 << (j - 1))][j - 1]
                i += 1
            j += 1

    def max_query(self,l ,r):   # Range Maximum Query  :  [l,r)
        length = r-l+1
        k = int(log(length, 2))
        ans = max(self.Arr[self.Stable[l][k]], self.Arr[self.Stable[l + length - (1 << k)][k]])
        return ans              # return the mximum number in the range

if __name__ == '__main__':

    Arr = [1,2,3,4,5,6,7,8,9]
    Sobj = SparseTable(Arr)
    print(Sobj.max_query(2,5))
    print(Sobj.max_query(1,8))