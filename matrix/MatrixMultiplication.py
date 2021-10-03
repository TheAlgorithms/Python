l = []
print("Enter values for matrix - A")
row1 = int(input("Number of rows, m = "))
col1 = int(input("Number of columns, n = "))
for i in range(row1):
	a = []
	for j in range(col1):
		print("Entry in row:",i+1,"column:",j+1)
		x = int(input())
		a.append(x)
	l.append(a)
print("Enter values for matrix - B")
p = []
row2 = int(input("Number of rows, m = "))
col2 = int(input("Number of columns, n = "))
for k in range(row2):
	b = []
	for t in range(col2):
		print("Entry in row:", k+1,"column:", t+1)
		z = int(input())
		b.append(z)
	p.append(b)
	
ans = []
for k in range(row1):
	l1 = []
	for i in range(col2):
		s = 0
		for j in range(col1):
			s += l[k][j]*p[j][i]
		l1.append(s)
	ans.append(l1)
	
print("Matrix - A =", l)
print("Matrix - B =", p)
print("Matrix - A * Matrix- B =", ans)
