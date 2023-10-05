from heapq import heappush, heappop  # to import heappop and heappush

l = input().split(" ")
k = int(input())
for i in range(len(l)):
    l[i] = int(l[i])
minheap = []
count = 0
for i in l:
    heappush(minheap, i)
    count += 1
    if count > k:
        heappop(minheap)
        count -= 1
print(minheap[0])
