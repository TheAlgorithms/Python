file1="this.txt"
file2="copy.txt"

with open("this.txt") as f:
    f1=f.read()

with open("copy.txt") as f:
    f2=f.read()

if (f1==f2):
    print("Files are identical")
else:
    print("Files are not identical")