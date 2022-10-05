def print_job_scheduling(x, t):
 
    n = len(x)
 
    for i in range(n):
        for j in range(n - 1 - i):
            if x[j][2] < x[j + 1][2]:
                x[j], x[j + 1] = x[j + 1], x[j]
 
    result = [False] * t
 
    job = ['-1'] * t
 
    for i in range(len(arr)):
 
        for j in range(min(t - 1, x[i][1] - 1), -1, -1):
 
            if result[j] is False:
                result[j] = True
                job[j] = x[i][0]
                break
     """
    Print the Jobs
    """
    print(job)
 
 x = [[1, 4, 20],  
              [2, 1, 20],
              [3, 1, 40],
              [4, 1, 30]
 
print_job_scheduling(x, 4)
