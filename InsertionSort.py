
def simple_insertion_sort(int_list):
	for i in range(1, 6):
		temp = int_list[i]
		j = i - 1
		while(j >= 0 and temp < int_list[j]):
			int_list[j + 1] = int_list[j]
			j -= 1
		int_list[j + 1] = temp

	return int_list


def main(num):
	inputs = []
	print('Enter any {} numbers for unsorted list: '.format(num))
	try:
		for i in range(num):
			n = input()
			inputs.append(n)
	except Exception as e:
		print(e)
	else:
		sorted_input = simple_insertion_sort(inputs)
		print('\nSorted list (min to max): {}'.format(sorted_input))

if __name__ == '__main__':
	print('==== Insertion Sort ====\n')
	list_count = 6
	main(list_count)
