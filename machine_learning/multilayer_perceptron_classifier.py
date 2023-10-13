import numpy as np


class MLP:
    """Multi-Layer Perceptron model.

    Attributes:
        num_inputs (int): Number of input features
        num_hidden (int): Number of neurons in the hidden layer
        num_outputs (int): Number of output classes
        w1 (numpy array): Weights from inputs to the hidden layer
        b1 (numpy array): Biases for the hidden layer
        w2 (numpy array): Weights from the hidden layer to outputs
        b2 (numpy array): Biases for the output layer

    Examples:
        # Create an MLP model with 2 input features, 3 hidden neurons, and 1 out class
        >>> mlp = MLP(2, 3, 1)
        # Forward pass using the model with a batch of input data
        >>> x = np.array([[1.0, 2.0]])
        >>> y_pred = mlp.forward(x)
        # Training the model using backpropagation
        >>> x_train = np.array([[1.0, 2.0], [3.0, 4.0]])
        >>> y_train = np.array([[0.0], [1.0]])
        >>> mlp.fit(x_train, y_train, epochs=100, learning_rate=0.01)
    """

    def __init__(self, num_inputs, num_hidden, num_outputs):
        """Initialize the model.

        Args:
            num_inputs (int): Number of input features
            num_hidden (int): Number of neurons in the hidden layer
            num_outputs (int): Number of output classes
        """
        self.w1 = np.random.randn(num_inputs, num_hidden)
        self.b1 = np.zeros(num_hidden)
        self.w2 = np.random.randn(num_hidden, num_outputs)
        self.b2 = np.zeros(num_outputs)

    def forward(self, x):
        """Perform the forward pass.

        Args:
            x (numpy array): Batch of input data

        Returns:
            y_pred (numpy array): The predicted outputs

        Examples:
            >>> mlp = MLP(2, 3, 1)
            >>> x = np.array([[1.0, 2.0]])
            >>> y_pred = mlp.forward(x)
        """
        # Hidden layer
        self.z1 = np.dot(x, self.w1) + self.b1
        self.a1 = np.tanh(self.z1)

        # Output layer
        self.z2 = np.dot(self.a1, self.w2) + self.b2
        y_pred = self.z2

        return y_pred

    def fit(self, x, y, epochs=100, learning_rate=0.01):
        """Train the model using backpropagation.

        Args:
            x (numpy array): Training data
            y (numpy array): Target classes
            epochs (int): Number of training epochs
            learning_rate (float): Learning rate for gradient descent

        Examples:
            >>> mlp = MLP(2, 3, 1)
            >>> x_train = np.array([[1.0, 2.0], [3.0, 4.0]])
            >>> y_train = np.array([[0.0], [1.0]])
            >>> mlp.fit(X_train, y_train, epochs=100, learning_rate=0.01)
        """
        for epoch in range(epochs):
            # Forward pass
            y_pred = self.forward(x)

            # Compute loss
            loss = np.mean((y_pred - y) ** 2)

            # Backpropagation
            dl_dypred = 2 * (y_pred - y)
            dl_dz2 = dl_dypred
            dl_dw2 = np.dot(self.a1.T, dl_dz2)
            dl_db2 = np.sum(dl_dz2, axis=0)

            dl_da1 = np.dot(dl_dz2, self.w2.T)
            dl_dz1 = dl_da1 * (1 - np.power(self.a1, 2))
            dl_dw1 = np.dot(x.T, dl_dz1)
            dl_db1 = np.sum(dl_dz1, axis=0)

            # Update weights and biases
            self.w1 -= learning_rate * dl_dw1
            self.b1 -= learning_rate * dl_db1
            self.w2 -= learning_rate * dl_dw2
            self.b2 -= learning_rate * dl_db2

    doctest.testmod()
