"""
- - - - - -- - - - - - - - - - - - - - - - - - - - - - -
Name - - Deep Belief Network (DBN) Using Restricted Boltzmann Machines (RBMs)
Goal - - Unsupervised layer-wise feature learning and pretraining for deep neural networks
Detail: Multi-layer DBN constructed by stacking RBMs trained via contrastive divergence.
        Implements Gibbs sampling for binary units, manual weight updates with NumPy.
        Developed for Intrusion Detection System (IDS) in WiFi networks.
        This implementation is written entirely in pure NumPy, with no deep learning frameworks.
        Can be extended for fine-tuning deep neural networks.

Author: Adhithya Laxman Ravi Shankar Geetha 
GitHub: https://github.com/Adhithya-Laxman/
Date: 2025.10.21
- - - - - -- - - - - - - - - - - - - - - - - - - - - - -
"""

import numpy as np
import matplotlib.pyplot as plt


class RBM:
    def __init__(self, n_visible, n_hidden, learning_rate=0.01, k=1, epochs=10, batch_size=64, mode='bernoulli'):
        """
        Initialize an RBM.

        Args:
            n_visible (int): Number of visible units.
            n_hidden (int): Number of hidden units.
            learning_rate (float): Learning rate for weight updates.
            k (int): Number of Gibbs sampling steps.
            epochs (int): Number of training epochs.
            batch_size (int): Batch size.
            mode (str): Sampling mode ('bernoulli' or 'gaussian').
        """
        self.n_visible = n_visible
        self.n_hidden = n_hidden
        self.learning_rate = learning_rate
        self.k = k
        self.epochs = epochs
        self.batch_size = batch_size
        self.mode = mode

        # Initialize weights and biases
        self.weights = np.random.normal(0, 0.01, (n_visible, n_hidden))
        self.hidden_bias = np.zeros(n_hidden)
        self.visible_bias = np.zeros(n_visible)

    def sigmoid(self, x):
        """
        Compute the sigmoid activation function.

        Args:
            x (np.ndarray): Input array.

        Returns:
            np.ndarray: Sigmoid of input.
        """
        return 1.0 / (1.0 + np.exp(-x))

    def sample_prob(self, probs):
        """
        Sample binary states from given probabilities.

        Args:
            probs (np.ndarray): Probabilities of activation.

        Returns:
            np.ndarray: Sampled binary values.
        """
        return (np.random.rand(*probs.shape) < probs).astype(float)

    def sample_hidden_given_visible(self, v):
        """
        Sample hidden units conditioned on visible units.

        Args:
            v (np.ndarray): Visible units.

        Returns:
            tuple: (hidden probabilities, hidden samples)
        """
        hid_probs = self.sigmoid(np.dot(v, self.weights) + self.hidden_bias)
        hid_samples = self.sample_prob(hid_probs)
        return hid_probs, hid_samples

    def sample_visible_given_hidden(self, h):
        """
        Sample visible units conditioned on hidden units.

        Args:
            h (np.ndarray): Hidden units.

        Returns:
            tuple: (visible probabilities, visible samples)
        """
        vis_probs = self.sigmoid(np.dot(h, self.weights.T) + self.visible_bias)
        vis_samples = self.sample_prob(vis_probs)
        return vis_probs, vis_samples

    def contrastive_divergence(self, v0):
        """
        Perform Contrastive Divergence (CD-k) step.

        Args:
            v0 (np.ndarray): Initial visible units (data batch).

        Returns:
            float: Reconstruction loss for the batch.
        """
        h_probs0, h0 = self.sample_hidden_given_visible(v0)
        vk, hk = v0, h0

        for _ in range(self.k):
            v_probs, vk = self.sample_visible_given_hidden(hk)
            h_probs, hk = self.sample_hidden_given_visible(vk)

        # Compute gradients
        positive_grad = np.dot(v0.T, h_probs0)
        negative_grad = np.dot(vk.T, h_probs)

        # Update weights and biases
        self.weights += self.learning_rate * (positive_grad - negative_grad) / v0.shape[0]
        self.visible_bias += self.learning_rate * np.mean(v0 - vk, axis=0)
        self.hidden_bias += self.learning_rate * np.mean(h_probs0 - h_probs, axis=0)

        loss = np.mean((v0 - vk) ** 2)
        return loss

    def train(self, data):
        """
        Train the RBM on given data.

        Args:
            data (np.ndarray): Training data matrix.
        """
        n_samples = data.shape[0]
        for epoch in range(self.epochs):
            np.random.shuffle(data)
            losses = []

            for i in range(0, n_samples, self.batch_size):
                batch = data[i:i + self.batch_size]
                loss = self.contrastive_divergence(batch)
                losses.append(loss)

            print(f"Epoch [{epoch + 1}/{self.epochs}] avg loss: {np.mean(losses):.6f}")


class DeepBeliefNetwork:
    def __init__(self, input_size, layers, mode='bernoulli', k=5, save_path=None):
        """
        Initialize a Deep Belief Network.

        Args:
            input_size (int): Number of input features.
            layers (list): List of hidden layer sizes.
            mode (str): Sampling mode ('bernoulli' or 'gaussian').
            k (int): Number of sampling steps in generate_input_for_layer.
            save_path (str): Path to save trained parameters.
        """
        self.input_size = input_size
        self.layers = layers
        self.k = k
        self.mode = mode
        self.save_path = save_path
        self.layer_params = [{'W': None, 'hb': None, 'vb': None} for _ in layers]

    def sigmoid(self, x):
        """
        Sigmoid activation function.

        Args:
            x (np.ndarray): Input array.

        Returns:
            np.ndarray: Sigmoid output.
        """
        return 1.0 / (1.0 + np.exp(-x))

    def sample_prob(self, probs):
        """
        Sample binary states from probabilities.

        Args:
            probs (np.ndarray): Probabilities.

        Returns:
            np.ndarray: Binary samples.
        """
        return (np.random.rand(*probs.shape) < probs).astype(float)

    def sample_h(self, x, W, hb):
        """
        Sample hidden units given visible units.

        Args:
            x (np.ndarray): Visible units.
            W (np.ndarray): Weight matrix.
            hb (np.ndarray): Hidden biases.

        Returns:
            tuple: (hidden probabilities, hidden samples)
        """
        probs = self.sigmoid(np.dot(x, W) + hb)
        samples = self.sample_prob(probs)
        return probs, samples

    def sample_v(self, y, W, vb):
        """
        Sample visible units given hidden units.

        Args:
            y (np.ndarray): Hidden units.
            W (np.ndarray): Weight matrix.
            vb (np.ndarray): Visible biases.

        Returns:
            tuple: (visible probabilities, visible samples)
        """
        probs = self.sigmoid(np.dot(y, W.T) + vb)
        samples = self.sample_prob(probs)
        return probs, samples

    def generate_input_for_layer(self, layer_index, x):
        """
        Generate smoothed input for a layer by stacking and averaging samples.

        Args:
            layer_index (int): Index of the current layer.
            x (np.ndarray): Input data.

        Returns:
            np.ndarray: Smoothed input for the layer.
        """
        if layer_index == 0:
            return x.copy()
        samples = []
        for _ in range(self.k):
            x_dash = x.copy()
            for i in range(layer_index):
                _, x_dash = self.sample_h(x_dash, self.layer_params[i]['W'], self.layer_params[i]['hb'])
            samples.append(x_dash)
        return np.mean(np.stack(samples, axis=0), axis=0)

    def train_dbn(self, x):
        """
        Train the DBN layer-wise.

        Args:
            x (np.ndarray): Training data.
        """
        for idx, layer_size in enumerate(self.layers):
            n_visible = self.input_size if idx == 0 else self.layers[idx - 1]
            n_hidden = layer_size

            rbm = RBM(n_visible, n_hidden, k=5, epochs=300)
            x_input = self.generate_input_for_layer(idx, x)
            rbm.train(x_input)
            self.layer_params[idx]['W'] = rbm.weights
            self.layer_params[idx]['hb'] = rbm.hidden_bias
            self.layer_params[idx]['vb'] = rbm.visible_bias
            print(f"Finished training layer {idx + 1}/{len(self.layers)}")

    def reconstruct(self, x):
        """
        Reconstruct input data through forward and backward sampling.

        Args:
            x (np.ndarray): Input data.

        Returns:
            tuple: (encoded representation, reconstructed input, reconstruction error)
        """
        # Forward pass
        h = x.copy()
        for i in range(len(self.layer_params)):
            _, h = self.sample_h(h, self.layer_params[i]['W'], self.layer_params[i]['hb'])
        encoded = h.copy()

        # Backward pass
        for i in reversed(range(len(self.layer_params))):
            _, h = self.sample_v(h, self.layer_params[i]['W'], self.layer_params[i]['vb'])
        reconstructed = h

        # Compute reconstruction error (Mean Squared Error)
        error = np.mean((x - reconstructed) ** 2)
        print(f"Reconstruction error: {error:.6f}")

        return encoded, reconstructed, error

# Usage example
if __name__ == "__main__":
    # Generate synthetic dataset
    data = np.random.randint(0, 2, (100, 16)).astype(float)

    # Initialize DBN
    dbn = DeepBeliefNetwork(input_size=16, layers=[16, 8, 4])

    # Train DBN
    dbn.train_dbn(data)

    # Reconstruct
    encoded, reconstructed, error = dbn.reconstruct(data[:5])
    print("Encoded shape:", encoded.shape)
    print("Reconstructed shape:", reconstructed.shape)
    # Visualization of original vs reconstructed samples
    features_to_show = 16  # Show only the first 20 features
    plt.figure(figsize=(12, 5))
    for i in range(5):
        plt.subplot(2, 5, i + 1)
        plt.title(f"Original {i+1}")
        plt.imshow(data[i][:features_to_show].reshape(1, -1), cmap='gray', aspect='auto', interpolation='nearest')
        plt.axis('off')

        plt.subplot(2, 5, i + 6)
        plt.title(f"Reconstructed {i+1}")
        plt.imshow(reconstructed[i][:features_to_show].reshape(1, -1), cmap='gray', aspect='auto', interpolation='nearest')
        plt.axis('off')
    plt.suptitle(f"DBN Reconstruction (First {features_to_show} Features, MSE: {error:.6f})")
    plt.tight_layout()
    plt.savefig('reconstruction_subset.png')
    print("Subset reconstruction plot saved as 'reconstruction_subset.png'")
