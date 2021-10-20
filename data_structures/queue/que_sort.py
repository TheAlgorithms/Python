import queue  
q = queue.Queue()  
  
q.put(14)  
q.put(27)  
q.put(11)  
q.put(4)  
q.put(1)  
  
  
n =  q.qsize()  
for i in range(n):  
    a = q.get()  
    for j in range(n-1):  
        b = q.get()  
        if a > b :  
            q.put(b)  
        else:  
            q.put(a)  
            a = b    
    q.put(a)  
  
while (q.empty() == False):   
    print(q.queue[0], end = " ")    
    q.get()  
