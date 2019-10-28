def max(l):
    m=l[0]
    for i in l[1:]:
        if i>m:
            m=i
    return m
a=[1,2,3,4,22]
s=max(a)
print("max of the given list is",s)
