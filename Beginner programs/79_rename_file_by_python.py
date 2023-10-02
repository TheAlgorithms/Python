import os # module for rename a file
oldname="sample2.txt"
newname="rename by python.txt"
with open(oldname) as f:
    content=f.read()

with open(newname,"w") as f:
    f.write(content)

os.remove(oldname)