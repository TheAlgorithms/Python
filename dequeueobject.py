import collections as col
my_deque = col.deque('124dfre')
print(my_deque)

print("Popped Item: " + str(my_deque.pop()))
print("Popped Item From Left: " + str(my_deque.popleft()))
print(my_deque)
