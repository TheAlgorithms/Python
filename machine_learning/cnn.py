
import numpy as np

# Simple Convolutional Neural Network (CNN) implementation using numpy
# Supports a single convolutional and pooling layer, followed by a fully connected layer
class SimpleCNN:
    def __init__(self, num_filters=8, filter_size=3, pool_size=2, num_classes=10):
        self.num_filters = num_filters  # Number of convolutional filters
        self.filter_size = filter_size  # Size of each filter (square)
        self.pool_size = pool_size      # Pooling window size
        self.num_classes = num_classes  # Number of output classes
        # Randomly initialize convolutional filters
        self.filters = np.random.randn(num_filters, filter_size, filter_size) / 9
        self.fc_weights = None  # Fully connected layer weights

    def _convolve(self, X):
        # Perform convolution operation on input X
        h, w = X.shape
        out_dim = h - self.filter_size + 1
        feature_maps = np.zeros((self.num_filters, out_dim, out_dim))
        for f in range(self.num_filters):
            for i in range(out_dim):
                for j in range(out_dim):
                    region = X[i:i+self.filter_size, j:j+self.filter_size]
                    feature_maps[f, i, j] = np.sum(region * self.filters[f])
        return feature_maps

    def _pool(self, feature_maps):
        # Apply max pooling to feature maps
        num_filters, h, w = feature_maps.shape
        pool_h = h // self.pool_size
        pool_w = w // self.pool_size
        pooled = np.zeros((num_filters, pool_h, pool_w))
        for f in range(num_filters):
            for i in range(pool_h):
                for j in range(pool_w):
                    region = feature_maps[f, i*self.pool_size:(i+1)*self.pool_size, j*self.pool_size:(j+1)*self.pool_size]
                    pooled[f, i, j] = np.max(region)
        return pooled

    def _flatten(self, pooled):
        # Flatten pooled feature maps for fully connected layer
        return pooled.flatten()

    def fit(self, X, y):
        # Dummy fit: just sets up a random FC layer for demonstration
        # In practice, CNNs are trained with backpropagation
        n_samples = X.shape[0]
        sample_flat = self._flatten(self._pool(self._convolve(X[0])))
        self.fc_weights = np.random.randn(self.num_classes, sample_flat.shape[0]) / np.sqrt(sample_flat.shape[0])

    def predict(self, X):
        # Predict class for each input sample
        preds = []
        for x in X:
            feature_maps = self._convolve(x)
            pooled = self._pool(feature_maps)
            flat = self._flatten(pooled)
            logits = self.fc_weights @ flat
            preds.append(np.argmax(logits))
        return np.array(preds)
