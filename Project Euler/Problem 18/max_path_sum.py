f=open('triangle.txt','r')
previous=list(map(int,f.readline().strip().split()))
while True:
    current=list(map(int,f.readline().strip().split()))
    if len(current)==0:
        break
    current[0]+=previous[0]
    current[-1]+=previous[-1]
    for i in range(1,len(current)-1):
        current[i]+=max(previous[i],previous[i-1])
    previous=current.copy()
print(max(previous))
f.close()