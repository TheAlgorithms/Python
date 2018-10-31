import heapq

my_list = [58, 41, 12, 17, 89, 65, 23, 20, 10, 16, 17, 19]
heapq.heapify(my_list)
print(my_list)

heapq.heappush(my_list, 7)
print(my_list)

print('Popped Element: ' + str(heapq.heappop(my_list)))
print(my_list)

new_iter = list()
new_iter = heapq.nlargest(4, my_list)
print(new_iter)
