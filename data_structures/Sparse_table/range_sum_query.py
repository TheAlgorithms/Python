from math import log

class SparseTable:

    def __init__(self, Arr):  # create Sparse Table using given Array
        self.Arr = Arr
        self.size = len(self.Arr)     # length of the Array
        self.Stable = [[0 for j in range(int(log(self.size, 2)) + 1)] for i in range(self.size)]

        for i in range(self.size):     # initialize first column with corresponding row number
            self.Stable[i][0] = Arr[i]

        j = 1
        while (1 << j) <= self.size:   # Build the Sparse table
            i = 0
            while (i + (1 << j) - 1) < self.size:
                self.Stable[i][j] = self.Stable[i][j - 1] + self.Stable[i + (1<<(j-1))][j-1]
                i += 1
            j += 1

    def sum_query(self,l ,r):   # Range Sum Query  :  [l,r)
        sum = 0
        k = int(log(self.size, 2))
        for j in range(k,-1,-1):
            if ((1<<j) <= (r-l+1)):
                sum+=self.Stable[l][j]
                l+=(1<<j)
        return sum

if __name__ == '__main__':

    Arr = [1,2,3,4,5,6,7,8,9]
    Sobj = SparseTable(Arr)
    print(Sobj.sum_query(1,3))
    print(Sobj.sum_query(1,8))
