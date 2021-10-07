# initializing string
test_str = 'geeksforgeeks'
  
# printing original string
print("The original string is : " + str(test_str))
  
# computing half index
hlf_idx = len(test_str) // 2
  
res = ''
for idx in range(len(test_str)):
      
    # uppercasing later half
    if idx >= hlf_idx:
      res += test_str[idx].upper()
    else :
      res += test_str[idx]
          
# printing result 
print("The resultant string : " + str(res)) 
