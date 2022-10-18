nums = []
print("Enter 10 Elements for the List: ")
for i in range(10):
  nums.append(int(input()))

for i in range(9):
    chk = 0
    small = nums[i]
    for j in range(i+1, 10):
        if small > nums[j]:
            small = nums[j]
            chk = chk + 1
            index = j
    if chk != 0:
        temp = nums[i]
        nums[i] = small
        nums[index] = temp

print("\nSorted List is: ")
for i in range(10):
    print(nums[i])
