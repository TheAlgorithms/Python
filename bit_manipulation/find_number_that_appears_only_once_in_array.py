###

###


def findDuplicate(nums):
    duplicate_num = 0
    
    for i in nums:
        duplicate_num = duplicate_num ^ i;
    
    return duplicate_num

if __name__ == "__main__":
    nums = [1, 4, 1, 7, 9, 2, 9, 7, 2]
    print(findDuplicate(nums))
