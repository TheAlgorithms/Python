# creating a tuple using ()
t=(1,2,4,7,9)

#t1=() it is an empty tuple
#t1=(1)#wrong way to declare a tuple with single element
t1=(1,3)# tuple with single element 
print(t1)
#print the elments of tuple
print(t[0])
t[0]=34
print(t) # this line will show error because in list value can be change but in tuple value cannot be change 
# so we can say tuple is immutable means cannot change 