** Program to find maximum occuring character in a string **



str=input("Please enter a String")
d={}
c={}
for i in str:
    if i in c:
        c[i]+= 1
    else:
        c[i]=1
    d.update({i:c[i]})
occ=max(d.values())
str= max(d,key = d.get)
print(s,occ)
