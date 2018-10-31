import copy
my_mat = [[11,22,33],[44,55,66],[11,22,33]]
print('Matrix Before Updation: ' + str(my_mat))

new_mat = copy.copy(my_mat) #Make a shallow copy and update on copied object
new_mat[2][0] = 77
new_mat[2][1] = 88
new_mat[2][2] = 99
print('Matrix After Updation: ' + str(my_mat)) #Original Matrix Updated

my_mat = [[11,22,33],[44,55,66],[11,22,33]]

new_mat_deep = copy.deepcopy(new_mat)
print('\nMatrix Before Updation: ' + str(my_mat))

new_mat_deep[2][0] = 77
new_mat_deep[2][1] = 88
new_mat_deep[2][2] = 99

print('Matrix After Updation: ' + str(my_mat)) # Original Matrix unchanged
print('New Matrix: ' + str(new_mat_deep)) # Original Matrix unchanged
