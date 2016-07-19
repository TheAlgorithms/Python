array=[];

# input
print ("Enter any 6 Numbers for Unsorted Array : ");
for i in range(0, 6):
	n=input();
	array.append(int(n));

# Sorting
print("")
for i in range(1, 6):
	temp=array[i]
	j=i-1;
	while(j>=0 and temp<array[j]):
		array[j+1]=array[j];
		j-=1;
	array[j+1]=temp;

# Output
for i in range(0,6):
	print(array[i]);




