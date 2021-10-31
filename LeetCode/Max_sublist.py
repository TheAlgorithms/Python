L=list(map(int,input().split(',')))
# Brute Force: O(n3)
# ans=float('-inf')
# for i in range(len(L)):
#     for j in range(i,len(L)):
#         cur_sum=0
#         for k in range(i,j+1):
#             cur_sum=cur_sum+L[k]
#         if cur_sum>ans:
#             ans=cur_sum
# print(ans)
#----------------------------------------------------
### O(n2):
# ans=float('-inf')
# for i in range(len(L)):
#     cur_sum = 0
#     for j in range(i,len(L)):
#         cur_sum += L[j]
#         if cur_sum > ans:
#             ans=cur_sum
# print(ans)
#----------------------------------------------------
##Optimized Approach: Kadane's Algo || O(n)

max_sum=float('-inf')
cur_sum=0
for i in range(len(L)):
    cur_sum += L[i]
    if cur_sum > max_sum:
        max_sum = cur_sum
    if cur_sum < 0: # If the sum becomes negetive, then we discard that sum, and start a new summation of further elements.However the prvious max_sum is being tracked in max_sum var
        cur_sum = 0
print(max_sum)
