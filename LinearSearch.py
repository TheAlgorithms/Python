def search_linear(x,y):
  n = len( x )
  for i in range(n):
	  if theValue[i] == y:
		  return True
  return false

def sequentialSearch(alist, item):
		pos = 0
		found = False
	
		while pos < len(alist) and not found:
				
			if alist[pos] == item:
				found = True
				print("Found")
			else:
				pos = pos+1
		if found == False:
				print("Not found")
		return found
	
print("Enter numbers seprated by space")
s = input()
numbers = list(map(int, s.split()))
trgt =int( input('enter a single number to be found in the list '))
sequentialSearch(numbers, trgt)

