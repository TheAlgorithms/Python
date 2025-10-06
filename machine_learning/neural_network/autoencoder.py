import numpy as np

# Simple Autoencoder for dimensionality reduction
class Autoencoder:
    def __init__(self, input_dim, hidden_dim):
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        # Encoder weights
        self.W_enc = np.random.randn(hidden_dim, input_dim) * 0.1
        self.b_enc = np.zeros((hidden_dim, 1))
        # Decoder weights
        self.W_dec = np.random.randn(input_dim, hidden_dim) * 0.1
        self.b_dec = np.zeros((input_dim, 1))

    def encode(self, x):
        # x: (input_dim, 1)
        return np.tanh(self.W_enc @ x + self.b_enc)

    def decode(self, h):
        # h: (hidden_dim, 1)
        return np.tanh(self.W_dec @ h + self.b_dec)

    def forward(self, x):
        # x: (input_dim, 1)
        h = self.encode(x)
        x_recon = self.decode(h)
        return x_recon
