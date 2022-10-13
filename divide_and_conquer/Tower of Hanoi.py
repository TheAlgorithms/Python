# Recursive Python function to solve the tower of hanoi.
#Tower of Hanoi is a mathematical puzzle where we have three rods and n disks

def TowerOfHanoi(n , source, destination, auxiliary):
if n==1:
print ("Move disk 1 from source",source,"to destination",destination)
return

TowerOfHanoi(n-1, source, auxiliary, destination)
print ("Move disk",n,"from source",source,"to destination",destination)
TowerOfHanoi(n-1, auxiliary, destination, source)
		
# Driver code

n = 6

TowerOfHanoi(n,'A','B','C')



