

#Activity Selection Problem
#https://practice.geeksforgeeks.org/problems/activity-selection-1587115620/1

class Solution:

    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):


        def comp(arr):
            return arr[1]

        arr=[]

        for i in range (n):
            arr.append([start[i],end[i]])


        arr.sort(key=comp)


        prev=0
        ans=1
        for i in range (1,n):
            if arr[prev][1]<arr[i][0]:
                ans+=1
                prev=i

        return ans


# Job SequencingProblem
# https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1


class Solution:

    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,jobs,n):



        def comp(arr):
            return arr[1]

        jobs.sort(key=lambda x:x.profit, reverse=True)


        ans=0

        marked=[False for i in range (n)]
        count=1
        for i in range (n):

            for j in range(min(n,jobs[i].deadline)-1 ,-1,-1):
                if marked[j]==False:
                    count+=1
                    ans+=jobs[i].profit
                    marked[j]=True
                    break


        return [count-1,ans]

#Fractional Knapsack
https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1
class Solution:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

   # Main greedy function to solve problem
   def fractionalKnapsack(W, arr):

    # sorting Item on basis of ratio
    arr.sort(key=lambda x: (x.value/x.weight), reverse=True)

    # Uncomment to see new order of Items with their
    # ratio
    # for item in arr:
    #     print(item.value, item.weight, item.value/item.weight)

    # Result(value in Knapsack)
    finalvalue = 0.0

    # Looping through all Items
    for item in arr:

        # If adding Item won't overflow, add it completely
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.value

        # If we can't add current Item, add fractional part
        # of it
        else:
            finalvalue += item.value * W / item.weight
            break
    # Returning final value
    return finalvalue
