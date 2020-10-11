from scipy.stats import pearsonr 
  

list1 = list(map(int,input("\nEnter the numbers in first list: ").strip().split()))
list2 = list(map(int,input("\nEnter the numbers in second list : ").strip().split())) 

  
# Apply the pearsonr() 
corr, _ = pearsonr(list1, list2) 
print('Pearsons correlation: %.3f' % corr) 
  
  
