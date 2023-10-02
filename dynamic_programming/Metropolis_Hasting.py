import numpy as np


def metropolis_hastings(
    target_distribution, proposal_distribution, num_samples, initial_state
):
    samples = [initial_state]
    current_state = initial_state

    for _ in range(num_samples):
        proposed_state = proposal_distribution(current_state)
        acceptance_ratio = min(
            1, target_distribution(proposed_state) / target_distribution(current_state)
        )

        if np.random.rand() < acceptance_ratio:
            current_state = proposed_state

        samples.append(current_state)

    return samples[1:]


def target_distribution(x):
    return np.exp(-(x**2) / 2) / np.sqrt(2 * np.pi)


def proposal_distribution(x):
    return x + np.random.normal(0, 1)


if __name__ == "__main__":
    num_samples = 10000
    initial_state = 0

    samples = metropolis_hastings(
        target_distribution, proposal_distribution, num_samples, initial_state
    )
