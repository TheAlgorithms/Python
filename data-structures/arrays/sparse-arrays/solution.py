# We put everything in a collections.Counter, and let it do
# its work.

import collections
N = int(input())
counter = collections.Counter(input() for i in range(N))
for i in range(int(input())):
  print(counter[input()]) 
