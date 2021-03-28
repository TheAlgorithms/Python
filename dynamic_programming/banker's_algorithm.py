# The Banker algorithm, sometimes referred to as the detection algorithm, is a resource allocation and deadlock avoidance 
# algorithm developed by Edsger Dijkstra that tests for safety by simulating the allocation of predetermined maximum possible 
# amounts of all resources, and then makes an "s-state" check to test for possible deadlock conditions for all other pending 
# activities, before deciding whether allocation should be allowed to continue.

# https://en.wikipedia.org/wiki/Banker's_algorithm




process = [] # Table of process names
allocation = [] # Table of each process current allocated resources
maxx = [] # Table of each process Max allocations to complete task
available = [] # table of available resources


# Set prcoess function
# ProcessName Param : String Parameter to define process name (P1 , Process1 ...)
# Allocation Param : List of currently allocated resources to the process
# Need Param : List of how many resources the process totally needs to complete the task
def set_process(ProcessName, Allocation, Need):
    process.append(ProcessName)
    allocation.append(Allocation)
    maxx.append(Need)
  
# set available resources
# available Param : List of current available resources that are not used by any process
def set_available_resources(available):
    available.append(available)
    
    
# setting example of process with their currently allocated resources for 3 resources and how much they from these 3 resources to complete the task
set_process("P1", [0, 1, 0] , [7, 5, 3])
set_process("P2", [2, 0, 0] , [3, 2, 2])
set_process("P3", [3, 0, 2] , [9, 0, 2])
set_process("P4", [2, 1, 1] , [2, 2, 2])
set_process("P5", [0, 0, 2] , [4, 3, 3])

# available resources from 3 instances
set_available_resources([3, 3, 2])


# Creation of need matrix
need = [[ 0 for i in range(len(allocation[0]))]for i in range(len(allocation))]
for counter in range (len(allocation)):
    for counter1 in range (len(allocation[counter])):
        need[counter][counter1] = maxx[counter][counter1] - allocation[counter][counter1]
        
        
        
# Here, we compare each process needs to the currently available resources to check if its possible to create a safe
# Sequence for our 5 defined processes (P1..P5).
i=0
j=0
while(i < len(available[0]) and len(need) > 0):
    while(available[0][i] - need[j][i] <  0):
        if(j > len(need)):
            print("There is a deadlock in the system")
        j+= 1
            
    i+=1
    if(i == (len(available[0]) -1)):
        print(process[j], "-->")
        process.pop(j)
        for k in range (len(available[0])):
            available[0][k] += allocation[j][k]
        allocation.pop(j)
        need.pop(j)
        i = 0
        j =0
        
# P2 -->
# P4 -->
# P1 -->
# P3 -->
# P5 -->
# This is a safe sequence.
