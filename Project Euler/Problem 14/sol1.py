largest_number = 0
pre_counter = 0

for input1 in range(750000,1000000):
    counter = 1
    number = input1

    while number > 1:
        if number % 2 == 0:
            number /=2
            counter += 1
        else:
            number = (3*number)+1
            counter += 1

    if counter > pre_counter:
        largest_number = input1
        pre_counter = counter

print('Largest Number:',largest_number,'->',pre_counter,'digits')
