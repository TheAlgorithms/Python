class Process:
    def __init__(self, pid, bt, p):
        self.pid = pid
        self.burst_time = bt
        self.priority = p
        self.remaining_time = bt
        self.waiting_time=0
        self.turnaround_time=0


timer = 20
current_time=0
current_queue = 0
time_Quantem=5

total_waiting_time_for_Roundrobin=0
total_turnAround_time_for_Roundrobin=0
total_waiting_time_for_SJF1=0
total_waiting_time_for_SJF2=0
total_turnAround_time_for_SJF1=0
total_turnAround_time_for_SJF2=0
total_waiting_time_for_FCFS=0
total_turnAround_time_for_FCFS=0

q=[[],[],[],[]]
n0=0
n1=0
n2=0
n3=0
n = int(input("Enter the number of processes: "))
print("Enter the priority, burst time for each process: \n------------------------------------------------------\n")
for i in range(n):
    print("Enter details of process " + str(i+1))
    print("Enter burstTime : ");
    burstTime=int(input())
    print("Enter priority : ");
    priority = int(input())
    print("\n")
    if priority == 0:
        q[0].append(Process((i+1),burstTime, priority))
        n0+=1
    if priority == 1:
        q[1].append(Process((i+1), burstTime, priority))
        n1+=1
    if priority == 2:
        q[2].append(Process((i+1), burstTime, priority))
        n2+=1
    if priority == 3:
        q[3].append(Process((i+1), burstTime, priority))
        n3+=1
q[1].sort(key = lambda process: process.burst_time)
q[2].sort(key = lambda process: process.burst_time)


def dequeueRoundRobin():
    global timer
    global current_time
    global  total_turnAround_time_for_Roundrobin
    global total_waiting_time_for_Roundrobin
    if timer >= time_Quantem:
        p = q[0][0]
        print("Process id : "+str(p.pid)+" takes CPU to execute now at "+str(current_time))
        if p.remaining_time > time_Quantem:
            timer -= time_Quantem
            p.remaining_time -= time_Quantem
            current_time+=time_Quantem
            if timer == time_Quantem:
                print("The process with process id " + str(p.pid) + " completed successfully at "+str(current_time))
                p.turnaround_time=current_time
                total_turnAround_time_for_Roundrobin+=p.turnaround_time
                p.waiting_time=p.turnaround_time-p.burst_time
                total_waiting_time_for_Roundrobin+=p.waiting_time
                print("turndaround time for "+str(p.pid)+" is : "+str(p.turnaround_time))
                print("waiting time for " + str(p.pid) + " is : " + str(p.waiting_time)+"\n")
                q[0].pop(0)
            else:
                q[0].append(p)
                q[0].pop(0)
        elif p.remaining_time == time_Quantem:
            timer -= time_Quantem
            p.remaining_time -= time_Quantem
            current_time += time_Quantem
            print("The process with process id " + str(p.pid) + " completed successfully at " + str(current_time))
            p.turnaround_time = current_time
            total_turnAround_time_for_Roundrobin += p.turnaround_time
            p.waiting_time = p.turnaround_time - p.burst_time
            total_waiting_time_for_Roundrobin += p.waiting_time
            print("turndaround time for " + str(p.pid) + " is : " + str(p.turnaround_time))
            print("waiting time for " + str(p.pid) + " is : " + str(p.waiting_time) + "\n")
            q[0].pop(0)
        else:
            timer -= p.remaining_time
            current_time+=p.remaining_time
            p.remaining_time = 0
            print("The process with process id " + str(p.pid) + " completed successfully at "+str(current_time))
            p.turnaround_time = current_time
            total_turnAround_time_for_Roundrobin += p.turnaround_time
            p.waiting_time = p.turnaround_time - p.burst_time
            total_waiting_time_for_Roundrobin += p.waiting_time
            print("turndaround time for " + str(p.pid) + " is : " + str(p.turnaround_time))
            print("waiting time for " + str(p.pid) + " is : " + str(p.waiting_time)+"\n")
            q[0].pop(0)
    else:
        p = q[0][0]
        print("Process id : "+str(p.pid)+" takes CPU to execute now at "+str(current_time))
        if p.remaining_time <= timer:
            timer -= p.remaining_time
            current_time+=p.remaining_time
            p.remaining_time = 0
            print("The process with process id " + str(p.pid) + " completed successfully at "+str(current_time))
            p.turnaround_time = current_time
            total_turnAround_time_for_Roundrobin += p.turnaround_time
            p.waiting_time = p.turnaround_time - p.burst_time
            total_waiting_time_for_Roundrobin += p.waiting_time
            print("turndaround time for " + str(p.pid) + " is : " + str(p.turnaround_time))
            print("waiting time for " + str(p.pid) + " is : " + str(p.waiting_time)+"\n")
            q[0].pop(0)
        else:
            p.remaining_time -= timer
            current_time+=timer
            timer = 0
    if(len(q[0])==0):
        timer=0
def dequeueSjf(sjfQueue):
    global timer,current_time
    global total_turnAround_time_for_SJF1,total_turnAround_time_for_SJF2,total_waiting_time_for_SJF1,total_waiting_time_for_SJF2
    p = sjfQueue[0]
    print("Process id : "+str(p.pid)+" takes CPU to execute now at "+str(current_time))
    if p.remaining_time <= timer:
        timer -= p.remaining_time
        current_time+=p.remaining_time
        p.remaining_time = 0
        sjfQueue.pop(0)
        print("The process with process id " + str(p.pid) + " completed successfully at "+str(current_time))
        p.turnaround_time = current_time
        p.waiting_time = p.turnaround_time - p.burst_time
        if sjfQueue==q[1]:
            total_turnAround_time_for_SJF1 += p.turnaround_time
            total_waiting_time_for_SJF1 += p.waiting_time
        elif sjfQueue==q[2]:
            total_turnAround_time_for_SJF2 += p.turnaround_time
            total_waiting_time_for_SJF2 += p.waiting_time

        print("turndaround time for " + str(p.pid) + " is : " + str(p.turnaround_time))
        print("waiting time for " + str(p.pid) + " is : " + str(p.waiting_time)+"\n")
    else:
        p.remaining_time -= timer
        current_time+=timer
        timer = 0
    if (len(sjfQueue) == 0):
        timer = 0

def dequeueFcfs():
    global timer,current_time
    global total_turnAround_time_for_FCFS,total_waiting_time_for_FCFS
    p = q[3][0]
    print("Process id : "+str(p.pid)+" takes CPU to execute now at "+str(current_time))
    if p.remaining_time <= timer:
        timer -= p.remaining_time
        current_time+=p.remaining_time
        p.remaining_time = 0
        q[3].pop(0)
        print("The process with process id " + str(p.pid) + " completed successfully at "+str(current_time))
        p.turnaround_time = current_time
        total_turnAround_time_for_FCFS += p.turnaround_time
        p.waiting_time = p.turnaround_time - p.burst_time
        total_waiting_time_for_FCFS += p.waiting_time
        print("turndaround time for " + str(p.pid) + " is : " + str(p.turnaround_time))
        print("waiting time for " + str(p.pid) + " is : " + str(p.waiting_time)+"\n")
    else:
        p.remaining_time -= timer
        current_time+=timer
        timer = 0
    if (len(q[3]) == 0):
        timer = 0
def condition(k):
    global current_queue
    if k==0:
        dequeueRoundRobin()
        current_queue = 0
    elif k==1:
        dequeueSjf(q[1])
        current_queue = 1
    elif k==2:
        dequeueSjf(q[2])
        current_queue = 2
    elif k==3:
        dequeueFcfs()
        current_queue = 3
j=0
while(len(q[0]) != 0) or (len(q[1]) != 0) or (len(q[2]) != 0) or (len(q[3]) != 0):
    if timer == 0:
        timer = 20
        if (current_queue == j):
            if (len(q[(j + 1)%4])!=0):
                condition((j+1)%4)
            elif(len(q[(j + 2)%4])!=0):
                condition((j + 2) % 4)
            elif (len(q[(j + 3) % 4]) !=0):
                condition((j + 3) % 4)
            elif (len(q[(j + 4) % 4]) !=0):
                condition((j + 4) % 4)
    else:
        if (current_queue == j):
            if (len(q[(j) % 4]) != 0):
                    condition((j) % 4)
            elif (len(q[(j + 1) % 4]) != 0):
                    condition((j + 1) % 4)
            elif (len(q[(j + 2) % 4]) != 0):
                    condition((j + 2) % 4)
            elif (len(q[(j + 3) % 4]) != 0):
                    condition((j + 3) % 4)
        j = (j + 1) % 4

print("Processes successfully executed............................................\n")
print("Total waiting time and turn around time calculated\n")

print("Total waiting time for roundrobin : "+str(total_waiting_time_for_Roundrobin))
print("Total TurnAround time for roundrobin : "+str(total_turnAround_time_for_Roundrobin))
print("Total waiting time for SJF1 : "+str(total_waiting_time_for_SJF1))
print("Total TurnArond time for SJF1 : "+str(total_turnAround_time_for_SJF1))
print("Total waiting time for SJF2 : "+str(total_waiting_time_for_SJF2))
print("Total TurnArond time for SJF2 : "+str(total_turnAround_time_for_SJF2))
print("Total waiting time for FCFS : "+str(total_waiting_time_for_FCFS))
print("Total TurnArond time for FCFS : "+str(total_turnAround_time_for_FCFS))

print("\nAverage waiting time and turn around time calculated\n")
print("Average waiting time for roundrobin : "+str(total_waiting_time_for_Roundrobin/n0))
print("Average TurnAround time for roundrobin : "+str(total_turnAround_time_for_Roundrobin/n0))
print("Average waiting time for SJF1 : "+str(total_waiting_time_for_SJF1/n1))
print("Average TurnArond time for SJF1 : "+str(total_turnAround_time_for_SJF1/n1))
print("Average waiting time for SJF2 : "+str(total_waiting_time_for_SJF2/n2))
print("Average TurnArond time for SJF2 : "+str(total_turnAround_time_for_SJF2/n2))
print("Average waiting time for FCFS : "+str(total_waiting_time_for_FCFS/n3))
print("Average TurnArond time for FCFS : "+str(total_turnAround_time_for_FCFS/n3))