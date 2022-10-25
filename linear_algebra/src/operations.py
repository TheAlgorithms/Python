# A class to represent a disjoint set
class DisjointSet:
	parent = {}

	# Find the root of the set in which element `k` belongs
	def Find(self, k):
		# if `k` is root
		if self.parent[k] == k:
			return k
		# recur for the parent until we find the root
		return self.Find(self.parent[k])

	# perform MakeSet operation
	def makeSet(self, universe):
		for i in universe:
		# create `n` disjoint sets (one for each item)
			self.parent[i] = i

	# Perform Union of two subsets
	def Union(self, p, q):
		# find the root of the sets in which elements
		# `x` and `y` belongs
		x = self.Find(p)
		y = self.Find(q)

		self.parent[x] = y


def printSets(universe, ds):
	print([ds.Find(i) for i in universe])


# Disjoint–Set data structure (Union–Find algorithm)
if __name__ == '__main__':

	# group of items
	universe = [1, 2, 3, 4, 5]

	# initialize disjoint set
	ds = DisjointSet()

	# create a singleton set for each element of the universe
	ds.makeSet(universe)
	printSets(universe, ds)

	ds.Union(4, 3) # 4 and 3 are in the same set
	printSets(universe, ds)

	ds.Union(2, 1) # 1 and 2 are in the same set
	printSets(universe, ds)

	ds.Union(1, 3) # 1, 2, 3, 4 are in the same set
	printSets(universe, ds)
