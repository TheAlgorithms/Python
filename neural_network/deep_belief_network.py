"""
- - - - - -- - - - - - - - - - - - - - - - - - - - - - -
Name - - Deep Belief Network (DBN) Using Restricted Boltzmann Machines (RBMs)
Goal - - Unsupervised layer-wise feature learning and pretraining
         for deep neural networks
Detail: Multi-layer DBN constructed by stacking RBMs trained via contrastive divergence.
        Implements Gibbs sampling for binary units, manual weight updates with NumPy.
        Developed for Intrusion Detection System (IDS) in WiFi networks.
        This implementation is written entirely in pure NumPy,
        with no deep learning frameworks.
        Can be extended for fine-tuning deep neural networks.

Author: Adhithya Laxman Ravi Shankar Geetha
GitHub: https://github.com/Adhithya-Laxman/
Date: 2025.10.21
- - - - - -- - - - - - - - - - - - - - - - - - - - - - -
"""

import matplotlib.pyplot as plt
import numpy as np


class RBM:
    def __init__(
        self,
        n_visible: int,
        n_hidden: int,
        learning_rate: float = 0.01,
        cd_steps: int = 1,
        epochs: int = 10,
        batch_size: int = 64,
        mode: str = "bernoulli",
    ) -> None:
        """
        Initialize an RBM (Restricted Boltzmann Machine).

        Args:
            n_visible (int): Number of visible units.
            n_hidden (int): Number of hidden units.
            learning_rate (float): Learning rate for weight updates.
            cd_steps (int): Number of Gibbs sampling steps for Contrastive Divergence.
            epochs (int): Number of training epochs.
            batch_size (int): Batch size.
            mode (str): Sampling mode ('bernoulli' or 'gaussian').

        >>> rbm = RBM(3, 2)
        >>> rbm.n_visible
        3
        >>> rbm.n_hidden
        2
        """
        self.n_visible = n_visible
        self.n_hidden = n_hidden
        self.learning_rate = learning_rate
        self.cd_steps = cd_steps
        self.epochs = epochs
        self.batch_size = batch_size
        self.mode = mode

        self.rng = np.random.default_rng()

        # Initialize weights and biases
        self.weights = self.rng.normal(0, 0.01, (n_visible, n_hidden))
        self.hidden_bias = np.zeros(n_hidden)
        self.visible_bias = np.zeros(n_visible)

    def sigmoid(self, input_array: np.ndarray) -> np.ndarray:
        """
        Compute the sigmoid activation function element-wise.

        Args:
            input_array (np.ndarray): Input array.

        Returns:
            np.ndarray: Sigmoid output of input.

        >>> rbm = RBM(3, 2)
        >>> import numpy as np
        >>> np.allclose(
        ...    rbm.sigmoid(np.array([0, 1])),
        ...    np.array([0.5, 1/(1+np.exp(-1))])
        ... )
        True
        """
        return 1.0 / (1.0 + np.exp(-input_array))

    def sample_prob(self, probabilities: np.ndarray) -> np.ndarray:
        """
        Sample binary states from given probabilities.

        Args:
            probabilities (np.ndarray): Probabilities of activation.

        Returns:
            np.ndarray: Binary sampled values.

        >>> rbm = RBM(3, 2)
        >>> probs = np.array([0., 1.])
        >>> result = rbm.sample_prob(probs)
        >>> set(result).issubset({0., 1.})
        True
        """
        return (self.rng.random(probabilities.shape) < probabilities).astype(float)

    def sample_hidden_given_visible(
        self, visible_batch: np.ndarray
    ) -> tuple[np.ndarray, np.ndarray]:
        """
        Sample hidden units conditioned on visible units.

        Args:
            visible_batch (np.ndarray): Visible unit batch.

        Returns:
            tuple: (hidden probabilities, hidden samples)

        >>> rbm = RBM(3, 2)
        >>> visible = np.array([[0., 1., 0.]])
        >>> probs, samples = rbm.sample_hidden_given_visible(visible)
        >>> probs.shape == samples.shape == (1, 2)
        True
        """
        hid_probs = self.sigmoid(np.dot(visible_batch, self.weights) + self.hidden_bias)
        hid_samples = self.sample_prob(hid_probs)
        return hid_probs, hid_samples

    def sample_visible_given_hidden(
        self, hidden_batch: np.ndarray
    ) -> tuple[np.ndarray, np.ndarray]:
        """
        Sample visible units conditioned on hidden units.

        Args:
            hidden_batch (np.ndarray): Hidden unit batch.

        Returns:
            tuple: (visible probabilities, visible samples)

        >>> rbm = RBM(3, 2)
        >>> hidden = np.array([[0., 1.]])
        >>> probs, samples = rbm.sample_visible_given_hidden(hidden)
        >>> probs.shape == samples.shape == (1, 3)
        True
        """
        vis_probs = self.sigmoid(
            np.dot(hidden_batch, self.weights.T) + self.visible_bias
        )
        vis_samples = self.sample_prob(vis_probs)
        return vis_probs, vis_samples

    def contrastive_divergence(self, visible_zero: np.ndarray) -> float:
        """
        Perform Contrastive Divergence (CD-k) for a single batch.

        Args:
            visible_zero (np.ndarray): Initial visible units (data batch).

        Returns:
            float: Reconstruction loss (mean squared error) for batch.

        >>> rbm = RBM(3, 2, cd_steps=2)
        >>> data = np.array([[0., 1., 0.]])
        >>> round(rbm.contrastive_divergence(data), 5)
        0.0 < 1.0  # Loss should be a non-negative float less than 1
        """
        h_probs0, h0 = self.sample_hidden_given_visible(visible_zero)
        vk, hk = visible_zero, h0

        for _ in range(self.cd_steps):
            _v_probs, vk = self.sample_visible_given_hidden(hk)
            h_probs, hk = self.sample_hidden_given_visible(vk)

        positive_grad = np.dot(visible_zero.T, h_probs0)
        negative_grad = np.dot(vk.T, h_probs)

        self.weights += (
            self.learning_rate * (positive_grad - negative_grad) / visible_zero.shape[0]
        )
        self.visible_bias += self.learning_rate * np.mean(visible_zero - vk, axis=0)
        self.hidden_bias += self.learning_rate * np.mean(h_probs0 - h_probs, axis=0)

        loss = np.mean((visible_zero - vk) ** 2)
        return loss

    def train(self, dataset: np.ndarray) -> None:
        """
        Train the RBM on the entire dataset.

        Args:
            dataset (np.ndarray): Training dataset matrix.

        >>> rbm = RBM(6, 3, epochs=1, batch_size=2)
        >>> data = np.random.randint(0, 2, (4, 6)).astype(float)
        >>> rbm.train(data)  # runs without error
        """
        n_samples = dataset.shape[0]
        for epoch in range(self.epochs):
            self.rng.shuffle(dataset)
            losses = []

            for i in range(0, n_samples, self.batch_size):
                batch = dataset[i : i + self.batch_size]
                loss = self.contrastive_divergence(batch)
                losses.append(loss)

            print(f"Epoch [{epoch + 1}/{self.epochs}] avg loss: {np.mean(losses):.6f}")


class DeepBeliefNetwork:
    def __init__(
        self,
        input_size: int,
        layers: list[int],
        mode: str = "bernoulli",
        cd_steps: int = 5,
        save_path: str | None = None,
    ) -> None:
        """
        Initialize a Deep Belief Network (DBN) with multiple RBM layers.

        Args:
            input_size (int): Number of features in input layer.
            layers (list): list of hidden layer unit counts.
            mode (str): Sampling mode ('bernoulli' or 'gaussian').
            cd_steps (int): Number of sampling steps in generate_input_for_layer.
            save_path (str, optional): Path for saving trained model parameters.

        >>> dbn = DeepBeliefNetwork(4, [3])
        >>> dbn.input_size
        4
        """
        self.input_size = input_size
        self.layers = layers
        self.cd_steps = cd_steps
        self.mode = mode
        self.save_path = save_path
        self.layer_params = [{"W": None, "hb": None, "vb": None} for _ in layers]

    def sigmoid(self, input_array: np.ndarray) -> np.ndarray:
        """
        Compute sigmoid activation function.

        Args:
            input_array (np.ndarray): Input array.

        Returns:
            np.ndarray: Sigmoid of input.

        >>> dbn = DeepBeliefNetwork(4, [3])
        >>> import numpy as np
        >>> np.allclose(
        ...    dbn.sigmoid(np.array([0, 1])),
        ...    np.array([0.5, 1/(1+np.exp(-1))])
        ... )
        True
        """
        return 1.0 / (1.0 + np.exp(-input_array))

    def sample_prob(self, probabilities: np.ndarray) -> np.ndarray:
        """
        Sample binary states from probabilities.

        Args:
            probabilities (np.ndarray): Activation probabilities.

        Returns:
            np.ndarray: Binary sampled values.

        >>> dbn = DeepBeliefNetwork(4, [3])
        >>> probs = np.array([0., 1.])
        >>> result = dbn.sample_prob(probs)
        >>> set(result).issubset({0., 1.})
        True
        """
        rng = np.random.default_rng()
        return (rng.random(probabilities.shape) < probabilities).astype(float)

    def sample_h(
        self, visible_units: np.ndarray, weights: np.ndarray, hidden_bias: np.ndarray
    ) -> tuple[np.ndarray, np.ndarray]:
        """
        Sample hidden units given visible units for a DBN layer.

        Args:
            visible_units (np.ndarray): Visible units.
            weights (np.ndarray): Weight matrix.
            hidden_bias (np.ndarray): Hidden bias vector.

        Returns:
            tuple: Hidden probabilities and binary samples.

        >>> dbn = DeepBeliefNetwork(4, [3])
        >>> import numpy as np
        >>> visible = np.array([[0., 1., 0., 1.]])
        >>> probs, samples = dbn.sample_h(visible, np.ones((4,3)), np.zeros(3))
        >>> probs.shape == samples.shape == (1, 3)
        True
        """
        probs = self.sigmoid(np.dot(visible_units, weights) + hidden_bias)
        samples = self.sample_prob(probs)
        return probs, samples

    def sample_v(
        self, hidden_units: np.ndarray, weights: np.ndarray, visible_bias: np.ndarray
    ) -> tuple[np.ndarray, np.ndarray]:
        """
        Sample visible units given hidden units for a DBN layer.

        Args:
            hidden_units (np.ndarray): Hidden units.
            weights (np.ndarray): Weight matrix.
            visible_bias (np.ndarray): Visible bias vector.

        Returns:
            tuple: Visible probabilities and binary samples.

        >>> dbn = DeepBeliefNetwork(4, [3])
        >>> import numpy as np
        >>> hidden = np.array([[0., 1., 1.]])
        >>> probs, samples = dbn.sample_v(hidden, np.ones((4,3)), np.zeros(4))
        >>> probs.shape == samples.shape == (1, 4)
        True
        """
        probs = self.sigmoid(np.dot(hidden_units, weights.T) + visible_bias)
        samples = self.sample_prob(probs)
        return probs, samples

    def generate_input_for_layer(
        self, layer_index: int, original_input: np.ndarray
    ) -> np.ndarray:
        """
        Generate input for a particular DBN layer by sampling and averaging.

        Args:
            layer_index (int): Layer index for which input is generated.
            original_input (np.ndarray): Original input data.

        Returns:
            np.ndarray: Smoothed input for the layer.

        >>> dbn = DeepBeliefNetwork(4, [3])
        >>> data = np.ones((2, 4))
        >>> np.allclose(dbn.generate_input_for_layer(0, data), data)
        True
        """
        if layer_index == 0:
            return original_input.copy()
        samples = []
        for _ in range(self.cd_steps):
            x_dash = original_input.copy()
            for i in range(layer_index):
                _, x_dash = self.sample_h(
                    x_dash, self.layer_params[i]["W"], self.layer_params[i]["hb"]
                )
            samples.append(x_dash)
        return np.mean(np.stack(samples, axis=0), axis=0)

    def train_dbn(self, training_data: np.ndarray) -> None:
        """
        Layer-wise train the DBN using RBMs.

        Args:
            training_data (np.ndarray): Training dataset.

        >>> dbn = DeepBeliefNetwork(4, [3])
        >>> data = np.random.randint(0, 2, (10, 4)).astype(float)
        >>> dbn.train_dbn(data)  # runs without error
        """
        for idx, layer_size in enumerate(self.layers):
            n_visible = self.input_size if idx == 0 else self.layers[idx - 1]
            n_hidden = layer_size

            rbm = RBM(n_visible, n_hidden, cd_steps=5, epochs=300)
            x_input = self.generate_input_for_layer(idx, training_data)
            rbm.train(x_input)
            self.layer_params[idx]["W"] = rbm.weights
            self.layer_params[idx]["hb"] = rbm.hidden_bias
            self.layer_params[idx]["vb"] = rbm.visible_bias
            print(f"Finished training layer {idx + 1}/{len(self.layers)}")

    def reconstruct(
        self, input_data: np.ndarray
    ) -> tuple[np.ndarray, np.ndarray, float]:
        """
        Reconstruct input through forward and backward Gibbs sampling.

        Args:
            input_data (np.ndarray): Input data to reconstruct.

        Returns:
            tuple: (encoded representation, reconstructed input, MSE error)

        >>> dbn = DeepBeliefNetwork(4, [3])
        >>> data = np.ones((2, 4))
        >>> encoded, reconstructed, error = dbn.reconstruct(data)
        >>> encoded.shape
        (2, 3)
        """
        h = input_data.copy()
        for i in range(len(self.layer_params)):
            _, h = self.sample_h(
                h, self.layer_params[i]["W"], self.layer_params[i]["hb"]
            )
        encoded = h.copy()

        for i in reversed(range(len(self.layer_params))):
            _, h = self.sample_v(
                h, self.layer_params[i]["W"], self.layer_params[i]["vb"]
            )
        reconstructed = h

        error = np.mean((input_data - reconstructed) ** 2)
        print(f"Reconstruction error: {error:.6f}")

        return encoded, reconstructed, error


# Usage example
if __name__ == "__main__":
    rng = np.random.default_rng()  # for random number generation
    data = rng.integers(0, 2, size=(100, 16)).astype(float)

    dbn = DeepBeliefNetwork(input_size=16, layers=[16, 8, 4])

    dbn.train_dbn(data)

    encoded, reconstructed, error = dbn.reconstruct(data[:5])
    print("Encoded shape:", encoded.shape)
    print("Reconstructed shape:", reconstructed.shape)

    features_to_show = 16
    plt.figure(figsize=(12, 5))
    for i in range(5):
        plt.subplot(2, 5, i + 1)
        plt.title(f"Original {i + 1}")
        plt.imshow(
            data[i][:features_to_show].reshape(1, -1),
            cmap="gray",
            aspect="auto",
            interpolation="nearest",
        )
        plt.axis("off")

        plt.subplot(2, 5, i + 6)
        plt.title(f"Reconstructed {i + 1}")
        plt.imshow(
            reconstructed[i][:features_to_show].reshape(1, -1),
            cmap="gray",
            aspect="auto",
            interpolation="nearest",
        )
        plt.axis("off")
    plt.suptitle(
        f"DBN Reconstruction (First {features_to_show} Features, MSE: {error:.6f})"
    )
    plt.tight_layout()
    plt.savefig("reconstruction_subset.png")
    print("Subset reconstruction plot saved as 'reconstruction_subset.png'")
