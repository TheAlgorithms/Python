"""This is a python program that calculates the rank of a matrix"""
""" BY - RUDRANSH BHARDWAJ"""
def swapRows(a,row1,row2):
	a[row2],a[row1]=a[row1],a[row2]
	return a

def Row_Transformation(a,x,row1,row2):
	for i in range(len(a[row2])):
                a[row2][i]+=a[row1][i]*x
	return a

def MatrixRank(a):

	ncol=len(a[0])
	nrow=len(a)
	rank=min(ncol,nrow)

	if nrow>ncol:
		b=[]
		for m in range(ncol):
			l=[]
			for n in range(nrow):
				l.append(a[n][m])
			b.append(l)
		a=b
		ncol,nrow=nrow,ncol

	for r in range(rank):
		if a[r][r]!=0:
			for j in range(r+1,nrow):
				a=Row_Transformation(a,-(a[j][r]//a[r][r]),r,j)
		else:
			count1=True
			for k in range(r+1,nrow):
				if a[k][r]!=0:
					a=swapRows(a,r,k)
					count1=False
					break

			if count1:
				for i in range(nrow):
					a[i][r],a[i][rank-1]=a[i][rank-1],a[i][r]
			nrow-=1


		count2=0
		for i in a:
			if i==[0]*ncol:
				count2+=1

		return (rank-count2)
