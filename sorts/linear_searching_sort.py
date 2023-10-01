def linear_search(values, searched):
   
   for i in range(0, len(values)):
       
       if (values[i] == searched):
           
           return "Element " + str(searched) + " is at " + str(i+1)
   
   return "Element has not been found"