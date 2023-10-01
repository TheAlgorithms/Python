# This is one of the searching algorithms that involves sequentially going through every element in the list until the element is located and its position is enumerated. This method might take a long time to run if the list or array is quite long and the element being searched is deep in the array. This is the disadvantage of this method. However, this method is quite handy as it can search in an unsorted list. 

#Linear search method.
def linear_search(values, searched):
   #The function takes in only two parameters.
   #'Searched' is the element being looked for.
   #'Values' is the list in which the element is searched.
   for i in range(0, len(values)):
       #We iterate over every element in the list.
       if (values[i] == searched):
           #If we find the element, we return the position of the element in the list.
           return "Element " + str(searched) + " is at " + str(i+1)
   #If we don't find the element, we return an 'absent statement'
   return "Element has not been found"

# by: Max Muller