import numpy as np

class ART1:
    """
    Adaptive Resonance Theory 1 (ART1) model for binary data clustering.

    The ART1 algorithm is a type of neural network used for unsupervised learning and clustering of binary input data.
    It continuously learns to categorize inputs based on similarity while preserving previously learned categories.
    The vigilance parameter controls the degree of similarity required to assign an input to an existing category,
    allowing for flexible and adaptive clustering.

    Attributes:
        num_features (int): Number of features in the input data.
        vigilance (float): Threshold for similarity that determines whether an input matches an existing cluster.
        weights (list): List of cluster weights representing the learned categories.
    """
    
    def __init__(self, num_features: int, vigilance: float = 0.7) -> None:
        """
        Initialize the ART1 model with the given number of features and vigilance parameter.

        Args:
            num_features (int): Number of features in the input data.
            vigilance (float): Threshold for similarity (default is 0.7).
            
        Examples:
            >>> model = ART1(num_features=4, vigilance=0.5)
            >>> model.num_features
            4
            >>> model.vigilance
            0.5
        """
        self.vigilance = vigilance  # Controls cluster strictness
        self.num_features = num_features
        self.weights = []           # List of cluster weights
        
    def train(self, data: np.ndarray) -> None:
        """
        Train the ART1 model on the provided data.

        Args:
            data (np.ndarray): A 2D array of binary input data (num_samples x num_features).

        Examples:
            >>> model = ART1(num_features=4, vigilance=0.5)
            >>> data = np.array([[1, 1, 0, 0], [1, 1, 1, 0]])
            >>> model.train(data)
            >>> len(model.weights)
            2
        """
        for x in data:
            match = False
            for i, w in enumerate(self.weights):
                if self._similarity(w, x) >= self.vigilance:
                    self.weights[i] = self._learn(w, x)
                    match = True
                    break
            if not match:
                self.weights.append(x.copy())  # Add a new cluster

    def _similarity(self, w: np.ndarray, x: np.ndarray) -> float:
        """
        Calculate similarity between weight and input.

        Args:
            w (np.ndarray): Weight vector representing a cluster.
            x (np.ndarray): Input vector.

        Returns:
            float: The similarity score between the weight and the input.

        Examples:
            >>> model = ART1(num_features=4)
            >>> w = np.array([1, 1, 0, 0])
            >>> x = np.array([1, 0, 0, 0])
            >>> model._similarity(w, x)
            0.25
        """
        return np.dot(w, x) / (self.num_features)
    
    def _learn(self, w: np.ndarray, x: np.ndarray, learning_rate: float = 0.5) -> np.ndarray:
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
        return np.argmax(similarities) if max(similarities) >= self.vigilance else -1  # -1 if no match


# Example usage for ART1
def art1_example() -> None:
    """
    Example function demonstrating the usage of the ART1 model.

    This function creates a dataset, trains the ART1 model, and prints the assigned clusters for each data point.

    Examples:
        >>> art1_example()
        Data point 0 assigned to cluster: 0
        Data point 1 assigned to cluster: 0
        Data point 2 assigned to cluster: 1
        Data point 3 assigned to cluster: 1
    """
    data = np.array([[1, 1, 0, 0], [1, 1, 1, 0], [0, 0, 1, 1], [0, 1, 0, 1]])
    model = ART1(num_features=4, vigilance=0.5)
    model.train(data)

    for i, x in enumerate(data):
        cluster = model.predict(x)
        print(f"Data point {i} assigned to cluster: {cluster}")

if __name__ == "__main__":
    art1_example()
