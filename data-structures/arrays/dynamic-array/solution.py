# Well, this isn't quite an interesting challenge. Just
# follow what the problem requires us to do.

N, Q = map(int, input().split())
seqList, lastAns = [[] for i in range(N)], 0
for i in range(Q):
  op, x, y = map(int, input().split())
  seq = seqList[(x ^ lastAns) % N]
  if op == 1:
    seq.append(y)
  else:
    lastAns = seq[y % len(seq)]
    print(lastAns)
