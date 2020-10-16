er_none
edit
play_arrow

brightness_4
# A naive recursive implementation that 
# simply follows the above optimal  
# substructure property  
import sys 
  
# Matrix A[i] has dimension p[i-1] x p[i] 
# for i = 1..n 
def MatrixChainOrder(p, i, j): 
  
    if i == j: 
        return 0
  
    _min = sys.maxsize 
      
    # place parenthesis at different places  
    # between first and last matrix,  
    # recursively calculate count of 
    # multiplications for each parenthesis 
    # placement and return the minimum count 
    for k in range(i, j): 
      
        count = (MatrixChainOrder(p, i, k)  
             + MatrixChainOrder(p, k + 1, j) 
                   + p[i-1] * p[k] * p[j]) 
  
        if count < _min: 
            _min = count; 
      
  
    # Return minimum count 
    return _min; 
  
  
# Driver program to test above function 
arr = [1, 2, 3, 4, 3]; 
n = len(arr); 
  
print("Minimum number of multiplications is ", 
                MatrixChainOrder(arr, 1, n-1)); 
