def pascals(limit:int,times:int = 0,number:list = ["1"])->None:
	"""
	A function to print Pascals Triangle pattern upto given limit.Only limit is required other arguements are for controlling the loop
	>>> pascals(5)
	1
	1 1
	1 2 1
	1 3 3 1
	1 4 6 4 1
	>>> pascals(4)
	1
	1 1
	1 2 1
	1 3 3 1
        >>> pascals(10)
	1
	1 1
	1 2 1
	1 3 3 1
	1 4 6 4 1
	1 5 10 10 5 1
	1 6 15 20 15 6 1
	1 7 21 35 35 21 7 1
	1 8 28 56 70 56 28 8 1
	1 9 36 84 126 126 84 36 9 1
        """
	print(" ".join(number))
	if (times <= int(limit)-2):
		newnumlis = ["1"]
		for i in range(len(number)-1):
			newnum = int(number[i]) + int(number[i+1])
			newnumlis.append(str(newnum))
		newnumlis.append("1")
		times += 1
		pascals(limit,times,newnumlis)
if __name__ == "__main__":
	inpu = str(input("Enter a Limit:"))
	pascals(inpu)	
