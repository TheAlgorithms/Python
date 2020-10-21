def pureCocktailSort(a):
   
   length = len(a)
   semaphore = True
   
   start = 0
   end = length-1
   
   while (semaphore == True):
      
      semaphore = False
      
      for i in range (start, end):
         if (a[i] > a[i+1]) :
            a[i], a[i+1]= a[i+1], a[i]
            semaphore=True
            
      if (semaphore == False):
         break
         
      semaphore = False
      
      end = end-1
      
      for i in range(end-1, start-1,-1):
      
         if (a[i] > a[i+1]):
            a[i], a[i+1] = a[i+1], a[i]
            semaphore = True
      
      start = start+1
