
def sequential_search(alist, target):
	for index, item in enumerate(alist):
		if item == target:
			print("Found target {} at index {}".format(target, index))
			break
	else:
		print("Not found")


def main():
	try:
		print("Enter numbers separated by spaces")
		s = raw_input()
		inputs = list(map(int, s.split(' ')))
		target = int(raw_input('\nEnter a single number to be found in the list: '))
	except Exception as e:
		print(e)
	else:
		sequential_search(inputs, target)

if __name__ == '__main__':
	print('==== Insertion Sort ====\n')
	main()
