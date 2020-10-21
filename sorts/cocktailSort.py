def cocktailSort(a):
   n = len(a)
   flag = True
   start = 0
   end = n-1
   while (flag==True):
      flag = False
      
      for i in range (start, end):
         if (a[i] > a[i+1]) :
            a[i], a[i+1]= a[i+1], a[i]
            flag=True
            
      if (flag==False):
         break
         
      flag = False
      
      end = end-1
      
      for i in range(end-1, start-1,-1):
         if (a[i] > a[i+1]):
            a[i], a[i+1] = a[i+1], a[i]
            flag = True
      
      start = start+1
