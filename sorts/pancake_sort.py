from random import randint

def pancake_sort(cakes):
  if not cakes or len(cakes) == 1:
        return cakes
  cake_index = 0
  while cake_index < len(cakes)-1:
    prev_cake_size, current_cake_size = cakes[cake_index], cakes[cake_index+1]
    if prev_cake_size > current_cake_size:
      '''move the highest element to the beginning by reversing
      the cakes from 0 to highest element(including) and then move
      the highest element to the end by reversing the subarray'''
      cakes[0:cake_index+2] = (cakes[0:cake_index+1][::-1] + [cakes[cake_index+1]])[::-1]
      cake_index = 0
      continue
    cake_index += 1
  return cakes

for i in range(randint(0, 5)):
  data = [randint(0, 100) for _ in range(randint(0, 40))]
  if pancake_sort(data[:]) != sorted(data[:]):
    print("failed for", data[:])
