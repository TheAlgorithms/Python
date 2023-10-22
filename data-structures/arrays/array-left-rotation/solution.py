# We slice the array in two parts at index d, then print them
# in reverse order.

n, d = map(int, input().split())
A = list(map(int, input().split()))
print(*(A[d:] + A[:d])) 
