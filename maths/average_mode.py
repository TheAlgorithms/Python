def mode(inputlist):
	countlist = []
	checklist = inputlist.copy()
	result = list()
	for x in inputlist:
		result.append(inputlist.count(x))
		inputlist.remove(x)
		y=max(result)
		return checklist[result.index(y)]
data=[1,2,3,4,5,1,1,1,1,1]
print(mode(data))