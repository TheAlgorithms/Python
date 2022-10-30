 #Python program to demonstrate
# Adding Elements to a Array
 
# importing "array" for array creations
import array as arr
 
# array with int type
a = arr.array('i', [1, 2, 3])
 
 
print ("Array before insertion : ", end =" ")
for i in range (0, 3):
    print (a[i], end =" ")
print()
 
# inserting array using
# insert() function
a.insert(1, 4)
 
print ("Array after insertion : ", end =" ")
for i in (a):
    print (i, end =" ")
print()
 
# array with float type
b = arr.array('d', [2.5, 3.2, 3.3])
 
print ("Array before insertion : ", end =" ")
for i in range (0, 3):
    print (b[i], end =" ")
print()
 
# adding an element using append()
b.append(4.4)
 
print ("Array after insertion : ", end =" ")
for i in (b):
    print (i, end =" ")
print()