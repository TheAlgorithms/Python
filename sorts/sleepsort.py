from time import sleep

import thread

items = []
n = int(input())
for i in range(0,n):
  a = int(input())
  items.append(a)
def sleep_sort(i):
        sleep(i)
        print i
[thread.start_new_thread(sleep_sort, (i,)) for i in items]
