

def simple_bubble_sort(int_list):
	count = len(int_list)
	swapped = True
	while (swapped):
		swapped = False
		for j in range(count - 1):
			if (int_list[j] > int_list[j + 1]):
				int_list[j], int_list[j + 1] = int_list[j + 1], int_list[j]
				swapped = True
	return int_list


def main(num):
	inputs = []
	print("Enter any {} numbers for unsorted list: ".format(num))
	try:
		for i in range(num):
			n = input()
			inputs.append(n)
	except Exception as e:
		print(e)
	else:
		sorted_input = simple_bubble_sort(inputs)
		print('\nSorted list (min to max): {}'.format(sorted_input))

if __name__ == '__main__':
	print('==== Bubble Sort ====\n')
	list_count = 6
	main(list_count)
