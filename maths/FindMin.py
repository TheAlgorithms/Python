def find_min(nums):
    min = nums[0]
    for x in nums:
        if min > x:
            min = x
    return min

def main():
    print(findMin([0,1,2,3,4,5,-3,24,-56])) # = -56

if __name__ == '__main__':
    main()
