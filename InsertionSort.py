
def simple_insertion_sort(int_list):
	count = len(int_list)
	for i in range(1, count):
		temp = int_list[i]
		j = i - 1
		while(j >= 0 and temp < int_list[j]):
			int_list[j + 1] = int_list[j]
			j -= 1
		int_list[j + 1] = temp

	return int_list


def main():
	try:
		print("Enter numbers separated by spaces:")
		s = raw_input()
		inputs = list(map(int, s.split(' ')))
		if len(inputs) < 2:
			print('No Enough values to sort!')
			raise Exception

	except Exception as e:
		print(e)
	else:
		sorted_input = simple_insertion_sort(inputs)
		print('\nSorted list (min to max): {}'.format(sorted_input))

if __name__ == '__main__':
	print('==== Insertion Sort ====\n')
	main()
