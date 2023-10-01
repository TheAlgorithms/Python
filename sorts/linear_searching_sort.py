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