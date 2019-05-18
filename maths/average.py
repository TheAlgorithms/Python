def average(nums):
    sum = 0
    n = 0
    for x in nums:
      sum += x
      n += 1
    avg = sum / n
    print(avg)

def main():
  average([2, 4, 6, 8, 20, 50, 70])

  #uncomment this to take input from user.
  #average(list(map(int, input("Enter a list a numbers seperated by commas: ").split(','))))

if __name__ == '__main__':
  main()
