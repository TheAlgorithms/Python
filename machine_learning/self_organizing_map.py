"""
https://en.wikipedia.org/wiki/Self-organizing_map
"""
import math


class SelfOrganizingMap:
    def get_winner(self, weights: list[list[int]], sample: list[int]) -> list[list[int]]:
        """
        Compute the winning vector by Euclidean distance

        >>> SelfOrganizingMap().get_winner([[1, 2, 3], [4, 5, 6]], [1, 2, 3])
        1
        """
        d0 = 0
        d1 = 0
        for i in range(len(sample)):
            d0 = d0 + math.pow((sample[i] - weights[0][i]), 2)
            d1 = d1 + math.pow((sample[i] - weights[1][i]), 2)
            if d0 > d1:
                return 0
            else:
                return 1

    def update(self, weights: list[list[int]], sample: list[int], j: int, alpha: float) -> list[list[int | float]]:
        """
        Update the winning vector.

        >>> SelfOrganizingMap().update([[1, 2, 3], [4, 5, 6]], [1, 2, 3], 1, 0.1)
        [[1, 2, 3], [3.7, 4.7, 6]]
        """
        for i in range(len(weights)):
            weights[j][i] = weights[j][i] + alpha * (sample[i] - weights[j][i])
        return weights


# Driver code
def main():
    # Training Examples ( m, n )
    training_samples = [[1, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 1]]
    m, n = len(training_samples), len(training_samples[0])

    # weight initialization ( n, C )
    weights = [[0.2, 0.6, 0.5, 0.9], [0.8, 0.4, 0.7, 0.3]]

    # training
    self_organizing_map = SelfOrganizingMap()
    epochs = 3
    alpha = 0.5

    for i in range(epochs):
        for j in range(m):

            # training sample
            sample = training_samples[j]

            # Compute the winning vector
            winner = self_organizing_map.get_winner(weights, sample)

            # Update the winning vector
            weights = self_organizing_map.update(weights, sample, winner, alpha)

    # classify test sample
    sample = [0, 0, 0, 1]
    winner = self_organizing_map.get_winner(weights, sample)

    # results
    print(f"Clusters that the test sample belongs to : {winner}")
    print(f"Weights that have been trained : {weights}")


# running the main() function
if __name__ == "__main__":
    main()
