'''
Given an array of scores that are non-negative integers.
Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on.
Each time a player picks a number, that number will not be available for the next player.
This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.

Guide Through:

Lets say we have arr of  -> [1,5,2]
    |(1,0)|     |     |
    |_____|_____|_____| # If we have only 1
    |     |(5,0)|     |
    |_____|_____|_____| # If we have only 5
    |     |     |(2,0)|
    |_____|_____|_____| # If we have only 2

    |(1,0)|(5,1)|     |
    |_____|_____|_____| # If we have only 1,5
    |     |(5,0)|(5,2)|
    |_____|_____|_____| # If we have only 5,2
    |     |     |(2,0)|
    |_____|_____|_____|

    dp[0][1] choice: 2 ways take 5 or 1
    -> If we take 5
       we have only 1 which is dp[0][0].
       player 2 takes dp[0][0][0] leaves dp[0][0][1]
       so if 5 its 5+dp[0][0][1] = 5 1st player
                    dp[0][0][0]  = 1 2nd player

    -> If 1
        we have a 5 which is dp[1][1].
        As we took 1 its 2nd players turn he takes 5(dp[1][1][0])
        so its 1+dp[1][1][1] = 1 1st player
               dp[1][1][0]   = 5 2nd player

        As we want to win we take the best possible way so that we can lead here its
        way 1 by taking 5.

     Same for dp[1][2] position.

     |(1,0)|(5,1)|(3,5)|
     |_____|_____|_____| # If we have only 1,5,2
     |     |(5,0)|(5,2)|
     |_____|_____|_____|
     |     |     |(2,0)|
     |_____|_____|_____|

     dp[0][2] choice: 2 ways take 1 or 2
     -> If we take 1
        we have 5,2 which is dp[1][2].
        so 2nd player takes dp[1][2][0] as every players wants to take max
        which leaves dp[1][2][1]
        so its 1+dp[1][2][1] = 3 1st player
                dp[1][2][0]  = 5 2nd player

     -> If we take 2
        we have 1,5 in the array which is dp[0][1]
        so 2nd player takes dp[0][1][0] as every players wants to take max.
        which leaves dp[0][1][1]
        so its 2+dp[0][1][1] = 3 1st player
                dp[0][1][0]  = 5 2nd player

        Here Player 1 loss no matter what possible combination he takes.
'''


nums = list(map(int,input().split()))
# 2-D array to store
dp = [[0] * len(nums) for _ in range(len(nums))]

# If there is only 1 value in the array then 1st player takes it has arr[0] and 2nd player has 0
#so we store (arr[i],0)->(first_player_score,second_player_score)
for q in range(len(nums)):
    dp[q][q] = (nums[q], 0)

# To fill the dp from 0th row and 1st column
for i in range(1, len(nums)):
    # As we need to move to column+1 and row+1 we use k for rows so we incerment k+=1
    k = 0
    for j in range(i, len(nums)):
        # we check if 1st possible(taking starting element in the array) way gives us higher value if yes we take it
        if nums[k] + dp[k + 1][j][1] >= nums[j] + dp[k][j - 1][1]:
            dp[k][j] = (nums[k] + dp[k + 1][j][1], dp[k + 1][j][0])
        else:
            dp[k][j] = (nums[j] + dp[k][j - 1][1], dp[k][j - 1][0])
        k+=1

# we compare scores in the final end if 1st player has >= score of 2nd player we return True else False
if dp[0][len(nums)-1][0]>=dp[0][len(nums)-1][1]:
    print(True)
else:
    print(False)
