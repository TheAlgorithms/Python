import numpy as np
import matplotlib.pyplot as plt


# Define the target distribution (standard normal in this case)
def target_distribution(x):
    return np.exp(-0.5 * x**2) / np.sqrt(2 * np.pi)


# Metropolis-Hastings algorithm
def metropolis_hastings(
    target_dist, proposal_dist, num_samples, initial_state=0, burn_in=1000
):
    samples = []
    current_state = initial_state

    for _ in range(num_samples + burn_in):
        # Propose a new state from the proposal distribution
        proposed_state = current_state + proposal_dist()

        # Calculate acceptance ratio
        acceptance_ratio = target_dist(proposed_state) / target_dist(current_state)

        # Accept the proposed state with probability min(1, acceptance_ratio)
        if np.random.rand() < acceptance_ratio:
            current_state = proposed_state

        # If we're past the burn-in period, add the state to the samples
        if _ >= burn_in:
            samples.append(current_state)

    return samples


# Proposal distribution (e.g., a Gaussian with a small standard deviation)
def gaussian_proposal():
    return np.random.normal(0, 0.5)


# Number of samples to generate
num_samples = 10000

# Run Metropolis-Hastings
samples = metropolis_hastings(target_distribution, gaussian_proposal, num_samples)

# Plot the results
plt.hist(samples, bins=50, density=True, label="Samples")
x = np.linspace(-5, 5, 1000)
plt.plot(x, target_distribution(x), "r", label="True Distribution")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.legend()
plt.show()
