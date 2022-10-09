# INPUT
N = int(input())
jobs = []
for i in range(N):
    jobs.append(list(map(int, input().split())))

#OUTPUT
# SORT JOBS ACCORDING TO THEIR PROFIT
jobs.sort(key=lambda value: value[2], reverse=True)

# FIND MAXIMUM DEADLINE
max_deadline = max(jobs, key=lambda value: value[1])[1]

# INITIALIZE SLOTS
slots = [0] * max_deadline

# FIND SLOTS FOR JOBS
for job in jobs:
    for i in range(job[1]-1, -1, -1):
        if slots[i] == 0:
            slots[i] = job[0]
            break

# FIND PROFIT AND COUNT OF JOBS
count = 0
profit = 0
for i in slots:
    if i != 0:
        count += 1
        profit += jobs[i-1][2]

# PRINTING NUMBER OF JOBS AND MAXIMUM PROFIT      
print(count, profit)
