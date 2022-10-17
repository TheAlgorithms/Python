nums = [7,1,6,0] 
k=7 
curr=0 
res=0 
prefix={0:1} 
for n in nums: 
    curr+=n 
    diff=curr-k 
    if diff not in prefix: 
        res+=0 
    else: 
        res+=prefix[diff]  
    if curr not in prefix: 
        prefix[curr]=1 
    else: 
        prefix[curr]+=1  
print(res)
