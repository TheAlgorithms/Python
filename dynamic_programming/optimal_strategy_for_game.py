"""
Problem statement:

We are given with N coins having value val_1 ... val_n , where n is even. 

We are playing a game with an opponent in alternating turns. 
In each particular turm one player selects one or last coin.
We remove the coin from the row and get the value of the coin.

Find the max possinle amoint of money one can win 

"""


#Input: value in form of given sequence of coins
#Output: Maximum value a player can win from the array of coins

#Imp: N must be even  

def optimal_strategy(coin, N): 
      
    #table to store sub problems

 
    storage = [[0 for i in range(N)] for i in range(N)] 


    #Diagonal traversal 
    
    for gap in range(N): 
        for j in range(gap, N): 
            i = j - gap 
            x = 0

            #option 1 :
            #choose ith coin with Vi value 
            #now other player can choose between Vi+(F(i+2,j)) 
            #or Vi+(F(i+1,j-1))
            #take min of both

            if((i + 2) <= j): 
                x = storage[i + 2][j] 
            y = 0

            #option 2 :
            #choose jth coin with Vj value 
            #now other player can choose between Vi+(F(i+1,j-1)) 
            #or Vi+(F(i,j-2))
            #take min of both
            if((i + 1) <= (j - 1)): 
                y = storage[i + 1][j - 1] 
            z = 0
            if(i <= (j - 2)): 
                z = storage[i][j - 2] 

            #store the maximum of all
            storage[i][j] = max(coin[i] + min(x, y), coin[j] + min(y, z)) 

    #Output at storage[0][n01]
    return storage[0][N - 1] 


#input function
def input_user():
    arr = list(map(int,input("Enter the numbers:").strip().split(" ")))
    n = len(arr) 
    print(optimal_strategy(arr, n)) 


if __name__ == "__main__":
    input_user() 


    
