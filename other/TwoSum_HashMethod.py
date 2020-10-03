
class Solution:
    def twoSumHashing(self,num_arr, pair_sum): # hash method
        sums = []
        hashTable = {}

        for i in range(len(num_arr)):
            complement = pair_sum - num_arr[i]
            if complement in hashTable:
                print("Pair with sum", pair_sum,"is: (", num_arr[i],",",complement,")")
            hashTable[num_arr[i]] = num_arr[i]



if __name__ == "__main__":
    s = Solution()
    os.system("clear")
    list = [3,2,4]
    target = 6
    print(len(list))
    print(s.twoSumHashing(list,target))

