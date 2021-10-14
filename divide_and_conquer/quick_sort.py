# Implementation of Quick sort algo-> https://en.wikipedia.org/wiki/Quicksort
class QuickSort():
   
    def __init__(self, array:list,asc:bool=True)->None:
        self.asc=asc
        self.array = array

    def partition(self, start:int, end:int)->int:  # Will sort in ascending order by default
        """ 
        >>> arr=[2,1,4,5,6,1]
        >>> q_s=QuickSort(arr)
        >>> q_s.partition(0,len(arr))
        2
        >>> arr=[2,3,4,5,6,9]
        >>> q_s=QuickSort(arr)
        >>> q_s.partition(0,len(arr))
        0
        """
        '''Normal partition routine read more about it here: google Lomuto partition algorithm. '''
        i = start
        j = start+1
        while(j < end):
            if(self.asc):
                if(self.array[j] < self.array[start]):
                    i += 1
                    self.array[j], self.array[i] = self.array[i], self.array[j]
                j += 1
            else:
                if(self.array[j] > self.array[start]):
                    i += 1
                    self.array[j], self.array[i] = self.array[i], self.array[j]
                j += 1
        self.array[start], self.array[i] = self.array[i], self.array[start]
        return i
    def sort(self,start:int,end:int)->None: #recursive implementation of quick sort
        """ 
        >>> arr=[2,1,4,5,6,1]
        >>> q_s=QuickSort(arr)
        >>> q_s.sort(0,len(arr))
        >>> print(arr)
        [1, 1, 2, 4, 5, 6]
        """
        if(start>=end):
            return
        i=self.partition(start,end)
        self.sort(start,i)
        self.sort(i+1,end)

if __name__=='__main__':
    import doctest

    doctest.testmod()
    ls = [3, 2, 1, 4, 3, 0, 5, 9,0,99,88,77,66,55,1]
    #sort in ascending order
    
