"""

This is a python implementation for questions involving task assignments between people.
Here Bitmasking and DP are used for solving this.

Question :-
We have N tasks and M people. Each person in M can do only certain of these tasks. Also a person can do only one task and a task is performed only by one person.
Find the total no of ways in which the tasks can be distributed.


"""
from __future__ import print_function
from collections import defaultdict


class AssignmentUsingBitmask:
    def __init__(self,task_performed,total):
        
        self.total_tasks = total    #total no of tasks (N)
        
        # DP table will have a dimension of (2^M)*N
        # initially all values are set to -1
        self.dp = [[-1 for i in range(total+1)] for j in range(2**len(task_performed))]
        
        self.task = defaultdict(list)   #stores the list of persons for each task
        
        #finalmask is used to check if all persons are included by setting all bits to 1
        self.finalmask = (1<<len(task_performed)) - 1
    
    
    def CountWaysUtil(self,mask,taskno):
        
        # if mask == self.finalmask all persons are distributed tasks, return 1
        if mask == self.finalmask:
            return 1

        #if not everyone gets the task and no more tasks are available, return 0
        if taskno > self.total_tasks:
            return 0

        #if case already considered
        if self.dp[mask][taskno]!=-1:
            return self.dp[mask][taskno]

        # Number of ways when we dont this task in the arrangement
        total_ways_util = self.CountWaysUtil(mask,taskno+1)

        # now assign the tasks one by one to all possible persons and recursively assign for the remaining tasks.
        if taskno in self.task:
            for p in self.task[taskno]:
                
                # if p is already given a task
                if mask & (1<<p):
                    continue
                
                # assign this task to p and change the mask value. And recursively assign tasks with the new mask value.
                total_ways_util+=self.CountWaysUtil(mask|(1<<p),taskno+1)
        
        # save the value.
        self.dp[mask][taskno] = total_ways_util
        
        return self.dp[mask][taskno] 

    def countNoOfWays(self,task_performed):

        # Store the list of persons for each task
        for i in range(len(task_performed)):
            for j in task_performed[i]:
                self.task[j].append(i)
        
        # call the function to fill the DP table, final answer is stored in dp[0][1]
        return self.CountWaysUtil(0,1)
        

if __name__ == '__main__':
    
    total_tasks = 5    #total no of tasks (the value of N)
    
    #the list of tasks that can be done by M persons.
    task_performed = [ 
        [ 1 , 3 , 4 ],
        [ 1 , 2 , 5 ],
        [ 3 , 4 ]
         ]
    print(AssignmentUsingBitmask(task_performed,total_tasks).countNoOfWays(task_performed))
    """
    For the particular example the tasks can be distributed as
    (1,2,3), (1,2,4), (1,5,3), (1,5,4), (3,1,4), (3,2,4), (3,5,4), (4,1,3), (4,2,3), (4,5,3)
    total 10
    """