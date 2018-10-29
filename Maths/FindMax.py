def find_max(nums):
    m=sorted(nums,reverse=True)
    print(m[0])
 
def main():
  find_max([2, 4, 9, 7, 19, 94, 5])

if __name__ == '__main__':
  main()
