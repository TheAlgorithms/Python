# Python program to find all subsets of given set. Any
# repeated subset is considered only once in the output
def find_subsets(ind, nums, ds, ans_list):
	ans_list.append(list(ds))
	for i in range(ind, len(nums)):
		if i != ind and nums[i] == nums[i - 1]:
			continue

		ds.append(nums[i])
		find_subsets(i + 1, nums, ds, ans_list)
		ds.pop()

def all_subsets(arr):
	nums = sorted(arr)
	ans_list = []
	find_subsets(0, nums, [], ans_list)
	return ans_list

if __name__ == "__main__":
	set = [10, 12, 12]
	subsets = all_subsets(set)

	for subset in subsets:
		print(subset, end=", ")
