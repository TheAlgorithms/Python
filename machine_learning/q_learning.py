"""
Q-Learning is a widely-used model-free algorithm in reinforcement learning that 
learns the optimal action-value function Q(s, a), which tells an agent the expected 
utility of taking action a in state s and then following the optimal policy after.
It is able to find the best policy for any given finite Markov decision process (MDP) 
without requiring a model of the environment.

See: [https://en.wikipedia.org/wiki/Q-learning](https://en.wikipedia.org/wiki/Q-learning)
"""

from collections import defaultdict
import random

# Hyperparameters for Q-Learning
LEARNING_RATE = 0.1
DISCOUNT_FACTOR = 0.97
EPSILON = 0.2
EPSILON_DECAY = 0.995
EPSILON_MIN = 0.01

# Global Q-table to store state-action values
q_table = defaultdict(lambda: defaultdict(float))

# Environment variables for simple grid world
SIZE = 4
GOAL = (SIZE - 1, SIZE - 1)
current_state = (0, 0)


def get_q_value(state, action):
    """
    Get Q-value for a given state-action pair.

    >>> get_q_value((0, 0), 2)
    0.0
    """
    return q_table[state][action]


def get_best_action(state, available_actions):
    """
    Get the action with maximum Q-value in the given state.

    >>> q_table[(0, 0)][1] = 0.7
    >>> q_table[(0, 0)][2] = 0.7
    >>> q_table[(0, 0)][3] = 0.5
    >>> get_best_action((0, 0), [1, 2, 3]) in [1, 2]
    True
    """
    if not available_actions:
        raise ValueError("No available actions provided")
    max_q = max(q_table[state][a] for a in available_actions)
    best = [a for a in available_actions if q_table[state][a] == max_q]
    return random.choice(best)


def choose_action(state, available_actions):
    """
    Choose action using epsilon-greedy policy.

    >>> EPSILON = 0.0
    >>> q_table[(0, 0)][1] = 1.0
    >>> q_table[(0, 0)][2] = 0.5
    >>> choose_action((0, 0), [1, 2])
    1
    """
    global EPSILON
    if not available_actions:
        raise ValueError("No available actions provided")
    if random.random() < EPSILON:
        return random.choice(available_actions)
    return get_best_action(state, available_actions)


def update(state, action, reward, next_state, next_available_actions, done=False):
    """
    Perform Q-value update for a transition using the Q-learning rule.

    Q(s,a) <- Q(s,a) + alpha * (r + gamma * max_a' Q(s',a') - Q(s,a))

    >>> LEARNING_RATE = 0.5
    >>> DISCOUNT_FACTOR = 0.9
    >>> update((0,0), 1, 1.0, (0,1), [1,2], done=True)
    >>> get_q_value((0,0), 1)
    0.5
    """
    global LEARNING_RATE, DISCOUNT_FACTOR
    max_q_next = 0.0 if done or not next_available_actions else max(
        get_q_value(next_state, a) for a in next_available_actions
    )
    old_q = get_q_value(state, action)
    new_q = (1 - LEARNING_RATE) * old_q + LEARNING_RATE * (
        reward + DISCOUNT_FACTOR * max_q_next
    )
    q_table[state][action] = new_q


def get_policy():
    """
    Extract a deterministic policy from the Q-table.

    >>> q_table[(1,2)][1] = 2.0
    >>> q_table[(1,2)][2] = 1.0
    >>> get_policy()[(1,2)]
    1
    """
    policy = {}
    for s, a_dict in q_table.items():
        if a_dict:
            policy[s] = max(a_dict, key=a_dict.get)
    return policy


def reset_env():
    """
    Reset the environment to initial state.
    """
    global current_state
    current_state = (0, 0)
    return current_state


def get_available_actions_env():
    """
    Get available actions in the current environment state.
    """
    return [0, 1, 2, 3]


def step_env(action):
    """
    Take a step in the environment with the given action.
    """
    global current_state
    x, y = current_state
    if action == 0:  # up
        x = max(0, x - 1)
    elif action == 1:  # right
        y = min(SIZE - 1, y + 1)
    elif action == 2:  # down
        x = min(SIZE - 1, x + 1)
    elif action == 3:  # left
        y = max(0, y - 1)
    next_state = (x, y)
    reward = 10.0 if next_state == GOAL else -1.0
    done = next_state == GOAL
    current_state = next_state
    return next_state, reward, done


def run_q_learning():
    """
    Run Q-Learning on the simple grid world environment.
    """
    global EPSILON
    episodes = 200
    for episode in range(episodes):
        state = reset_env()
        done = False
        while not done:
            actions = get_available_actions_env()
            action = choose_action(state, actions)
            next_state, reward, done = step_env(action)
            next_actions = get_available_actions_env()
            update(state, action, reward, next_state, next_actions, done)
            state = next_state
        EPSILON = max(EPSILON * EPSILON_DECAY, EPSILON_MIN)
    policy = get_policy()
    print("Learned Policy (state: action):")
    for s, a in sorted(policy.items()):
        print(f"{s}: {a}")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_q_learning()