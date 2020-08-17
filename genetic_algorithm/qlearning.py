"""
Implementation of the Qlearning Algorithm.
Wikipedia link: https://en.wikipedia.org/wiki/Q-learning
Author: AryanRaj315
"""

import numpy as np
import pickle


GAMMA = 0.9
LEARNING_RATE = 0.7


if __name__ == "__main__":
    with open("Qtable.txt", "rb") as f:
        """
        This code is responsible for loading Qtable.txt if already present
        """
        Q_table = pickle.load(f)


def next_best_action(state: int, Q_table: np.ndarray) -> int:
    """
    Return the most suitable action value from Q_table or a random action
    if there is no np.argmax(Q_table[state]).
    >>> next_best_action(1, []) in [0, 1, 2, 3]
    True
    """
    action = np.argmax(Q_table[state])
    return action if action is not None else np.random.choice([0, 1, 2, 3])


def state_action_reward(player: object, x_food: int, y_food: int) -> tuple:
    """
    This function returns state, action and reward to update the Qtable.
    """
    x_agent, y_agent = player.body[0].pos
    current_state = state(player, x_food, y_food)
    current_action = next_best_action(state, Q_table)
    current_reward = reward(player, x_food, y_food)
    return (current_state, current_action, current_reward)


# States to consider:
#   * Food's relative positioning wrt the head
# Checking for food in nine directions
###
# #
###
#   * obstruction Ahead, Right, Left


def state(player: object, x_food: int, y_food: int) -> int:
    """
    This function Checks for the food in nine directions and returns state.
    """
    x_agent, y_agent = player.body[0].pos
    states = []

    # Code to check for obstacles in front of the agent
    DangerAhead = (
        (player.dirnx == -1 and x_agent + player.delx < 0)
        or (player.dirnx == -1 and ((x_agent + player.delx, y_agent) in player.body))
        or (player.dirnx == 1 and x_agent + player.delx > 14)
        or (player.dirnx == 1 and ((x_agent + player.delx, y_agent) in player.body))
        or (player.dirny == 1 and y_agent + player.dely > 14)
        or (player.dirny == 1 and ((x_agent, y_agent + player.dely) in player.body))
        or (player.dirny == -1 and y_agent + player.dely < 0)
        or (player.dirny == -1 and ((x_agent, y_agent + player.dely) in player.body))
    )
    # Code to check for obstacles to the left of the agent
    DangerLeft = (
        (player.dirnx == -1 and y_agent + 1 > 14)
        or (player.dirnx == -1 and ((x_agent, y_agent + 1) in player.body))
        or (player.dirnx == 1 and y_agent - 1 < 0)
        or (player.dirnx == 1 and ((x_agent, y_agent - 1) in player.body))
        or (player.dirny == 1 and x_agent + 1 > 14)
        or (player.dirny == 1 and ((x_agent + 1, y_agent) in player.body))
        or (player.dirny == -1 and x_agent - 1 < 0)
        or (player.dirny == -1 and ((x_agent - 1, y_agent) in player.body))
    )
    # Code to check for obstacles to the right of the agent
    DangerRight = (
        (player.dirnx == -1 and y_agent - 1 < 0)
        or (player.dirnx == -1 and ((x_agent, y_agent - 1) in player.body))
        or (player.dirnx == 1 and y_agent + 1 > 14)
        or (player.dirnx == 1 and ((x_agent, y_agent + 1) in player.body))
        or (player.dirny == 1 and x_agent - 1 < 0)
        or (player.dirny == 1 and ((x_agent - 1, y_agent) in player.body))
        or (player.dirny == -1 and x_agent + 1 > 14)
        or (player.dirny == -1 and ((x_agent + 1, y_agent) in player.body))
    )
    # Code for food straight wrt head
    FoodStraightAhead = (
        (player.dirnx == 1 and y_agent == y_food and x_food > x_agent)
        or (player.dirnx == -1 and y_agent == y_food and x_food < x_agent)
        or (player.dirny == 1 and y_agent < y_food and x_food == x_agent)
        or (player.dirny == -1 and y_agent > y_food and x_food == x_agent)
    )
    # Code for food which is ahead and right wrt head
    FoodAheadRight = (
        (player.dirnx == 1 and y_agent < y_food and x_food > x_agent)
        or (player.dirnx == -1 and y_agent > y_food and x_food < x_agent)
        or (player.dirny == 1 and y_agent < y_food and x_food < x_agent)
        or (player.dirny == -1 and y_agent > y_food and x_food > x_agent)
    )
    # Code for food which is ahead and right wrt head
    FoodAheadLeft = (
        (player.dirnx == 1 and y_agent > y_food and x_food > x_agent)
        or (player.dirnx == -1 and y_agent < y_food and x_food < x_agent)
        or (player.dirny == 1 and y_agent < y_food and x_food > x_agent)
        or (player.dirny == -1 and y_agent > y_food and x_food < x_agent)
    )
    # Code for food which is ahead and right wrt head
    FoodBehindRight = (
        (player.dirnx == 1 and y_agent < y_food and x_food < x_agent)
        or (player.dirnx == -1 and y_agent > y_food and x_food > x_agent)
        or (player.dirny == 1 and y_agent > y_food and x_food < x_agent)
        or (player.dirny == -1 and y_agent < y_food and x_food > x_agent)
    )
    # Code for food which is ahead and right wrt head
    FoodBehindLeft = (
        (player.dirnx == 1 and y_agent > y_food and x_food < x_agent)
        or (player.dirnx == -1 and y_agent < y_food and x_food > x_agent)
        or (player.dirny == 1 and y_agent > y_food and x_food > x_agent)
        or (player.dirny == -1 and y_agent < y_food and x_food < x_agent)
    )
    # Code for food exactly behind
    FoodBehind = (
        (player.dirnx == 1 and y_agent == y_food and x_food < x_agent)
        or (player.dirnx == -1 and y_agent == y_food and x_food > x_agent)
        or (player.dirny == 1 and y_agent > y_food and x_food == x_agent)
        or (player.dirny == -1 and y_agent < y_food and x_food == x_agent)
    )
    # Code for food left
    FoodLeft = (
        (player.dirnx == 1 and y_agent > y_food and x_food == x_agent)
        or (player.dirnx == -1 and y_agent < y_food and x_food == x_agent)
        or (player.dirny == 1 and y_agent == y_food and x_food > x_agent)
        or (player.dirny == -1 and y_agent == y_food and x_food < x_agent)
    )
    # Code for food right
    FoodRight = (
        (player.dirnx == 1 and y_agent < y_food and x_food == x_agent)
        or (player.dirnx == -1 and y_agent > y_food and x_food == x_agent)
        or (player.dirny == 1 and y_agent == y_food and x_food < x_agent)
        or (player.dirny == -1 and y_agent == y_food and x_food > x_agent)
    )
    # Adding to states list while priortizing danger over eating food
    states = [int(x) for x in (DangerAhead, DangerLeft, DangerRight)]
    if sum(states) == 0:
        states += [int(x) for x in (
            FoodStraightAhead, FoodAheadRight, FoodAheadLeft, FoodBehindRight,
            FoodBehindLeft, FoodBehind, FoodLeft, FoodRight
        )]
    else:
        states += [0] * 8
    state = 0
    for i in range(11):
        if states[i] == 1:
            state = i
    return state


def euler_dist(x1: int, y1: int, x2: int, y2: int) -> int:
    """
    For calculation of Euler Distance.
    """
    dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
    return dist ** 0.5


# Reward conditions:
#   * +10 for eating food
#   * -12 for dying
#   * -2 for getting closer
#   * -7 for going away from the fruit


def reward(player: object, x_food: int, y_food: int) -> int:
    """
    This function assigns the reward to the agent according to the action taken
    """
    x_agent, y_agent = player.body[0].pos
    if x_agent == x_food and y_agent == y_food:
        return +10
    elif (
        (player.dirnx == -1 and x_agent + player.delx <= 0)
        or (
            player.dirnx == -1
            and ((x_agent + player.delx, y_agent + player.dely) in player.body)
        )
        or (player.dirnx == 1 and x_agent + player.delx >= 14)
        or (
            player.dirnx == 1
            and ((x_agent + player.dirnx, y_agent + player.dely) in player.body)
        )
        or (player.dirny == 1 and y_agent + player.dely >= 14)
        or (
            player.dirny == 1
            and ((x_agent + player.delx, y_agent + player.dely) in player.body)
        )
        or (player.dirny == -1 and y_agent + player.dely <= 0)
        or (
            player.dirny == -1
            and ((x_agent + player.delx, y_agent + player.dely) in player.body)
        )
        or (player.resetDone is True)
    ):
        return -12
    elif (
        euler_dist(x_agent + player.delx, y_agent + player.dely, x_food, y_food)
        - euler_dist(x_agent, y_agent, x_food, y_food)
        > 0
    ):
        return -2
    elif (
        euler_dist(x_agent + player.delx, y_agent + player.dely, x_food, y_food)
        - euler_dist(x_agent, y_agent, x_food, y_food)
        < 0
    ):
        return -7


def learn(
        state: int, action: int, reward: int, next_state: int,
        next_action: int, i: int, trialNumber: int, epsilon: float) -> type(None):
    """
    This function is for iteratively updating the Qtable.
    """
    currentQ = Q_table[state][action]
    nextQ = Q_table[next_state][next_action]
    # Qlearning Algorithm to get new q value for the q table.
    newQ = (1 - LEARNING_RATE) * currentQ + LEARNING_RATE * (reward + GAMMA * nextQ)
    Q_table[state][action] = newQ
    state = next_state
    currentQ = nextQ
    if trialNumber % 100 == 0:
        print("Printing Q_table: ")
        print(Q_table)
