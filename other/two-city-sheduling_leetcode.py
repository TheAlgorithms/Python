class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
       costs = sorted(costs,key = lambda x:x[0]-x[1])
       result =0
       for i in range(len(costs)):
         if(i <len(costs)//2):
            result += costs[i][0]
         else:
            result +=costs[i][1]
       return(result)
