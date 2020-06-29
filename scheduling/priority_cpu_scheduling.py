# Priority Scheduling algorithm implementation using python
# Priority Scheduling is one of the most common scheduling algorithm in batch systems
def findWaitingTime(processes, n, wt):  
    wt[0] = 0  
    for i in range(1, n):  
        wt[i] = processes[i - 1][1] + wt[i - 1]    
def findTurnAroundTime(processes, n, wt, tat):   
    for i in range(n): 
        tat[i] = processes[i][1] + wt[i]  
    
def findavgTime(processes, n):  
    wt = [0] * n 
    tat = [0] * n    
    findWaitingTime(processes, n, wt)    
    findTurnAroundTime(processes, n, wt, tat)  
    
    print("\nProcesses    Burst Time    Waiting Time    Turn-Around Time") 
    total_wt = 0
    total_tat = 0
    for i in range(n): 
  
        total_wt = total_wt + wt[i]  
        total_tat = total_tat + tat[i]  
        print(" ", processes[i][0], "\t\t", processes[i][1], "\t\t", wt[i], "\t\t", tat[i]) 
  
    print("\nAverage waiting time = %.5f "%(total_wt /n)) 
    print("Average turn around time = ", total_tat / n)  
  
def priorityScheduling(proc, n): 
        
    proc = sorted(proc, key = lambda proc:proc[2], reverse = True);  
  
    print("Order in which processes gets executed") 
    for i in proc: 
        print(i[0], end = " ") 
    findavgTime(proc, n)  
      
  
if __name__ =="__main__": 
       
    proc = [[1, 10, 1],  [2, 5, 0], [3, 8, 1]] 
    n = 3
    priorityScheduling(proc, n) 
