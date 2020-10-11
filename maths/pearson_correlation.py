import sys
from scipy.stats import pearsonr 
  

list1 = [1,2,4,7,8]
list2 = [3,7,8,7,90]
  
# Apply the pearsonr() 
corr, _ = pearsonr(list1, list2) 
print('Pearsons correlation: %.3f' % corr) 
  
  
