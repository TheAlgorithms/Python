import math 
  
def minimax (Depth, nodeIndex, isMax, scores, height):  
 
    if (Depth == height):  
        return scores[nodeIndex] 
      
    if (isMax): 
        return max(minimax(Depth + 1, nodeIndex * 2, False, scores, height), minimax(Depth + 1, nodeIndex * 2 + 1, False, scores, height)) 
    return min(minimax(Depth + 1, nodeIndex * 2, True, scores, height), minimax(Depth + 1, nodeIndex * 2 + 1, True, scores, height)) 

      
scores = [90, 23, 6, 33, 21, 65, 123, 34423] 
  
height = math.log(len(scores), 2) 
  
print("Optimal value : ", end = "") 
print(minimax(0, 0, True, scores, height)) 
