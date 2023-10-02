# with the help of with statement we can automatically close and open file we don't need to write fclose for closing file 
with open('another.txt','r') as f:
    a=f.read() 

with open('another.txt','w') as f:
    a=f.write("yash") 
print(a)