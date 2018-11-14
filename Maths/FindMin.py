# Time Complexity: O(n)
# Space Complexity: O(1) for n-inputs

def main():
    def findMin(x):
        return min(x) # Used built-in function min() on [x]

    print(findMin([0,1,2,3,4,5,-3,24,-56])) # = -56

if __name__ == '__main__':
    main()
