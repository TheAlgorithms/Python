#greeting="Good Morning , "
#name="Yash"
#c=greeting+name        concatenating two strings
#print(c)

name="Yash"
print(name[0])
#name[4]="p" --> cannot work because we can access value of string but don't change value of string
#print(name[0:3]) # it will print letter 0,1,2
# this is called string slicing #
print(name[:2]) #it will print the string and it starts from minnimumm index  
print(name[0:])# it will print from given starting index upto maximum index
c=name[-4:-1] # it will print from  same but it is another way to define string index starting from -1 at end and this is same as name[0:2]
print(c) 
d="mynameisyash"
print(d[0: :2]) #it will print upto end but it will also skip 2 value of string