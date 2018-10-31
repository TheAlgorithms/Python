import bisect

my_list = [11, 25, 36, 47, 56, 69, 69, 69, 78, 78, 91, 102, 120]
print('Correct Location to insert 53 is: ' + str(bisect.bisect(my_list, 53, 0, len(my_list))))

print('Correct right Location to insert 69 is: ' + str(bisect.bisect_right(my_list, 69, 0, len(my_list))))
print('Correct left Location to insert 69 is: ' + str(bisect.bisect_left(my_list, 69, 0, len(my_list))))

bisect.insort(my_list, 59, 0, len(my_list))
print(my_list)
bisect.insort_left(my_list, 78, 0, len(my_list))
print(my_list)
