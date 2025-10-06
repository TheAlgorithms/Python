import numpy as np

# Gated Recurrent Unit (GRU) implementation for sequence modeling
class GRU:
    def __init__(self, input_size, hidden_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        # Initialize weights
        self.Wz = np.random.randn(hidden_size, input_size)
        self.Uz = np.random.randn(hidden_size, hidden_size)
        self.bz = np.zeros((hidden_size, 1))
        self.Wr = np.random.randn(hidden_size, input_size)
        self.Ur = np.random.randn(hidden_size, hidden_size)
        self.br = np.zeros((hidden_size, 1))
        self.Wh = np.random.randn(hidden_size, input_size)
        self.Uh = np.random.randn(hidden_size, hidden_size)
        self.bh = np.zeros((hidden_size, 1))

    def step(self, x, h_prev):
        # x: (input_size, 1), h_prev: (hidden_size, 1)
        z = self._sigmoid(self.Wz @ x + self.Uz @ h_prev + self.bz)
        r = self._sigmoid(self.Wr @ x + self.Ur @ h_prev + self.br)
        h_hat = np.tanh(self.Wh @ x + self.Uh @ (r * h_prev) + self.bh)
        h = (1 - z) * h_prev + z * h_hat
        return h

    def forward(self, X):
        # X: (seq_len, input_size)
        h = np.zeros((self.hidden_size, 1))
        for t in range(X.shape[0]):
            x = X[t].reshape(-1, 1)
            h = self.step(x, h)
        return h

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
