def jobSequence(jobs,totalTime):
    result = [False]*totalTime
    jobs.sort(key=lambda x:x[2], reverse=True)

    accepted = [-1]*totalTime
    for i in range(len(jobs)):
        for j in range(min(totalTime-1,jobs[i][1]),-1,-1):
            if result[j] is False:
                result[j] = True
                accepted[j] = jobs[i][0]
                break
    
    print(accepted)

jobs = [
    ['a',2,100],
    ['b',1,19],
    ['c',2,27],
    ['d',1,25],
    ['e',3,15]
]

jobSequence(jobs,3)