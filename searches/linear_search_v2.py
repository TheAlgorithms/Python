#!/bin/python3
import os 
import time as t
os.system("clear")
def lsearch(array:list, search_element:any)->None:
	print("\nMethod:linear search")
	print("You entered:  ",list(array),type(array))
	print("Search Element is:  ",search_element,type(search_element))
	print("Searching started ")
	print("Checking..")
	i = 0
	for i in range(len(array)):
		if array[i] == search_element:
			t.sleep(0.1)
			print("Element is Found at",  i,"th index and",  i+1,  "th position")
			t.sleep(0.1)
			print("Completed chacking. ")
			t.sleep(0.1)
			print("Searching ended")
			break
		else:
			pass
			if i==len(array) -1:
				print("Element not found ")
				print("Completed chacking.")
				print("Searching ended")
		i = i+1


l1 = lsearch([1,2,3,4,5,6,7],'tejas')
l2 = lsearch(['tejas','kunal','vignesh','datta','saif'],5)
l3 = lsearch(['appale',1,2,3,'mango'],'mango')
