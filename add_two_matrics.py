X = [[1,2,3],  
       [4,5,6],  
       [7,8,9]]  
  
Y = [[10,11,12],  
       [13,14,15],  
       [16,17,18]]  
  
Result = [[0,0,0],  
                [0,0,0],  
                [0,0,0]]  
# iterate through rows  
for i in range(len(X)):  
   # iterate through columns  
   for j in range(len(X[0])):  
       result[i][j] = X[i][j] + Y[i][j]  
for r in result:  
   print(r)  
