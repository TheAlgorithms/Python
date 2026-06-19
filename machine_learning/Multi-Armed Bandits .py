import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod


class BanditAlgorithm(ABC):
    """Base class for bandit algorithms"""

    def __init__(self, n_arms):
        self.n_arms = n_arms
        self.reset()

    def reset(self):
        self.counts = np.zeros(self.n_arms)
        self.rewards = np.zeros(self.n_arms)
        self.t = 0

    @abstractmethod
    def select_arm(self):
        pass

    def update(self, arm, reward):
        self.t += 1
        self.counts[arm] += 1
        self.rewards[arm] += reward


class EpsilonGreedy(BanditAlgorithm):
    """Epsilon-Greedy Algorithm"""

    def __init__(self, n_arms, epsilon=0.1):
        super().__init__(n_arms)
        self.epsilon = epsilon

    def select_arm(self):
        if np.random.random() < self.epsilon:
            # Explore: random arm
            return np.random.randint(self.n_arms)
        else:
            # Exploit: best arm so far
            avg_rewards = np.divide(
                self.rewards,
                self.counts,
                out=np.zeros_like(self.rewards),
                where=self.counts != 0,
            )
            return np.argmax(avg_rewards)


class UCB(BanditAlgorithm):
    """Upper Confidence Bound Algorithm"""

    def __init__(self, n_arms, c=2.0):
        super().__init__(n_arms)
        self.c = c

    def select_arm(self):
        # If any arm hasn't been tried, try it
        if 0 in self.counts:
            return np.where(self.counts == 0)[0][0]

        # Calculate UCB values
        avg_rewards = self.rewards / self.counts
        confidence = self.c * np.sqrt(np.log(self.t) / self.counts)
        ucb_values = avg_rewards + confidence

        return np.argmax(ucb_values)


class ThompsonSampling(BanditAlgorithm):
    """Thompson Sampling (Beta-Bernoulli)"""

    def __init__(self, n_arms):
        super().__init__(n_arms)
        self.alpha = np.ones(n_arms)  # Prior successes
        self.beta = np.ones(n_arms)  # Prior failures

    def select_arm(self):
        # Sample from Beta distribution for each arm
        samples = np.random.beta(self.alpha, self.beta)
        return np.argmax(samples)

    def update(self, arm, reward):
        super().update(arm, reward)
        # Update Beta parameters
        if reward > 0:
            self.alpha[arm] += 1
        else:
            self.beta[arm] += 1


class GradientBandit(BanditAlgorithm):
    """Gradient Bandit Algorithm"""

    def __init__(self, n_arms, alpha=0.1):
        super().__init__(n_arms)
        self.alpha = alpha
        self.preferences = np.zeros(n_arms)
        self.avg_reward = 0

    def select_arm(self):
        # Softmax to get probabilities
        exp_prefs = np.exp(self.preferences - np.max(self.preferences))
        probs = exp_prefs / np.sum(exp_prefs)
        return np.random.choice(self.n_arms, p=probs)

    def update(self, arm, reward):
        super().update(arm, reward)

        # Update average reward
        self.avg_reward += (reward - self.avg_reward) / self.t

        # Get action probabilities
        exp_prefs = np.exp(self.preferences - np.max(self.preferences))
        probs = exp_prefs / np.sum(exp_prefs)

        # Update preferences
        for a in range(self.n_arms):
            if a == arm:
                self.preferences[a] += (
                    self.alpha * (reward - self.avg_reward) * (1 - probs[a])
                )
            else:
                self.preferences[a] -= (
                    self.alpha * (reward - self.avg_reward) * probs[a]
                )


# Testbed for comparing algorithms
class BanditTestbed:
    """Environment for testing bandit algorithms"""

    def __init__(self, n_arms=10, true_rewards=None):
        self.n_arms = n_arms
        if true_rewards is None:
            self.true_rewards = np.random.normal(0, 1, n_arms)
        else:
            self.true_rewards = true_rewards
        self.optimal_arm = np.argmax(self.true_rewards)

    def get_reward(self, arm):
        """Get noisy reward for pulling an arm"""
        return np.random.normal(self.true_rewards[arm], 1)

    def run_experiment(self, algorithm, n_steps=1000):
        """Run bandit algorithm for n_steps"""
        algorithm.reset()
        rewards = []
        optimal_actions = []

        for _ in range(n_steps):
            arm = algorithm.select_arm()
            reward = self.get_reward(arm)
            algorithm.update(arm, reward)

            rewards.append(reward)
            optimal_actions.append(1 if arm == self.optimal_arm else 0)

        return np.array(rewards), np.array(optimal_actions)


# Example usage and comparison
def compare_algorithms():
    """Compare different bandit algorithms"""

    # Create testbed
    testbed = BanditTestbed(n_arms=10)

    # Initialize algorithms
    algorithms = {
        "ε-greedy (0.1)": EpsilonGreedy(10, epsilon=0.1),
        "ε-greedy (0.01)": EpsilonGreedy(10, epsilon=0.01),
        "UCB (c=2)": UCB(10, c=2),
        "Thompson Sampling": ThompsonSampling(10),
        "Gradient Bandit": GradientBandit(10, alpha=0.1),
    }

    n_steps = 2000
    n_runs = 100

    results = {}

    for name, algorithm in algorithms.items():
        print(f"Running {name}...")
        avg_rewards = np.zeros(n_steps)
        optimal_actions = np.zeros(n_steps)

        for run in range(n_runs):
            rewards, optimal = testbed.run_experiment(algorithm, n_steps)
            avg_rewards += rewards
            optimal_actions += optimal

        avg_rewards /= n_runs
        optimal_actions /= n_runs

        results[name] = {"rewards": avg_rewards, "optimal_actions": optimal_actions}

    # Plot results
    plt.figure(figsize=(15, 5))

    # Average reward over time
    plt.subplot(1, 2, 1)
    for name, result in results.items():
        plt.plot(np.cumsum(result["rewards"]) / np.arange(1, n_steps + 1), label=name)
    plt.xlabel("Steps")
    plt.ylabel("Average Reward")
    plt.title("Average Reward vs Steps")
    plt.legend()
    plt.grid(True)

    # Percentage of optimal actions
    plt.subplot(1, 2, 2)
    for name, result in results.items():
        plt.plot(
            np.cumsum(result["optimal_actions"]) / np.arange(1, n_steps + 1) * 100,
            label=name,
        )
    plt.xlabel("Steps")
    plt.ylabel("% Optimal Action")
    plt.title("Optimal Action Selection vs Steps")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

    return results


# Run the comparison
if __name__ == "__main__":
    results = compare_algorithms()

    # Print final performance
    print("\nFinal Performance (last 100 steps):")
    for name, result in results.items():
        avg_reward = np.mean(result["rewards"][-100:])
        optimal_pct = np.mean(result["optimal_actions"][-100:]) * 100
        print(
            f"{name:20s}: Avg Reward = {avg_reward:.3f}, Optimal = {optimal_pct:.1f}%"
        )
