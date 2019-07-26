
#Implementaion of more than one stacks in one array
class Multistacks:
	'''
	Implementation of more than one stack in a single array
	'''
	def __init__(self,num_stacks):
		'''arguments : number of stacks in the array(num_stacks)'''
		self.arr = []
		self.bottoms = []
		for each in range(num_stacks):
			self.bottoms.append(0)

	def __repr__(self):
		res = ""
		for i in range(len(self.bottoms)):
			res += f"Stack {i+1} : "
			if i == len(self.bottoms) - 1:
				res += f"{self.arr[self.bottoms[i]:]}\n"
			else:
				res += f"{self.arr[self.bottoms[i]:self.bottoms[i+1]]}\n"			
		return res

	def insert(self, num_arr, value):
		'''	arguments : nth stack(num_arr) and value ''' 
		if num_arr < 1:
			return
		if num_arr == len(self.bottoms):
			self.arr.append(value)
			for num in range(num_arr, len(self.bottoms)):
				self.bottoms[num] += 1
		if num_arr < len(self.bottoms):
			self.arr.insert(self.bottoms[num_arr], value)
			for num in range(num_arr, len(self.bottoms)):
				self.bottoms[num] +=1

	def pop(self, num_arr):
		'''	arguments: nth stack(num_arr) ''' 
		if num_arr < 1:
			return
		if num_arr == len(self.bottoms):
			self.arr.pop()
		if num_arr < len(self.bottoms):
			self.arr.pop(self.bottoms[num_arr]-1)
			for num in range(num_arr, len(self.bottoms)):
				self.bottoms[num] -=1

	def size(self, num_arr):
		'''	arguments : nth stack(num_arr)''' 
		if num_arr < 1:
			return
		if num_arr == len(self.bottoms):
			return len(self.arr[self.bottoms[num_arr-1]:])
		if num_arr < len(self.bottoms):
			return len(self.arr[self.bottoms[num_arr-1]:self.bottoms[num_arr]])
def main():
	mults = Multistacks(3)
	mults.insert(1,2)
	mults.insert(1,6)
	mults.insert(1,5)
	mults.insert(2,3)
	mults.insert(2,3)
	mults.insert(2,3)
	mults.pop(1)
	print(mults)

if __name__ == '__main__':
	main()
