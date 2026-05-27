"""
Q-Learning is a widely-used model-free algorithm in reinforcement learning that
learns the optimal action-value function Q(s, a), which tells an agent the expected
utility of taking action a in state s and then following the optimal policy after.
It is able to find the best policy for any given finite Markov decision process (MDP)
without requiring a model of the environment.

See: [https://en.wikipedia.org/wiki/Q-learning](https://en.wikipedia.org/wiki/Q-learning)
"""

import random
from collections import defaultdict

# Type alias for state
type State = tuple[int, int]

# Hyperparameters for Q-Learning
LEARNING_RATE = 0.1
DISCOUNT_FACTOR = 0.97
EPSILON = 0.2
EPSILON_DECAY = 0.995
EPSILON_MIN = 0.01

# Global Q-table to store state-action values
q_table: dict[State, dict[int, float]] = defaultdict(lambda: defaultdict(float))

# Environment variables for simple grid world
SIZE = 4
GOAL = (SIZE - 1, SIZE - 1)
current_state = (0, 0)


def get_q_value(state: State, action: int) -> float:
    """
    Get Q-value for a given state-action pair.

    >>> q_table.clear()
    >>> get_q_value((0, 0), 2)
    0.0
    """
    return q_table[state][action]


def get_best_action(state: State, available_actions: list[int]) -> int:
    """
    Get the action with maximum Q-value in the given state.

    >>> q_table.clear()
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


def choose_action(state: State, available_actions: list[int]) -> int:
    """
    Choose action using epsilon-greedy policy.

    >>> q_table.clear()
    >>> old_epsilon = EPSILON
    >>> EPSILON = 0.0
    >>> q_table[(0, 0)][1] = 1.0
    >>> q_table[(0, 0)][2] = 0.5
    >>> result = choose_action((0, 0), [1, 2])
    >>> EPSILON = old_epsilon  # Restore
    >>> result
    1
    """
    global EPSILON
    if not available_actions:
        raise ValueError("No available actions provided")
    if random.random() < EPSILON:
        return random.choice(available_actions)
    return get_best_action(state, available_actions)


def update(
    state: State,
    action: int,
    reward: float,
    next_state: State,
    next_available_actions: list[int],
    done: bool = False,
    alpha: float | None = None,
    gamma: float | None = None,
) -> None:
    """
    Perform Q-value update for a transition using the Q-learning rule.

    Q(s,a) <- Q(s,a) + alpha * (r + gamma * max_a' Q(s',a') - Q(s,a))

    >>> q_table.clear()
    >>> update((0, 0), 1, 1.0, (0, 1), [1, 2], done=True, alpha=0.5, gamma=0.9)
    >>> get_q_value((0, 0), 1)
    0.5
    """
    global LEARNING_RATE, DISCOUNT_FACTOR
    alpha = alpha if alpha is not None else LEARNING_RATE
    gamma = gamma if gamma is not None else DISCOUNT_FACTOR
    max_q_next = (
        0.0
        if done or not next_available_actions
        else max(get_q_value(next_state, a) for a in next_available_actions)
    )
    old_q = get_q_value(state, action)
    new_q = (1 - alpha) * old_q + alpha * (reward + gamma * max_q_next)
    q_table[state][action] = new_q


def get_policy() -> dict[State, int]:
    """
    Extract a deterministic policy from the Q-table.


    >>> q_table.clear()
    >>> q_table[(1, 2)][1] = 2.0
    >>> q_table[(1, 2)][2] = 1.0
    >>> get_policy()[(1, 2)]
    1
    """
    policy: dict[State, int] = {}
    for s, a_dict in q_table.items():
        if a_dict:
            policy[s] = max(a_dict, key=lambda a: a_dict[a])
    return policy


def reset_env() -> State:
    """
    Reset the environment to initial state.

    >>> old_state = current_state
    >>> current_state = (1, 1)  # Simulate non-initial state
    >>> result = reset_env()
    >>> current_state = old_state  # Restore for other tests
    >>> result
    (0, 0)
    """
    global current_state
    current_state = (0, 0)
    return current_state


def get_available_actions_env() -> list[int]:
    """
    Get available actions in the current environment state.
    """
    return [0, 1, 2, 3]  # 0: up, 1: right, 2: down, 3: left


def step_env(action: int) -> tuple[State, float, bool]:
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


def run_q_learning() -> None:
    """
    Run Q-Learning on the simple grid world environment.
    """
    global EPSILON
    episodes = 200
    for _ in range(episodes):
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
