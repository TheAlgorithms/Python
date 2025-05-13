import numpy as np
from tqdm import tqdm
from typing import Tuple, List
class Dataloader:
    """
    DataLoader class for handling dataset, including data shuffling, one-hot encoding, and train-test splitting.

    Example usage:
    >>> X = [[0.0, 0.0], [1.0, 1.0], [1.0, 0.0], [0.0, 1.0]]
    >>> y = [0, 1, 0, 0]
    >>> loader = Dataloader(X, y)
    >>> loader.get_Train_test_data()  # Returns train and test data
    (array([[0., 0.],
           [1., 1.],
           [1., 0.]]), [array([0]), array([1]), array([0])], array([[0., 1.]]), [array([0])])
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

    def __init__(self, X: List[List[float]], y: List[int]) -> None:
        """
        Initializes the Dataloader instance with feature matrix X and labels y.

        Args:
            X: Feature matrix of shape (n_samples, n_features).
            y: List of labels of shape (n_samples,).
        """
        # random seed
        np.random.seed(42)

        self.X = np.array(X)
        self.y = np.array(y)
        self.class_weights = {0: 1.0, 1: 1.0}  # Example class weights, adjust as needed

    def get_Train_test_data(self) -> Tuple[List[np.ndarray], List[np.ndarray], List[np.ndarray], List[np.ndarray]]:
        """
        Splits the data into training and testing sets. Here, we manually split the data.

        Returns:
            A tuple containing:
            - Train data
            - Train labels
            - Test data
            - Test labels
        """
        # Manually splitting data into training and testing sets
        train_data = np.array([self.X[0], self.X[1], self.X[2]])  # First 3 samples for training
        train_labels = [np.array([self.y[0]]), np.array([self.y[1]]), np.array([self.y[2]])] # Labels as np.ndarray
        test_data = np.array([self.X[3]])  # Last sample for testing
        test_labels = [np.array([self.y[3]])]  # Labels as np.ndarray
        return train_data, train_labels, test_data, test_labels

    def shuffle_data(self, paired_data: List[Tuple[np.ndarray, int]]) -> List[Tuple[np.ndarray, int]]:
        """
        Shuffles the data randomly.

        Args:
            paired_data: List of tuples containing data and corresponding labels.

        Returns:
            A shuffled list of data-label pairs.
        """
        np.random.shuffle(paired_data)
        return paired_data

    def get_inout_dim(self) -> Tuple[int, int]:
        train_data, train_labels, test_data, test_labels = self.get_Train_test_data()
        in_dim = train_data[0].shape[0]
        out_dim = len(train_labels)
        return in_dim, out_dim

    @staticmethod
    def one_hot_encode(labels, num_classes):
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


class MLP():
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
            inter_variable (dict): Dictionary to store intermediate variables for backpropagation.
            weights1_list (List[Tuple[np.ndarray, np.ndarray]]): List of weights for each fold.
            best_accuracy (float): Best test accuracy achieved.
            patience (int): Patience for early stopping.
            epochs_no_improve (int): Counter for epochs without improvement.

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
    def __init__(self, dataloader, epoch: int, learning_rate: float, gamma=1, hidden_dim=2):
        self.learning_rate = learning_rate  #
        self.gamma = gamma  # learning_rate decay hyperparameter gamma
        self.epoch = epoch
        self.hidden_dim = hidden_dim

        self.train_loss = []
        self.train_accuracy = []
        self.test_loss = []
        self.test_accuracy = []

        self.dataloader = dataloader
        self.inter_variable = {}
        self.weights1_list = []

    def get_inout_dim(self):
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

    def initialize(self):
        """
        Initialize weights using He initialization.

        :return: Tuple of weights (W1, W2) for the network.

        >>> X = [[0.0, 0.0], [1.0, 1.0], [1.0, 0.0], [0.0, 1.0]]
        >>> y = [0, 1, 0, 0]
        >>> loader = Dataloader(X, y)
        >>> mlp = MLP(loader, 10, 0.1)
        >>> W1, W2 = mlp.initialize()
        >>> W1.shape
        (3, 2)
        >>> W2.shape
        (2, 3)
        """

        in_dim, out_dim = self.dataloader.get_inout_dim()  # in_dim here is image dim
        W1 = np.random.randn(in_dim + 1, self.hidden_dim) * 0.01  # (in_dim, hidden)

        W2 = np.random.randn(self.hidden_dim, out_dim) * 0.01  # (hidden, output)
        return W1, W2

    def relu(self, z):
        """
        Apply the ReLU activation function element-wise.

        :param z: Input array.
        :return: Output array after applying ReLU.

        >>> mlp = MLP(None, 1, 0.1)
        >>> mlp.relu(np.array([[-1, 2], [3, -4]]))
        array([[0, 2],
               [3, 0]])
        """
        return np.maximum(0, z)

    def relu_derivative(self, z):
        """
        Compute the derivative of the ReLU function.

        :param z: Input array.
        :return: Derivative of ReLU function element-wise.

        >>> mlp = MLP(None, 1, 0.01)
        >>> mlp.relu_derivative(np.array([[-1, 2], [3, -4]]))
        array([[0., 1.],
               [1., 0.]])
        """
        return (z > 0).astype(float)


    def forward(self, x, W1, W2, no_gradient=False):

        """
        Performs a forward pass through the neural network with one hidden layer.

        Args:
            x: Input data, shape (batch_size, input_dim).
            W1: Weight matrix for input to hidden layer, shape (input_dim + 1, hidden_dim).
            W2: Weight matrix for hidden to output layer, shape (hidden_dim, output_dim).
            no_gradient: If True, returns output without storing intermediates.

        Returns:
            Output of the network after forward pass, shape (batch_size, output_dim).

        Examples:
            >>> mlp = MLP(None, 1, 0.1, hidden_dim=2)
            >>> x = np.array([[1.0, 2.0, 1.0]])  # batch_size=1, input_dim=2 + bias
            >>> W1 = np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]])  # (input_dim=3, hidden_dim=2)
            >>> W2 = np.array([[0.7, 0.8], [0.9, 1.0]])  # (hidden_dim=2, output_dim=2)
            >>> output = mlp.forward(x, W1, W2)
            >>> output.shape
            (1, 2)
        """

        z1 = np.dot(x, W1)

        a1 = self.relu(z1)  # relu

        # hidden → output
        z2 = np.dot(a1, W2)
        a2 = z2


        if no_gradient:
            # when predict
            return a2
        else:
            # when training
            self.inter_variable = {
                "z1": z1, "a1": a1,
                "z2": z2, "a2": a2
            }
            return a2

    def back_prop(self, x, y, W1, W2):
        """
         Performs backpropagation to compute gradients for the weights.

         Args:
             x: Input data, shape (batch_size, input_dim).
             y: True labels, shape (batch_size, output_dim).
             W1: Weight matrix for input to hidden layer, shape (input_dim + 1, hidden_dim).
             W2: Weight matrix for hidden to output layer, shape (hidden_dim, output_dim).

         Returns:
             Tuple of gradients (grad_W1, grad_W2) for the weight matrices.

         Examples:
             >>> mlp = MLP(None, 1, 0.1, hidden_dim=2)
             >>> x = np.array([[1.0, 2.0, 1.0]])  # batch_size=1, input_dim=2 + bias
             >>> y = np.array([[0.0, 1.0]])  # batch_size=1, output_dim=2
             >>> W1 = np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]])  # (input_dim=3, hidden_dim=2)
             >>> W2 = np.array([[0.7, 0.8], [0.9, 1.0]])  # (hidden_dim=2, output_dim=2)
             >>> _ = mlp.forward(x, W1, W2)  # Run forward to set inter_variable
             >>> grad_W1, grad_W2 = mlp.back_prop(x, y, W1, W2)
             >>> grad_W1.shape
             (3, 2)
             >>> grad_W2.shape
             (2, 2)
         """


        a1 = self.inter_variable["a1"]  # (batch_size, hidden_dim)
        z1 = self.inter_variable["z1"]
        a2 = self.inter_variable["a2"]  # (batch_size, output_dim)
        z2 = self.inter_variable["z2"]

        batch_size = x.shape[0]

        # 1. output layer error
        delta_k = a2 - y
        delta_j = np.dot(delta_k, W2.T) * self.relu_derivative(z1)  # (batch, hidden_dim) 使用relu时


        grad_w2 = np.dot(a1.T, delta_k) / batch_size  # (hidden, batch).dot(batch, output) = (hidden, output)
        x_flat = x.reshape(x.shape[0], -1)  # (batch_size, input_dim)
        grad_w1 = np.dot(x_flat.T, delta_j) / batch_size  # (input_dim, batch_size).dot(batch, hidden) = (input, hidden)


        return grad_w1, grad_w2

    def update_weights(self, W1, W2, grad_W1, grad_W2, learning_rate):
        """
        Updates the weight matrices using the computed gradients and learning rate.

        Args:
            W1: Weight matrix for input to hidden layer, shape (input_dim + 1, hidden_dim).
            W2: Weight matrix for hidden to output layer, shape (hidden_dim, output_dim).
            grad_W1: Gradient for W1, shape (input_dim + 1, hidden_dim).
            grad_W2: Gradient for W2, shape (hidden_dim, output_dim).
            learning_rate: Learning rate for weight updates.

        Returns:
            Updated weight matrices (W1, W2).

        Examples:
            >>> mlp = MLP(None, 1, 0.1)
            >>> W1 = np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]])  # (input_dim=3, hidden_dim=2)
            >>> W2 = np.array([[0.7, 0.8], [0.9, 1.0]])  # (hidden_dim=2, output_dim=2)
            >>> grad_W1 = np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]])
            >>> grad_W2 = np.array([[0.7, 0.8], [0.9, 1.0]])
            >>> learning_rate = 0.1
            >>> new_W1, new_W2 = mlp.update_weights(W1, W2, grad_W1, grad_W2, learning_rate)
            >>> new_W1==np.array([[0.09, 0.18], [0.27, 0.36], [0.45, 0.54]])
            array([[ True,  True],
                   [ True,  True],
                   [ True,  True]])
            >>> new_W2==np.array([[0.63, 0.72], [0.81, 0.90]])
            array([[ True,  True],
                   [ True,  True]])
        """
        W1 -= learning_rate * grad_W1
        W2 -= learning_rate * grad_W2
        return W1, W2

    def update_learning_rate(self, learning_rate):
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
    def accuracy(label, y_hat):
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
            1.0
        """
        return (y_hat.argmax(axis=1) == label.argmax(axis=1)).mean()

    @staticmethod
    def loss(output, label):
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
            0.025
        """
        return np.sum((output - label) ** 2) / (2 * label.shape[0])

    def get_acc_loss(self):
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

    def train(self):
        """
        Trains the MLP model using the provided dataloader for multiple folds and epochs.

        Saves the best model parameters for each fold and records accuracy/loss.

        Examples:
            >>> X = [[0.0, 0.0], [1.0, 1.0], [1.0, 0.0], [0.0, 1.0]]
            >>> y = [0, 1, 0, 0]
            >>> loader = Dataloader(X, y)
            >>> mlp = MLP(loader, epoch=10, learning_rate=0.1, hidden_dim=2)
            >>> mlp.train()
            Test accuracy: 1.0
        """

        learning_rate = self.learning_rate
        train_data, train_labels, test_data, test_labels = self.dataloader.get_Train_test_data()

        train_data = np.c_[train_data, np.ones(train_data.shape[0])]
        test_data = np.c_[test_data, np.ones(test_data.shape[0])]


        _, total_label_num = self.dataloader.get_inout_dim()

        train_labels = self.dataloader.one_hot_encode(train_labels, total_label_num)
        test_labels = self.dataloader.one_hot_encode(test_labels, total_label_num)

        W1, W2 = self.initialize()

        train_accuracy_list, train_loss_list = [], []
        test_accuracy_list, test_loss_list = [], []

        batch_size = 1

        for j in tqdm(range(self.epoch)):
            for k in range(0, train_data.shape[0], batch_size):  # retrieve every image

                batch_imgs = train_data[k: k + batch_size]
                batch_labels = train_labels[k: k + batch_size]

                output = self.forward(x=batch_imgs, W1=W1, W2=W2, no_gradient=False)

                grad_W1, grad_W2 = self.back_prop(x=batch_imgs, y=batch_labels, W1=W1, W2=W2)

                W1, W2 = self.update_weights(W1, W2, grad_W1, grad_W2, learning_rate)

            test_output = self.forward(test_data, W1, W2, no_gradient=True)
            test_accuracy = self.accuracy(test_labels, test_output)
            test_loss = self.loss(test_output, test_labels)

            test_accuracy_list.append(test_accuracy)
            test_loss_list.append(test_loss)

            learning_rate = self.update_learning_rate(learning_rate)

        self.test_accuracy = test_accuracy_list
        self.test_loss = test_loss_list
        print(f"Test accuracy:", sum(test_accuracy_list)/len(test_accuracy_list))


