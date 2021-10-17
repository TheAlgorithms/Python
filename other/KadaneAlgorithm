import sys
max,curr,neg=0,0,-sys.maxsize-1
arr=[-1,-2,-3,-4]
for i in range(len(arr)):
     curr += arr[i]
     if curr > max:
          max = curr
     elif curr < 0:
          curr = 0
     if(neg<arr[i]):
          neg=arr[i]
        
if(neg>0):
    print(max);
else:
    print(neg);
