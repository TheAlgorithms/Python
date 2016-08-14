
from  __future__ import print_function


def heapify(unsorted,index,heap_size):
	largest = index
	left_index = 2*index + 1
	right_index = 2*index + 2
	if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
		largest = left_index
	
	if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
		largest =  right_index

	if largest != index:
		unsorted[largest],unsorted[index] = unsorted[index],unsorted[largest]
		heapify(unsorted,largest,heap_size)		
		
def heap_sort(unsorted):	
	n=len(unsorted) 
	for i in range (n/2 - 1 , -1, -1) :
		heapify(unsorted,i,n)
	for i in range(n - 1,  -1, -1):
		unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
		heapify(unsorted,0,i)
	return unsorted


if __name__ == '__main__':
    import sys
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function('Enter numbers separated by coma:\n')
    unsorted = [int(item) for item in user_input.split(',')]
    print (heap_sort(unsorted))

