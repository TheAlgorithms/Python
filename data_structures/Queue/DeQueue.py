from __future__ import print_function
# Python code to demonstrate working of 
# extend(), extendleft(), rotate(), reverse()
 
# importing "collections" for deque operations
import collections
 
# initializing deque
de = collections.deque([1, 2, 3,])
 
# using extend() to add numbers to right end 
# adds 4,5,6 to right end
de.extend([4,5,6])
 
# printing modified deque
print ("The deque after extending deque at end is : ")
print (de)
 
# using extendleft() to add numbers to left end 
# adds 7,8,9 to right end
de.extendleft([7,8,9])
 
# printing modified deque
print ("The deque after extending deque at beginning is : ")
print (de)
 
# using rotate() to rotate the deque
# rotates by 3 to left
de.rotate(-3)
 
# printing modified deque
print ("The deque after rotating deque is : ")
print (de)
 
# using reverse() to reverse the deque
de.reverse()
 
# printing modified deque
print ("The deque after reversing deque is : ")
print (de)
