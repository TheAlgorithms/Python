# 🔹 Imports
# -------------------------------
from __future__ import annotations

import math
import numpy as np


# -------------------------------
# 🔹 Time2Vec Layer
# -------------------------------
class Time2Vec:
    """Time2Vec positional encoding for real-valued time steps."""

    def __init__(self, d_model: int, seed: int | None = None) -> None:
        self.rng = np.random.default_rng(seed)
        self.w0 = self.rng.standard_normal((1, 1))
        self.b0 = self.rng.standard_normal((1, 1))
        self.w = self.rng.standard_normal((1, d_model - 1))
        self.b = self.rng.standard_normal((1, d_model - 1))

    def forward(self, time_steps: np.ndarray) -> np.ndarray:
        """
        Parameters
        ----------
        time_steps : np.ndarray
            Shape (batch, seq_len, 1)

        Returns
        -------
        np.ndarray
            Shape (batch, seq_len, d_model)

        Doctest
        -------
        >>> t2v = Time2Vec(4, seed=0)
        >>> t = np.ones((1, 3, 1))
        >>> out = t2v.forward(t)
        >>> out.shape
        (1, 3, 4)
        """
        linear = self.w0 * time_steps + self.b0
        periodic = np.sin(self.w * time_steps + self.b)
        return np.concatenate([linear, periodic], axis=-1)


# -------------------------------
# 🔹 LayerNorm
# -------------------------------
class LayerNorm:
    def __init__(self, d_model: int, eps: float = 1e-12) -> None:
        self.gamma = np.ones((d_model,))
        self.beta = np.zeros((d_model,))
        self.eps = eps

    def forward(self, input_tensor: np.ndarray) -> np.ndarray:
        """
        >>> ln = LayerNorm(4)
        >>> x = np.ones((1, 3, 4))
        >>> out = ln.forward(x)
        >>> out.shape
        (1, 3, 4)
        """
        mean = np.mean(input_tensor, axis=-1, keepdims=True)
        var = np.mean((input_tensor - mean) ** 2, axis=-1, keepdims=True)
        x_norm = (input_tensor - mean) / np.sqrt(var + self.eps)
        return self.gamma * x_norm + self.beta


# -------------------------------
# 🔹 PositionwiseFeedForward
# -------------------------------
class PositionwiseFeedForward:
    def __init__(self, d_model: int, hidden: int, seed: int | None = None) -> None:
        self.rng = np.random.default_rng(seed)
        self.linear1_w = self.rng.standard_normal((d_model, hidden)) * math.sqrt(
            2.0 / (d_model + hidden)
        )
        self.linear1_b = np.zeros((hidden,))
        self.linear2_w = self.rng.standard_normal((hidden, d_model)) * math.sqrt(
            2.0 / (hidden + d_model)
        )
        self.linear2_b = np.zeros((d_model,))

    def forward(self, x_tensor: np.ndarray) -> np.ndarray:
        """
        >>> ff = PositionwiseFeedForward(4, 8, seed=0)
        >>> x = np.ones((1, 3, 4))
        >>> out = ff.forward(x)
        >>> out.shape
        (1, 3, 4)
        """
        hidden = (
            np.tensordot(x_tensor, self.linear1_w, axes=([2], [0])) + self.linear1_b
        )
        hidden = np.maximum(0, hidden)  # ReLU
        out = np.tensordot(hidden, self.linear2_w, axes=([2], [0])) + self.linear2_b
        return out


# -------------------------------
# 🔹 MultiHeadAttention
# -------------------------------
class MultiHeadAttention:
    def __init__(self, d_model: int, n_head: int, seed: int | None = None) -> None:
        if d_model % n_head != 0:
            raise ValueError("d_model must be divisible by n_head")
        self.d_model = d_model
        self.n_head = n_head
        self.d_k = d_model // n_head
        self.rng = np.random.default_rng(seed)
        self.w_q = self.rng.standard_normal((d_model, d_model)) * math.sqrt(
            2.0 / d_model
        )
        self.w_k = self.rng.standard_normal((d_model, d_model)) * math.sqrt(
            2.0 / d_model
        )
        self.w_v = self.rng.standard_normal((d_model, d_model)) * math.sqrt(
            2.0 / d_model
        )
        self.w_o = self.rng.standard_normal((d_model, d_model)) * math.sqrt(
            2.0 / d_model
        )

    def forward(
        self,
        query: np.ndarray,
        key: np.ndarray,
        value: np.ndarray,
        mask: np.ndarray | None = None,
    ) -> tuple[np.ndarray, np.ndarray]:
        """
        >>> attn = MultiHeadAttention(4, 2, seed=0)
        >>> x = np.ones((1, 3, 4))
        >>> out, w = attn.forward(x, x, x)
        >>> out.shape
        (1, 3, 4)
        >>> w.shape
        (1, 2, 3, 3)
        """
        batch_size, _seq_len, _ = query.shape
        q = np.tensordot(query, self.w_q, axes=([2], [0]))
        k = np.tensordot(key, self.w_k, axes=([2], [0]))
        v = np.tensordot(value, self.w_v, axes=([2], [0]))

        q = q.reshape(batch_size, -1, self.n_head, self.d_k).transpose(0, 2, 1, 3)
        k = k.reshape(batch_size, -1, self.n_head, self.d_k).transpose(0, 2, 1, 3)
        v = v.reshape(batch_size, -1, self.n_head, self.d_k).transpose(0, 2, 1, 3)

        scores = np.matmul(q, k.transpose(0, 1, 3, 2)) / math.sqrt(self.d_k)
        if mask is not None:
            scores = np.where(mask[:, None, None, :] == 0, -1e9, scores)

        attn_weights = _softmax(scores, axis=-1)
        out = np.matmul(attn_weights, v)
        out = out.transpose(0, 2, 1, 3).reshape(batch_size, -1, self.d_model)
        out = np.tensordot(out, self.w_o, axes=([2], [0]))
        return out, attn_weights


# -------------------------------
# 🔹 TransformerEncoderLayer
# -------------------------------
class TransformerEncoderLayer:
    def __init__(
        self, d_model: int, n_head: int, hidden_dim: int, seed: int | None = None
    ) -> None:
        self.self_attn = MultiHeadAttention(d_model, n_head, seed)
        self.norm1 = LayerNorm(d_model)
        self.ff = PositionwiseFeedForward(d_model, hidden_dim, seed)
        self.norm2 = LayerNorm(d_model)

    def forward(
        self, x_tensor: np.ndarray, mask: np.ndarray | None = None
    ) -> np.ndarray:
        """
        >>> layer = TransformerEncoderLayer(4, 2, 8, seed=0)
        >>> x = np.ones((1, 3, 4))
        >>> out = layer.forward(x)
        >>> out.shape
        (1, 3, 4)
        """
        attn_out, _ = self.self_attn.forward(x_tensor, x_tensor, x_tensor, mask)
        x_tensor = self.norm1.forward(x_tensor + attn_out)
        ff_out = self.ff.forward(x_tensor)
        x_tensor = self.norm2.forward(x_tensor + ff_out)
        return x_tensor


# -------------------------------
# 🔹 TransformerEncoder
# -------------------------------
class TransformerEncoder:
    def __init__(
        self,
        d_model: int,
        n_head: int,
        hidden_dim: int,
        num_layers: int,
        seed: int | None = None,
    ) -> None:
        self.layers = [
            TransformerEncoderLayer(d_model, n_head, hidden_dim, seed)
            for _ in range(num_layers)
        ]

    def forward(
        self, x_tensor: np.ndarray, mask: np.ndarray | None = None
    ) -> np.ndarray:
        """
        >>> encoder = TransformerEncoder(4, 2, 8, 2, seed=0)
        >>> x = np.ones((1, 3, 4))
        >>> out = encoder.forward(x)
        >>> out.shape
        (1, 3, 4)
        """
        for layer in self.layers:
            x_tensor = layer.forward(x_tensor, mask)
        return x_tensor


# -------------------------------
# 🔹 AttentionPooling
# -------------------------------
class AttentionPooling:
    def __init__(self, d_model: int, seed: int | None = None) -> None:
        self.rng = np.random.default_rng(seed)
        self.w = self.rng.standard_normal((d_model,)) * math.sqrt(2.0 / d_model)

    def forward(self, x_tensor: np.ndarray) -> np.ndarray:
        """
        >>> pool = AttentionPooling(4, seed=0)
        >>> x = np.ones((1, 3, 4))
        >>> out = pool.forward(x)
        >>> out.shape
        (1, 4)
        """
        attn_weights = _softmax(np.tensordot(x_tensor, self.w, axes=([2], [0])), axis=1)
        return np.sum(x_tensor * attn_weights[..., None], axis=1)


# -------------------------------
# 🔹 EEGTransformer
# -------------------------------
class EEGTransformer:
    def __init__(
        self,
        d_model: int,
        n_head: int,
        hidden_dim: int,
        num_layers: int,
        output_dim: int = 1,
        task_type: str = "regression",
        seed: int | None = None,
    ) -> None:
        self.time2vec = Time2Vec(d_model, seed)
        self.encoder = TransformerEncoder(d_model, n_head, hidden_dim, num_layers, seed)
        self.pooling = AttentionPooling(d_model, seed)
        self.output_dim = output_dim
        self.task_type = task_type
        self.rng = np.random.default_rng(seed)
        self.w_out = self.rng.standard_normal((d_model, output_dim)) * math.sqrt(
            2.0 / (d_model + output_dim)
        )
        self.b_out = np.zeros((output_dim,))

    def forward(self, eeg_data: np.ndarray) -> np.ndarray:
        """
        >>> model = EEGTransformer(4, 2, 8, 2, seed=0)
        >>> x = np.ones((1, 3, 4))
        >>> out = model.forward(x)
        >>> out.shape
        (1, 1)
        """
        x = self.time2vec.forward(eeg_data)
        x = self.encoder.forward(x)
        x = self.pooling.forward(x)
        out = np.tensordot(x, self.w_out, axes=([1], [0])) + self.b_out
        return out


# -------------------------------
# 🔹 Helper softmax
# -------------------------------
def _softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    x_max = np.max(x, axis=axis, keepdims=True)
    e = np.exp(x - x_max)
    return e / (np.sum(e, axis=axis, keepdims=True) + 1e-12)
