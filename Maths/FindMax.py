# NguyenU

import math
#function to find the max number in the sequency.
def find_max(nums):
    max = 0
    for x in nums:
      if x > max: #any number greater than the maximum will become the new maximum.
        max = x
    print(max)

def main():
  find_max([2, 4, 9, 7, 19, 94, 5])

if __name__ == '__main__':
  main()
