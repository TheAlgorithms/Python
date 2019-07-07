import math 

''' Minimax helps to achieve maximum score in a game by checking all possible moves
    depth is current depth in game tree. 
    nodeIndex is index of current node in scores[].
    if move is of maximizer return true else false
    leaves of game tree is stored in scores[]  
    height is maximum height of Game tree
'''

def minimax (Depth, nodeIndex, isMax, scores, height):  

    if Depth == height:  
        return scores[nodeIndex] 

    if isMax: 
        return (max(minimax(Depth + 1, nodeIndex * 2, False, scores, height),
                    minimax(Depth + 1, nodeIndex * 2 + 1, False, scores, height))) 
    return (min(minimax(Depth + 1, nodeIndex * 2, True, scores, height), 
               minimax(Depth + 1, nodeIndex * 2 + 1, True, scores, height))) 

if __name__ == "__main__": 
 
    scores = [90, 23, 6, 33, 21, 65, 123, 34423] 
    height = math.log(len(scores), 2) 

    print("Optimal value : ", end = "") 
    print(minimax(0, 0, True, scores, height)) 
