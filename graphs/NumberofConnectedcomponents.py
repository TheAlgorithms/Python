d = {1:[2,3],2:[3],3:[],4:[]}


'''d = {}
for i in range(1,n+1):                      //if d is not given and connection between points is given
    d[i]=[]
for i in range(m):
    u,v = map(int,input().split())
    d[u].append(v) '''

l = set()
q = 0
o = len(l)
for key in d:
    l.add(key)
    for j in range(len(d[key])):
        l.add((d[key])[j])
    p = len(l)
    if(p-o==1+len(d[key])):
        q+=1
        o = len(l)
print(q)
