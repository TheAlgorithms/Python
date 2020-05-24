import doctest

"""
     This Function Implements Merge Sorting on the array passed as an parameter.
     Merge Sort is a sorting algorithm, which is commonly used in computer science.
     Merge Sort is a divide and conquer algorithm.
     It works by recursively breaking down a problem into two or more sub-problems of the same or related type,
     until these become simple enough to be solved directly.
     The solutions to the sub-problems are then combined to give a solution to the original problem.
     So Merge Sort first divides the array into equal halves and then combines them in a sorted manner.
    """ 

def mergeSort(array):
    """
        >>> mergeSort([9,7,5,3,1,1,2,4,6,8])
        [1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> mergeSort([9,8,7,6,5])
        [5, 6, 7, 8, 9]
    """
    if len(array) >1:
        middle_index = len(array)//2 						  #Finding the middle_index of the array
        left_index = array[:middle_index] 					  # Dividing the array elements 
        right_index = array[middle_index:]	 	 	 		  # into 2 halves - Left_index & Right Index. 

        mergeSort(left_index)                                                     # Sorting the first half of the array. 
        mergeSort(right_index)                                                    # Sorting the second half of the array.

        i = j = k = 0
		
        while i < len(left_index) and j < len(right_index):                       # Copy data to temporary array. 
            if left_index[i] < right_index[j]: 
                array[k] = left_index[i] 
                i+=1
            else: 
                array[k] = right_index[j] 
                j+=1
            k+=1
		 
        while i < len(left_index): 					          # Checking if any element was left
            array[k] = left_index[i] 
            i+=1
            k+=1
		
        while j < len(right_index):
            array[k] = right_index[j] 
            j+=1
            k+=1
    return array

if __name__ == "__main__":
    doctest.testmod()
