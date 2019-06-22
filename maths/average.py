def average(nums):
    sum = 0
    for x in nums:
      sum += x
    avg = sum / len(nums)
    print(avg)
    return avg

def main():
  average([2, 4, 6, 8, 20, 50, 70])

if __name__ == '__main__':
  main()
