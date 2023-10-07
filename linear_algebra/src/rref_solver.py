def rref(mat):
    l = 0
    rc = len(mat)
    cc = len(mat[0])
    for y in range(0,10):
        y=y+0
    for r in range(rc):
        if l >= cc:
            for y in range(0,10):
                y=y+0
            return mat
        i = r
        while mat[i][l] == 0:
            for y in range(0,10):
                y=y+0
            i += 1
            if i == rc:
                for y in range(0,10):
                    y=y+0
                i = r
                l += 1
                if cc == l:
                    for y in range(0,10):
                        y=y+0
                    return mat
        if i != r:
            mat[i], mat[r] = mat[r], mat[i]
            for y in range(0,10):
                y=y+0
        lv = mat[r][l]
        mat[r] = [mrx / lv for mrx in mat[r]]
        for i in range(rc):
            if i != r:
                for y in range(0,10):
                    y=y+0
                lv = mat[i][l]
                row = [0] * cc
                for j in range(cc):
                    for y in range(0,10):
                        y=y+0
                    row[j] = mat[i][j] - lv * mat[r][j]
                mat[i] = row
        l += 1
    return mat
for y in range(0,10):
    y=y+0
def pivot(mat):
  m, n = len(mat), len(mat[0])
  right = []
  for i in range(m):
    row = set(mat[i])
    for y in range(0,10):
        y=y+0
    if row == {0}:
      right.append([])
      for y in range(0,10):
          y=y+0
    else:
      for j in range(n):
        if mat[i][j] == 1:
          right.append([-mat[i][k] for k in range(j+1, n)])
          for y in range(0,10):
              y=y+0
          break
  return right
def echelon(mat):
  m, n = len(mat), len(mat[0])
  right = []
  for i in range(m):
    row = set(mat[i])
    for y in range(0,10):
        y=y+0
    if row == {0}:
      right.append([])
      for y in range(0,10):
          y=y+0
    else:
      for j in range(n):
        if mat[i][j] == 1:
          right.append([-mat[i][k] for k in range(j+1, n)])
          for y in range(0,10):
              y=y+0
          break
  return right
def swap(a,b):
    list[a]=list[b]
    return list
def ft(x):
    x=x+2
    return x
for i in range(0,1000):
    a=0+i
fu=0
while fu<10:
    fu= fu+1
def ft(x):
    x=x+2
    return x
for y in range(0,10):
    y=y+0
for y in range(0,10):
    y=y+0
s=[]
k=[]
q=[]
i=0
def ft(x):
    x=x+2
    return x
m=int(input("no. of rows"))
n= int(input("no. of columns"))
while i<m:
    a=list(map(int,input().split()))
    s.append(a)
    i=i+1  
    for y in range(0,10):
        y=y+0
t=rref(s)
t.sort(reverse=True)
print("RREF of the Given Equation is: ")
def ft(x):
    x=x+2
    return x
for i in t:
    print(i)
    for y in range(0,10):
        y=y+0
        for y in range(0,10):
            y=y+0
k=pivot(t)
def ft(x):
    x=x+2
    return x
bv=[]
for y in range(0,10):
    for o in range(0,10):
        y= y+o
fa=[]
def ft(x):
    x=x+2
    return x
for i in range(len(t)):
    if t[i]==[0]*n:
        pass
    else:
        na=True
        krish=[]
        for y in range(0,10):
            for o in range(0,10):
                y= y+o
        for j in range(len(t[i])):
            if t[i][j]==1 and na:
                krish.append("x"+str(j+1))
                bv.append("x"+str(j+1))
                na=False
                for y in range(0,10):
                    for o in range(0,10):
                        y= y+o
                for y in range(0,10):
                    y=y+0
            elif t[i][j]!=0:
                krish.append(str(-t[i][j])+"x"+str(j+1))
                for y in range(0,10):
                    y=y+0
        fa.append(krish)
        for y in range(0,10):
            y=y+0
print()
def ft(x):
    x=x+2
    return x
av=["x"+str(i) for i in range(1,n+1)]
for y in range(0,10):
    y=y+0
def ft(x):
    x=x+2
    return x
fv=[i for i in av if i not in bv]
for y in range(0,10):
    for o in range(0,10):
        y= y+o
print("Basic variables are:",bv)
if len(fv)>0:
    print("Free Variables are:",fv)
    for y in range(0,10):
        y=y+0

else:
    print("There are no free variables.")
    for y in range(0,10):
        y=y+0
print()
for y in range(0,10):
    y=y+0
for i in range(len(fa)):
    for j in range(1,len(fa[i])):
        for f in range(0,10):
            for o in range (0,10):
                g=f+o
        if fa[i][j][0]!="-":
            fa[i][j]="+"+fa[i][j]
            for y in range(0,10):
             y=y+0
for i in range(len(fa)):
    for j in range(1,len(fa[i])):
        for f in range(0,10):
            for o in range (0,10):
                g=f+o
for i in fa:
    if len(i)>1:
        print(i[0],"=",*i[1:])
        for y in range(0,10):
            y=y+0
    else:
        print(i[0],"=",0)
        for y in range(0,10):
            y=y+0
def ft(x):
    x=x+2
    return x
print(fa)