import numpy as np
from numpy.random import default_rng

rng = default_rng(42)


class Dataloader:
    """
    DataLoader class for handling dataset, including data shuffling,
    one-hot encoding, and train-test splitting.

    Example usage:
    >>> X = [[0.0, 0.0], [1.0, 1.0], [1.0, 0.0], [0.0, 1.0]]
    >>> y = [0, 1, 0, 0]
    >>> loader = Dataloader(X, y)
    >>> len(loader.get_train_test_data())  # Returns train and test data
    4
    >>> loader.one_hot_encode([0, 1, 0], 2)  # Returns one-hot encoded labels
    array([[0.99, 0.  ],
           [0.  , 0.99],
           [0.99, 0.  ]])
    >>> loader.get_inout_dim()
    (2, 3)
    >>> loader.one_hot_encode([0, 2], 3)
    array([[0.99, 0.  , 0.  ],
           [0.  , 0.  , 0.99]])
    """

    def __init__(self, features: list[list[float]], labels: list[int]) -> None:
        """
        Initializes the Dataloader instance with feature matrix
        features and labels labels.

        Args:
            features: Feature matrix of shape (n_samples, n_features).
            labels: List of labels of shape (n_samples,).
        """
        # random seed
        self.X = np.array(features)
        self.y = np.array(labels)
        self.class_weights = {0: 1.0, 1: 1.0}  # Example class weights, adjust as needed

    def get_train_test_data(
        self,
    ) -> tuple[np.ndarray, list[np.ndarray], np.ndarray, list[np.ndarray]]:
        """
        Splits the data into training and testing sets.
        Here, we manually split the data.

        Returns:
            A tuple containing:
            - Train data
            - Train labels
            - Test data
            - Test labels
        """
        train_data = np.array([self.X[0], self.X[1], self.X[2]])
        train_labels = [
            np.array([self.y[0]]),
            np.array([self.y[1]]),
            np.array([self.y[2]]),
        ]
        test_data = np.array([self.X[3]])
        test_labels = [np.array([self.y[3]])]
        return train_data, train_labels, test_data, test_labels

    def shuffle_data(
        self, paired_data: list[tuple[np.ndarray, int]]
    ) -> list[tuple[np.ndarray, int]]:
        """
        Shuffles the data randomly.

        Args:
            paired_data: List of tuples containing data and corresponding labels.

        Returns:
            A shuffled list of data-label pairs.
        """
        return paired_data

    def get_inout_dim(self) -> tuple[int, int]:
        train_data, train_labels, test_data, test_labels = self.get_train_test_data()
        in_dim = train_data[0].shape[0]
        out_dim = len(train_labels)
        return in_dim, out_dim

    @staticmethod
    def one_hot_encode(labels: list[int], num_classes: int) -> np.ndarray:
        """
        Perform one-hot encoding for the given labels.

        Args:
            labels: List of integer labels.
            num_classes: Total number of classes for encoding.

        Returns:
            A numpy array representing one-hot encoded labels.
        """
        one_hot = np.zeros((len(labels), num_classes))
        for idx, label in enumerate(labels):
            one_hot[idx, label] = 0.99
        return one_hot


class MLP:
    """
    A custom MLP class for implementing a simple multi-layer perceptron with
    forward propagation, backpropagation.

    Attributes:
        learning_rate (float): Learning rate for gradient descent.
        gamma (float): Parameter to control learning rate adjustment.
        epoch (int): Number of epochs for training.
        hidden_dim (int): Dimension of the hidden layer.
        batch_size (int): Number of samples per mini-batch.
        train_loss (List[float]): List to store training loss for each fold.
        train_accuracy (List[float]): List to store training accuracy for each fold.
        test_loss (List[float]): List to store test loss for each fold.
        test_accuracy (List[float]): List to store test accuracy for each fold.
        dataloader (Dataloader): DataLoader object for handling training data.
        inter_variable (dict): Dictionary to store intermediate variables
        for backpropagation.
        weights1_list (List[Tuple[np.ndarray, np.ndarray]]):
        List of weights for each fold.

    Methods:
        get_inout_dim:obtain input dimension and output dimension.
        relu: Apply the ReLU activation function.
        relu_derivative: Compute the derivative of the ReLU function.
        forward: Perform a forward pass through the network.
        back_prop: Perform backpropagation to compute gradients.
        update_weights: Update the weights using gradients.
        update_learning_rate: Adjust the learning rate based on test accuracy.
        accuracy: Compute accuracy of the model.
        loss: Compute weighted MSE loss.
        train: Train the MLP over multiple folds with early stopping.


    """

    def __init__(
        self,
        dataloader: Dataloader,
        epoch: int,
        learning_rate: float,
        gamma: float = 1.0,
        hidden_dim: int = 2,
    ) -> None:
        self.learning_rate = learning_rate
        self.gamma = gamma  # learning_rate decay hyperparameter gamma
        self.epoch = epoch
        self.hidden_dim = hidden_dim

        self.train_loss: list[float] = []
        self.train_accuracy: list[float] = []
        self.test_loss: list[float] = []
        self.test_accuracy: list[float] = []

        self.dataloader = dataloader
        self.inter_variable: dict[str, np.ndarray] = {}
        self.weights1_list: list[np.ndarray] = []

    def get_inout_dim(self) -> tuple[int, int]:
        """
        obtain input dimension and output dimension.

        :return: Tuple of weights (input_dim, output_dim) for the network.

        >>> X = [[0.0, 0.0], [1.0, 1.0], [1.0, 0.0], [0.0, 1.0]]
        >>> y = [0, 1, 0, 0]
        >>> loader = Dataloader(X, y)
        >>> mlp = MLP(loader, 10, 0.1)
        >>> mlp.get_inout_dim()
        (2, 3)
        """
        input_dim, output_dim = self.dataloader.get_inout_dim()

        return input_dim, output_dim

    def initialize(self) -> tuple[np.ndarray, np.ndarray]:
        """
        Initialize weights using He initialization.

        :return: Tuple of weights (w1, w2) for the network.

        >>> X = [[0.0, 0.0], [1.0, 1.0], [1.0, 0.0], [0.0, 1.0]]
        >>> y = [0, 1, 0, 0]
        >>> loader = Dataloader(X, y)
        >>> mlp = MLP(loader, 10, 0.1)
        >>> w1, w2 = mlp.initialize()
        >>> w1.shape
        (3, 2)
        >>> w2.shape
        (2, 3)
        """

        in_dim, out_dim = self.dataloader.get_inout_dim()
        w1 = rng.standard_normal((in_dim + 1, self.hidden_dim)) * np.sqrt(2.0 / in_dim)
        w2 = rng.standard_normal((self.hidden_dim, out_dim)) * np.sqrt(
            2.0 / self.hidden_dim
        )
        return w1, w2

    def relu(self, input_array: np.ndarray) -> np.ndarray:
        """
        Apply the ReLU activation function element-wise.

        :param input_array: Input array.
        :return: Output array after applying ReLU.

        >>> mlp = MLP(None, 1, 0.1)
        >>> mlp.relu(np.array([[-1, 2], [3, -4]]))
        array([[0, 2],
               [3, 0]])
        """
        return np.maximum(0, input_array)

    def relu_derivative(self, input_array: np.ndarray) -> np.ndarray:
        """
        Compute the derivative of the ReLU function.

        :param input_array: Input array.
        :return: Derivative of ReLU function element-wise.

        >>> mlp = MLP(None, 1, 0.01)
        >>> mlp.relu_derivative(np.array([[-1, 2], [3, -4]]))
        array([[0., 1.],
               [1., 0.]])
        """
        return (input_array > 0).astype(float)

    def forward(
        self,
        input_data: np.ndarray,
        w1: np.ndarray,
        w2: np.ndarray,
        no_gradient: bool = False,
    ) -> np.ndarray:
        """
        Performs a forward pass through the neural network with one hidden layer.

        Args:
            input_data: Input data, shape (batch_size, input_dim).
            w1: Weight matrix for input to hidden layer,
            shape (input_dim + 1, hidden_dim).
            w2: Weight matrix for hidden to output layer,
            shape (hidden_dim, output_dim).
            no_gradient: If True, returns output without storing intermediates.

        Returns:
            Output of the network after forward pass, shape (batch_size, output_dim).

        Examples:
            >>> mlp = MLP(None, 1, 0.1, hidden_dim=2)
            >>> x = np.array([[1.0, 2.0, 1.0]])  # batch_size=1, input_dim=2 + bias
            >>> w1 = np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]])
            >>> w2 = np.array([[0.7, 0.8], [0.9, 1.0]])
            >>> output = mlp.forward(x, w1, w2)
            >>> output.shape
            (1, 2)
        """
        z1 = np.dot(input_data, w1)

        a1 = self.relu(z1)  # relu

        # hidden → output
        z2 = np.dot(a1, w2)
        a2 = z2

        if no_gradient:
            # when predict
            return a2
        else:
            # when training
            self.inter_variable = {"z1": z1, "a1": a1, "z2": z2, "a2": a2}
            return a2

    def back_prop(
        self, input_data: np.ndarray, true_labels: np.ndarray, w2: np.ndarray
    ) -> tuple[np.ndarray, np.ndarray]:
        """
        Performs backpropagation to compute gradients for the weights.

        Args:
            input_data: Input data, shape (batch_size, input_dim).
            true_labels: True labels, shape (batch_size, output_dim).
            w2: Weight matrix for hidden to output layer,
            shape (hidden_dim, output_dim).

        Returns:
            Tuple of gradients (grad_w1, grad_w2) for the weight matrices.
        Examples:
            >>> mlp = MLP(None, 1, 0.1, hidden_dim=2)
            >>> x = np.array([[1.0, 2.0, 1.0]])  # batch_size=1, input_dim=2 + bias
            >>> y = np.array([[0.0, 1.0]])  # batch_size=1, output_dim=2
            >>> w1 = np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]])
            >>> w2 = np.array([[0.7, 0.8], [0.9, 1.0]])  # (hidden_dim=2, output_dim=2)
            >>> _ = mlp.forward(x, w1, w2)  # Run forward to set inter_variable
            >>> grad_w1, grad_w2 = mlp.back_prop(x, y, w2)
            >>> grad_w1.shape
            (3, 2)
            >>> grad_w2.shape
            (2, 2)
        """
        a1 = self.inter_variable["a1"]  # (batch_size, hidden_dim)
        z1 = self.inter_variable["z1"]
        a2 = self.inter_variable["a2"]  # (batch_size, output_dim)

        batch_size = input_data.shape[0]

        # 1. output layer error
        delta_k = a2 - true_labels
        delta_j = np.dot(delta_k, w2.T) * self.relu_derivative(
            z1
        )  # (batch, hidden_dim) 使用relu时

        grad_w2 = (
            np.dot(a1.T, delta_k) / batch_size
        )  # (hidden, batch).dot(batch, output) = (hidden, output)
        input_data_flat = input_data.reshape(input_data.shape[0], -1)
        grad_w1 = (
            np.dot(input_data_flat.T, delta_j) / batch_size
        )  # (input_dim, batch_size).dot(batch, hidden) = (input, hidden)

        return grad_w1, grad_w2

    def update_weights(
        self,
        w1: np.ndarray,
        w2: np.ndarray,
        grad_w1: np.ndarray,
        grad_w2: np.ndarray,
        learning_rate: float,
    ) -> tuple[np.ndarray, np.ndarray]:
        """
        Updates the weight matrices using the computed gradients and learning rate.

        Args:
            w1: Weight matrix for input to hidden layer,
            shape (input_dim + 1, hidden_dim).
            w2: Weight matrix for hidden to output layer,
            shape (hidden_dim, output_dim).
            grad_w1: Gradient for w1,
            shape (input_dim + 1, hidden_dim).
            grad_w2: Gradient for w2,
            shape (hidden_dim, output_dim).
            learning_rate: Learning rate for weight updates.

        Returns:
            Updated weight matrices (w1, w2).

        Examples:
            >>> mlp = MLP(None, 1, 0.1)
            >>> w1 = np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]])
            >>> w2 = np.array([[0.7, 0.8], [0.9, 1.0]])
            >>> grad_w1 = np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]])
            >>> grad_w2 = np.array([[0.7, 0.8], [0.9, 1.0]])
            >>> lr = 0.1
            >>> new_w1, new_w2 = mlp.update_weights(w1, w2, grad_w1, grad_w2, lr)
            >>> new_w1==np.array([[0.09, 0.18], [0.27, 0.36], [0.45, 0.54]])
            array([[ True,  True],
                   [ True,  True],
                   [ True,  True]])
            >>> new_w2==np.array([[0.63, 0.72], [0.81, 0.90]])
            array([[ True,  True],
                   [ True,  True]])
        """
        w1 -= learning_rate * grad_w1
        w2 -= learning_rate * grad_w2
        return w1, w2

    def update_learning_rate(self, learning_rate: float) -> float:
        """
        Updates the learning rate by applying the decay factor gamma.

        Args:
            learning_rate: Current learning rate.

        Returns:
            Updated learning rate.

        Examples:
            >>> mlp = MLP(None, 1, 0.1, gamma=0.9)
            >>> round(mlp.update_learning_rate(0.1), 2)
            0.09
        """

        return learning_rate * self.gamma

    @staticmethod
    def accuracy(label: np.ndarray, y_hat: np.ndarray) -> float:
        """
        Computes the accuracy of predictions by comparing predicted and true labels.

        Args:
            label: True labels, shape (batch_size, num_classes).
            y_hat: Predicted outputs, shape (batch_size, num_classes).

        Returns:
            Accuracy as a float between 0 and 1.

        Examples:
            >>> mlp = MLP(None, 1, 0.01)
            >>> label = np.array([[1, 0], [0, 1], [1, 0]])
            >>> y_hat = np.array([[0.9, 0.1], [0.2, 0.8], [0.6, 0.4]])
            >>> mlp.accuracy(label, y_hat)
            np.float64(1.0)
        """
        return (y_hat.argmax(axis=1) == label.argmax(axis=1)).mean()

    @staticmethod
    def loss(output: np.ndarray, label: np.ndarray) -> float:
        """
        Computes the mean squared error loss between predictions and true labels.

        Args:
            output: Predicted outputs, shape (batch_size, num_classes).
            label: True labels, shape (batch_size, num_classes).

        Returns:
            Mean squared error loss as a float.

        Examples:
            >>> mlp = MLP(None, 1, 0.1)
            >>> output = np.array([[0.9, 0.1], [0.2, 0.8]])
            >>> label = np.array([[1.0, 0.0], [0.0, 1.0]])
            >>> round(mlp.loss(output, label), 3)
            np.float64(0.025)
        """
        return np.sum((output - label) ** 2) / (2 * label.shape[0])

    def get_acc_loss(self) -> tuple[list[float], list[float]]:
        """
        Returns the recorded test accuracy and test loss.

        Returns:
            Tuple of (test_accuracy, test_loss) lists.

        Examples:
            >>> mlp = MLP(None, 1, 0.1)
            >>> mlp.test_accuracy = [0.8, 0.9]
            >>> mlp.test_loss = [0.1, 0.05]
            >>> acc, loss = mlp.get_acc_loss()
            >>> acc
            [0.8, 0.9]
            >>> loss
            [0.1, 0.05]
        """
        return self.test_accuracy, self.test_loss

    def train(self) -> None:
        """
        Trains the MLP model using the provided dataloader
        for multiple folds and epochs.

        Saves the best model parameters for each fold and records accuracy/loss.

        Examples:
            >>> X = [[0.0, 0.0], [1.0, 1.0], [1.0, 0.0], [0.0, 1.0]]
            >>> y = [0, 1, 0, 0]
            >>> loader = Dataloader(X, y)
            >>> mlp = MLP(loader, epoch=2, learning_rate=0.1, hidden_dim=2)
            >>> mlp.train() # doctest: +ELLIPSIS
            Test accuracy: ...
        """

        learning_rate = self.learning_rate
        train_data, train_labels, test_data, test_labels = (
            self.dataloader.get_train_test_data()
        )

        train_data = np.c_[train_data, np.ones(train_data.shape[0])]
        test_data = np.c_[test_data, np.ones(test_data.shape[0])]

        _, total_label_num = self.dataloader.get_inout_dim()

        train_labels = self.dataloader.one_hot_encode(train_labels, total_label_num)
        test_labels = self.dataloader.one_hot_encode(test_labels, total_label_num)

        w1, w2 = self.initialize()

        test_accuracy_list: list[float] = []
        test_loss_list: list[float] = []

        batch_size = 1

        for _j in range(self.epoch):
            for k in range(0, train_data.shape[0], batch_size):  # retrieve every image
                batch_imgs = train_data[k : k + batch_size]
                batch_labels = train_labels[k : k + batch_size]

                self.forward(input_data=batch_imgs, w1=w1, w2=w2, no_gradient=False)

                grad_w1, grad_w2 = self.back_prop(
                    input_data=batch_imgs, true_labels=batch_labels, w2=w2
                )

                w1, w2 = self.update_weights(w1, w2, grad_w1, grad_w2, learning_rate)

            test_output = self.forward(test_data, w1, w2, no_gradient=True)
            test_accuracy = self.accuracy(test_labels, test_output)
            test_loss = self.loss(test_output, test_labels)

            test_accuracy_list.append(test_accuracy)
            test_loss_list.append(test_loss)

            learning_rate = self.update_learning_rate(learning_rate)

        self.test_accuracy = test_accuracy_list
        self.test_loss = test_loss_list
        print("Test accuracy:", sum(test_accuracy_list) / len(test_accuracy_list))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
