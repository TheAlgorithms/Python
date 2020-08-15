import numpy as np
import pickle
import os

"""
This code was written to automate the classic Atari game snake using the algorithm Q-Learning.
"""

with open("Qtable.txt", "rb") as f:
    """
	This function is responsible for loading Qtable.txt if already present
    """
    Q_table = pickle.load(f)
    
def Action(state, Q_table):
    """
	This function returns the most suitable action value from the qtable.
    """
    action = np.argmax(Q_table[state])
    if(action == None):
        action = randomAction()
    return action

def randomAction():
    """
	This function returns random action just in case the Qtable values return None.
    """
    action = np.random.choice([0, 1, 2, 3])
    return action
    
def StateActionReward(player, x_food, y_food):
    """
	This function returns state, action and reward to update the Qtable.
    """
    x_agent, y_agent = player.body[0].pos
    state = State(player, x_food, y_food)
    action = Action(state, Q_table)
    reward = Reward(player, x_food, y_food)
    return state, action, reward

# States to consider:
#   * Food's relative positioning wrt the head
# Checking for food in nine directions
    ###
    # #
    ###
#   * obstruction Ahead, Right, Left

def State(player, x_food, y_food):
    """
	This function returns the state of the agent according to the food's relative positioning wrt to the head
	Checking for food in nine directions
	    ###
	    # #
	    ###
        Obstructions to consider: Ahead, Right, Left  (As these are the movements allowed for the snake)
    """
    x_agent, y_agent = player.body[0].pos
    states = []

    #Code to check for obstacles in front of the agent
    DangerAhead = (player.dirnx == -1 and x_agent + player.delx < 0) or (player.dirnx == -1 and ((x_agent + player.delx, y_agent ) in player.body)) or (player.dirnx == 1 and x_agent + player.delx > 14) or (player.dirnx == 1 and ((x_agent + player.delx, y_agent) in player.body)) or (player.dirny == 1 and y_agent + player.dely > 14) or (player.dirny == 1 and((x_agent, y_agent + player.dely) in player.body)) or (player.dirny == -1 and y_agent + player.dely < 0) or (player.dirny == -1 and ((x_agent, y_agent + player.dely) in player.body))
    #Code to check for obstacles to the left of the agent
    DangerLeft = (player.dirnx == -1 and y_agent + 1 > 14) or (player.dirnx == -1 and ((x_agent, y_agent + 1) in player.body)) or (player.dirnx == 1 and y_agent - 1 < 0) or (player.dirnx == 1 and ((x_agent, y_agent - 1) in player.body)) or (player.dirny == 1 and x_agent + 1 > 14) or (player.dirny == 1 and ((x_agent + 1, y_agent) in player.body)) or (player.dirny == -1 and x_agent - 1 < 0) or (player.dirny == -1 and ((x_agent - 1, y_agent) in player.body))
    #Code to check for obstacles to the right of the agent
    DangerRight = (player.dirnx == -1 and y_agent - 1 < 0) or (player.dirnx == -1 and ((x_agent, y_agent - 1) in player.body)) or (player.dirnx == 1 and y_agent + 1 > 14) or (player.dirnx == 1 and ((x_agent, y_agent + 1) in player.body)) or (player.dirny == 1 and x_agent - 1 < 0) or (player.dirny == 1 and ((x_agent - 1, y_agent) in player.body)) or (player.dirny == -1 and x_agent + 1 > 14) or (player.dirny == -1 and ((x_agent + 1, y_agent) in player.body))
    #Code for food straight wrt head
    FoodStraightAhead = (player.dirnx == 1 and y_agent == y_food and x_food > x_agent) or (player.dirnx == -1 and y_agent == y_food and x_food < x_agent) or (player.dirny == 1 and y_agent < y_food and x_food == x_agent) or (player.dirny == -1 and y_agent > y_food and x_food == x_agent)
    #Code for food which is ahead and right wrt head
    FoodAheadRight = (player.dirnx == 1 and y_agent < y_food and x_food > x_agent) or (player.dirnx == -1 and y_agent > y_food and x_food < x_agent) or (player.dirny == 1 and y_agent < y_food and x_food < x_agent) or (player.dirny == -1 and y_agent > y_food and x_food > x_agent)
    #Code for food which is ahead and right wrt head    
    FoodAheadLeft = (player.dirnx == 1 and y_agent > y_food and x_food > x_agent) or (player.dirnx == -1 and y_agent < y_food and x_food < x_agent) or (player.dirny == 1 and y_agent < y_food and x_food > x_agent) or (player.dirny == -1 and y_agent > y_food and x_food < x_agent)
    #Code for food which is ahead and right wrt head
    FoodBehindRight = (player.dirnx == 1 and y_agent < y_food and x_food < x_agent) or (player.dirnx == -1 and y_agent > y_food and x_food > x_agent) or (player.dirny == 1 and y_agent > y_food and x_food < x_agent) or (player.dirny == -1 and y_agent < y_food and x_food > x_agent)
    #Code for food which is ahead and right wrt head
    FoodBehindLeft = (player.dirnx == 1 and y_agent > y_food and x_food < x_agent) or (player.dirnx == -1 and y_agent < y_food and x_food > x_agent) or (player.dirny == 1 and y_agent > y_food and x_food > x_agent) or (player.dirny == -1 and y_agent < y_food and x_food < x_agent)
    # Code for food exactly behind
    FoodBehind = (player.dirnx == 1 and y_agent == y_food and x_food < x_agent) or (player.dirnx == -1 and y_agent == y_food and x_food > x_agent) or (player.dirny == 1 and y_agent > y_food and x_food == x_agent) or (player.dirny == -1 and y_agent < y_food and x_food == x_agent)
    # Code for food left
    FoodLeft = (player.dirnx == 1 and y_agent > y_food and x_food == x_agent) or (player.dirnx == -1 and y_agent < y_food and x_food == x_agent) or (player.dirny == 1 and y_agent == y_food and x_food > x_agent) or (player.dirny == -1 and y_agent == y_food and x_food < x_agent)
    # Code for food right
    FoodRight = (player.dirnx == 1 and y_agent < y_food and x_food == x_agent) or (player.dirnx == -1 and y_agent > y_food and x_food == x_agent) or (player.dirny == 1 and y_agent == y_food and x_food < x_agent) or (player.dirny == -1 and y_agent == y_food and x_food > x_agent)
    # Adding to states list while priortizing danger over eating food
    states = [1 if DangerAhead is True else 0,1 if DangerLeft is True else 0,
            1 if DangerRight is True else 0]
    if(DangerAhead == 0) and (DangerRight == 0) and(DangerLeft == 0):
        states.append(1 if FoodStraightAhead is True else 0) 
        states.append(1 if FoodAheadRight is True else 0) 
        states.append(1 if FoodAheadLeft is True else 0) 
        states.append(1 if FoodBehindRight is True else 0)
        states.append(1 if FoodBehindLeft is True else 0) 
        states.append(1 if FoodBehind is True else 0)
        states.append(1 if FoodLeft is True else 0)
        states.append(1 if FoodRight is True else 0)
    else:
        for i in range(8):
            states.append(0)
    state = 0
    for i in range(11):
        if states[i] == 1:
            state = i
    return state
    
def dist(x1, y1, x2, y2):
    """
       For calculation of Euler Distance.
    """
    dist = (x1 - x2)**2 + (y1 - y2)**2
    return dist**0.5

# Reward conditions:
#   * +10 for eating food
#   * -12 for dying
#   * -2 for getting closer
#   * -7 for going away from the fruit
          
def Reward(player, x_food, y_food):
    """
	This function assigns the reward to the agent according to the action taken
    """
    x_agent, y_agent = player.body[0].pos
    if (x_agent == x_food and y_agent == y_food):
        return +10
    elif (player.dirnx == -1 and x_agent + player.delx <= 0) or (player.dirnx == -1 and ((x_agent + player.delx, y_agent + player.dely) in player.body)) or (player.dirnx == 1 and x_agent + player.delx >= 14) or (player.dirnx == 1 and ((x_agent + player.dirnx, y_agent + player.dely) in player.body)) or (player.dirny == 1 and y_agent + player.dely >= 14) or (player.dirny == 1 and((x_agent + player.delx, y_agent + player.dely) in player.body)) or (player.dirny == -1 and y_agent + player.dely <= 0) or (player.dirny == -1 and ((x_agent + player.delx, y_agent + player.dely) in player.body)) or (player.resetDone == True):
        return -12
    elif dist(x_agent + player.delx, y_agent + player.dely, x_food, y_food) - dist(x_agent, y_agent, x_food, y_food) > 0:
        return -2
    elif dist(x_agent + player.delx, y_agent + player.dely, x_food, y_food) - dist(x_agent, y_agent, x_food, y_food) < 0:
        return -7

def Learn(state, action, reward, next_state, next_action, i,trialNumber, epsilon):
    """
	This function is for iteratively updating the Qtable.
    """
    gamma = 0.9
    learning_rate = 0.7
    Q_tablePrev = Q_table
    currentQ = Q_table[state][action]
    nextQ = Q_table[next_state][next_action]
    newQ = (1 - learning_rate)*currentQ + learning_rate*( reward + gamma*nextQ) # Qlearning Algorithm to get new q value for the q table.
    Q_table[state][action] = newQ
    state = next_state
    currentQ = nextQ     
    if trialNumber % 100 == 0:
        print("Printing Q_table: ")
        print(Q_table)
        with open("Qtable.txt", "wb") as f:
            pickle.dump(Q_table, f)
