# use the open function to read the content of a file
#f=open('sample.txt','r')
f=open('sample.txt') # it will have by default mode read
#data=f.read() it will read full content of file
data=f.read(10) # it will read only 10 letters of file
print(data)
f.close()