# All permutations:
def permute(nums: list[int]) -> list[list[int]]:
    result=[]
    if len(nums)==1:
        return [nums.copy()]
    for _ in range(len(nums)):
        n=nums.pop(0)
        permutations=permute(nums)
        for perm in permutations:
            perm.append(n)
        result.extend(permutations)
        nums.append(n)
    return result

def main() -> None: # Main function for testing.
	nums=[1,2,3]
	print("permutations are:",permute(nums))

if __name__=="__main__": 
	main()
