# create an empty set 
a=set()
print(type(a))

# adding values in set
a.add(4)
a.add(5)
a.add(5) # it will not add multiple values it only add single value
a.add(5)

# accessing elements
 #  a.add([1,2,3]) #list cannot add
 # a.add({1,2,3}) dictionary cannot be added
a.add((1,2,3)) # tuple can be add
print(a)

#length of set
print(len(a)) # prints the length of this set

# removal of an item
a.remove(5)# it will remove from set
print(a)
# a.remove(6) -------- it will show error while trying to remove 6 while it is not in set

print(a.pop())