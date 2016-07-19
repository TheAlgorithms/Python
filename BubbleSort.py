

array=[];

# input
print ("Enter any 6 Numbers for Unsorted Array : ");
for i in range(0, 6):
	n=input();
	array.append(int(n));

# Sorting
print("")
for i in range(0, 6):
	for j in range(0,5):
		if (array[j]>array[j+1]):
			temp=array[j];
			array[j]=array[j+1];
			array[j+1]=temp;

# Output
for i in range(0,6):
	print(array[i]);




