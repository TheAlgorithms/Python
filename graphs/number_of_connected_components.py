graph = {1:[2,3],2:[3],3:[],4:[]}


'''d = {}
for i in range(1,n+1):                      //if d is not given and connection between points is given
    d[i]=[]
for i in range(m):
    u,v = map(int,input().split())
    d[u].append(v) '''

l = set()
connected_comp = 0
o = len(l)
for key in d:
    l.add(key)
    for j in range(len(graph[key])):
        l.add((graph[key])[j])
    p = len(l)
    if(p-o==1+len(grah[key])):
        connected_comp+=1
        o = len(l)
print(connected_comp)
