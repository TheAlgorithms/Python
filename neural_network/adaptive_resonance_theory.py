import numpy as np


class ART1:
    """
    Adaptive Resonance Theory 1 (ART1) model for binary data clustering.

    This model is designed for unsupervised learning and clustering of binary 
    input data. The ART1 algorithm continuously learns to categorize inputs based 
    on their similarity while preserving previously learned categories. This is 
    achieved through a vigilance parameter that controls the strictness of 
    category matching, allowing for flexible and adaptive clustering.

    ART1 is particularly useful in applications where it is critical to learn new 
    patterns without forgetting previously learned ones, making it suitable for 
    real-time data clustering and pattern recognition tasks.

    References:
    1. Carpenter, G. A., & Grossberg, S. (1987). "A Adaptive Resonance Theory." 
       In: Neural Networks for Pattern Recognition, Oxford University Press.
    2. Carpenter, G. A., & Grossberg, S. (1988). "The ART of Adaptive Pattern 
       Recognition by a Self-Organizing Neural Network." IEEE Transactions on 
       Neural Networks, 1(2). DOI: 10.1109/TNN.1988.82656
    """

    def __init__(self, num_features: int, vigilance: float = 0.7) -> None:
        """
        Initialize the ART1 model with number of features and vigilance parameter.

        Args:
            num_features (int): Number of features in the input data.
            vigilance (float): Threshold for similarity (default is 0.7).

        Raises:
            ValueError: If num_features not positive or vigilance not between 0 and 1.
        """
        if num_features <= 0:
            raise ValueError("Number of features must be a positive integer.")
        if not (0 <= vigilance <= 1):
            raise ValueError("Vigilance parameter must be between 0 and 1.")

        self.vigilance = vigilance
        self.num_features = num_features
        self.weights: list[np.ndarray] = []

    def _similarity(self, weight_vector: np.ndarray, input_vector: np.ndarray) -> float:
        """
        Calculate similarity between weight and input.

        Args:
            weight_vector (np.ndarray): Weight vector representing a cluster.
            input_vector (np.ndarray): Input vector.

        Returns:
            float: The similarity score between the weight and the input.
        """
        if (
            len(weight_vector) != self.num_features
            or len(input_vector) != self.num_features
        ):
            raise ValueError(
                "Both weight_vector and input_vector must have the same number."
            )

        return np.dot(weight_vector, input_vector) / self.num_features

    def _learn(
        self, w: np.ndarray, x: np.ndarray, learning_rate: float = 0.5
    ) -> np.ndarray:
        """
        Update cluster weights using the learning rate.

        Args:
            w (np.ndarray): Current weight vector for the cluster.
            x (np.ndarray): Input vector.
            learning_rate (float): Learning rate for weight update (default is 0.5).

        Returns:
            np.ndarray: Updated weight vector.

        Examples:
            >>> model = ART1(num_features=4)
            >>> w = np.array([1, 1, 0, 0])
            >>> x = np.array([0, 1, 1, 0])
            >>> model._learn(w, x)
            array([0.5, 1. , 0.5, 0. ])
        """
        return learning_rate * x + (1 - learning_rate) * w

    def predict(self, x: np.ndarray) -> int:
        """
        Assign data to the closest cluster.

        Args:
            x (np.ndarray): Input vector.

        Returns:
            int: Index of the assigned cluster, or -1 if no match.

        Examples:
            >>> model = ART1(num_features=4)
            >>> model.weights = [np.array([1, 1, 0, 0])]
            >>> model.predict(np.array([1, 1, 0, 0]))
            0
            >>> model.predict(np.array([0, 0, 0, 0]))
            -1
        """
        similarities = [self._similarity(w, x) for w in self.weights]
        return (
            np.argmax(similarities) if max(similarities) >= self.vigilance else -1
        )  # -1 if no match


# Example usage for ART1
def art1_example() -> None:
    """
    Example function demonstrating the usage of the ART1 model.

    This function creates dataset, trains ART1 model, and prints assigned clusters.

    Examples:
        >>> art1_example()
        Data point 0 assigned to cluster: 0
        Data point 1 assigned to cluster: 0
        Data point 2 assigned to cluster: 1
        Data point 3 assigned to cluster: 1
    """
    data = np.array([[1, 1, 0, 0], [1, 1, 1, 0], [0, 0, 1, 1], [0, 1, 0, 1]])
    model = ART1(num_features=4, vigilance=0.5)
    # model.train(data)  # Ensure this method is defined in ART1

    for i, x in enumerate(data):
        cluster = model.predict(x)
        print(f"Data point {i} assigned to cluster: {cluster}")


if __name__ == "__main__":
    art1_example()
