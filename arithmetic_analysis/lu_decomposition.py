import numpy

def LUDecompose (table):
    #table that contains our data
    #table has to be a square array so we need to check first
    rows,columns=numpy.shape(table)
    L=numpy.zeros((rows,columns))
    U=numpy.zeros((rows,columns))
    if rows!=columns:
        return
    for i in range (columns):
        for j in range(i-1):
            sum=0
            for k in range (j-1):
                sum+=L[i][k]*U[k][j]
            L[i][j]=(table[i][j]-sum)/U[j][j]
        L[i][i]=1
        for j in range(i-1,columns):
            sum1=0
            for k in range(i-1):
                sum1+=L[i][k]*U[k][j]
            U[i][j]=table[i][j]-sum1
    return L,U







matrix =numpy.array([[2,-2,1],[0,1,2],[5,3,1]])
L,U = LUDecompose(matrix)
print(L)
print(U)
