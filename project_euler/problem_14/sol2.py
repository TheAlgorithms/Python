def collatz_sequence(n):
  """Collatz conjecture: start with any positive integer n.Next termis obtained from the previous term as follows:
  if the previous term is even, the next term is one half the previous term.
  If the previous term is odd, the next term is 3 times the previous term plus 1.
  The conjecture states the sequence will always reach 1 regaardess of starting n."""
  sequence = [n]
  while n != 1:
    if n % 2 == 0:# even
      n //= 2
    else:
      n = 3*n +1
    sequence.append(n)
  return sequence

answer = max([(len(collatz_sequence(i)), i)  for i in range(1,1000000)])
print("Longest Collatz sequence under one million is %d with length %d" % (answer[1],answer[0]))