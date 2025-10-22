# -------------------------------
# 🔹 Imports
# -------------------------------
from __future__ import annotations
import math
from typing import Optional

import numpy as np


# -------------------------------
# 🔹 Helper functions
# -------------------------------
def _softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    x_max = np.max(x, axis=axis, keepdims=True)
    e = np.exp(x - x_max)
    return e / (np.sum(e, axis=axis, keepdims=True) + 1e-12)


def _stable_div(x: np.ndarray, denom: np.ndarray) -> np.ndarray:
    return x / (denom + 1e-12)


# -------------------------------
# 🔹 Time2Vec
# -------------------------------
class Time2Vec:
    """Time2Vec positional encoding for real-valued time steps."""

    def __init__(self, d_model: int, seed: Optional[int] = None) -> None:
        if seed is not None:
            self.rng = np.random.default_rng(seed)
        else:
            self.rng = np.random.default_rng()

        if d_model < 2:
            raise ValueError("d_model must be >= 2 for Time2Vec")

        self.w0 = self.rng.standard_normal((1, 1))
        self.b0 = self.rng.standard_normal((1, 1))
        self.w = self.rng.standard_normal((1, d_model - 1))
        self.b = self.rng.standard_normal((1, d_model - 1))

    def forward(self, time_steps: np.ndarray) -> np.ndarray:
        """
        Parameters
        ----------
        time_steps : np.ndarray
            Shape (batch, seq_len, 1) or (batch, seq_len)

        Returns
        -------
        np.ndarray
            Shape (batch, seq_len, d_model)
        """
        ts = time_steps if time_steps.ndim == 3 else time_steps[..., None]
        linear = (self.w0 * ts) + self.b0
        periodic = np.sin((ts * self.w) + self.b)
        return np.concatenate([linear, periodic], axis=-1)


# -------------------------------
# 🔹 PositionwiseFeedForward
# -------------------------------
class PositionwiseFeedForward:
    def __init__(
        self,
        d_model: int,
        hidden: int,
        drop_prob: float = 0.0,
        seed: Optional[int] = None,
    ) -> None:
        self.rng = np.random.default_rng(seed)
        self.w1 = self.rng.standard_normal((d_model, hidden)) * math.sqrt(
            2.0 / (d_model + hidden)
        )
        self.b1 = np.zeros((hidden,))
        self.w2 = self.rng.standard_normal((hidden, d_model)) * math.sqrt(
            2.0 / (hidden + d_model)
        )
        self.b2 = np.zeros((d_model,))

    def forward(self, input_tensor: np.ndarray) -> np.ndarray:
        """
        Parameters
        ----------
        input_tensor : np.ndarray
            Shape (batch, seq_len, d_model)

        Returns
        -------
        np.ndarray
            Shape (batch, seq_len, d_model)
        """
        h = np.tensordot(input_tensor, self.w1, axes=([2], [0])) + self.b1
        h = np.maximum(h, 0.0)
        out = np.tensordot(h, self.w2, axes=([2], [0])) + self.b2
        return out


# -------------------------------
# 🔹 ScaledDotProductAttention
# -------------------------------
class ScaledDotProductAttention:
    def forward(
        self,
        query: np.ndarray,
        key: np.ndarray,
        value: np.ndarray,
        mask: np.ndarray | None = None,
    ) -> tuple[np.ndarray, np.ndarray]:
        """
        Compute scaled dot-product attention.

        Returns
        -------
        context : np.ndarray
            Shape (batch, n_head, seq_len, d_k)
        attn_weights : np.ndarray
            Shape (batch, n_head, seq_len, seq_len)
        """
        batch_size, n_head, seq_len, d_k = query.shape
        scores = np.matmul(query, key.transpose(0, 1, 3, 2)) / math.sqrt(d_k)

        if mask is not None:
            mask2 = mask[:, None, None, :] if mask.ndim == 2 else mask
            scores = np.where(mask2 == 0, -1e9, scores)

        attn_weights = _softmax(scores, axis=-1)
        context = np.matmul(attn_weights, value)
        return context, attn_weights


# -------------------------------
# 🔹 MultiHeadAttention
# -------------------------------
class MultiHeadAttention:
    def __init__(self, d_model: int, n_head: int, seed: Optional[int] = None) -> None:
        if d_model % n_head != 0:
            raise ValueError("d_model must be divisible by n_head")

        self.rng = np.random.default_rng(seed)
        self.d_model = d_model
        self.n_head = n_head
        self.d_k = d_model // n_head

        self.w_q = self.rng.standard_normal((d_model, d_model)) * math.sqrt(
            2.0 / (d_model + d_model)
        )
        self.b_q = np.zeros((d_model,))
        self.w_k = self.rng.standard_normal((d_model, d_model)) * math.sqrt(
            2.0 / (d_model + d_model)
        )
        self.b_k = np.zeros((d_model,))
        self.w_v = self.rng.standard_normal((d_model, d_model)) * math.sqrt(
            2.0 / (d_model + d_model)
        )
        self.b_v = np.zeros((d_model,))
        self.w_out = self.rng.standard_normal((d_model, d_model)) * math.sqrt(
            2.0 / (d_model + d_model)
        )
        self.b_out = np.zeros((d_model,))

        self.attn = ScaledDotProductAttention()

    def _linear(
        self, x: np.ndarray, weight: np.ndarray, bias: np.ndarray
    ) -> np.ndarray:
        return np.tensordot(x, weight, axes=([2], [0])) + bias

    def _split_heads(self, x: np.ndarray) -> np.ndarray:
        batch_size, seq_len, _ = x.shape
        return x.reshape(batch_size, seq_len, self.n_head, self.d_k).transpose(
            0, 2, 1, 3
        )

    def _concat_heads(self, x: np.ndarray) -> np.ndarray:
        batch_size, n_head, seq_len, d_k = x.shape
        return x.transpose(0, 2, 1, 3).reshape(batch_size, seq_len, n_head * d_k)

    def forward(
        self,
        query: np.ndarray,
        key: np.ndarray,
        value: np.ndarray,
        mask: np.ndarray | None = None,
    ) -> tuple[np.ndarray, np.ndarray]:
        """
        Parameters
        ----------
        query/key/value : np.ndarray
            Shape (batch, seq_len, d_model)
        mask : np.ndarray | None
            Optional mask

        Returns
        -------
        out : np.ndarray
            Shape (batch, seq_len, d_model)
        attn_weights : np.ndarray
            Shape (batch, n_head, seq_len, seq_len)
        """
        q = self._linear(query, self.w_q, self.b_q)
        k = self._linear(key, self.w_k, self.b_k)
        v = self._linear(value, self.w_v, self.b_v)

        qh, kh, vh = self._split_heads(q), self._split_heads(k), self._split_heads(v)
        context, attn_weights = self.attn.forward(qh, kh, vh, mask)
        concat = self._concat_heads(context)
        out = np.tensordot(concat, self.w_out, axes=([2], [0])) + self.b_out
        return out, attn_weights


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
        Parameters
        ----------
        input_tensor : np.ndarray
            Shape (batch, seq_len, d_model)

        Returns
        -------
        np.ndarray
            Layer-normalized tensor of same shape
        """
        mean = np.mean(input_tensor, axis=-1, keepdims=True)
        var = np.mean((input_tensor - mean) ** 2, axis=-1, keepdims=True)
        x_norm = (input_tensor - mean) / np.sqrt(var + self.eps)
        return self.gamma * x_norm + self.beta


# -------------------------------
# 🔹 TransformerEncoderLayer
# -------------------------------
class TransformerEncoderLayer:
    def __init__(
        self, d_model: int, n_head: int, hidden_dim: int, seed: Optional[int] = None
    ) -> None:
        self.self_attn = MultiHeadAttention(d_model, n_head, seed)
        self.ffn = PositionwiseFeedForward(d_model, hidden_dim, seed=seed)
        self.norm1 = LayerNorm(d_model)
        self.norm2 = LayerNorm(d_model)

    def forward(
        self, input_tensor: np.ndarray, mask: np.ndarray | None = None
    ) -> np.ndarray:
        """
        Parameters
        ----------
        input_tensor : np.ndarray
            Shape (batch, seq_len, d_model)
        mask : np.ndarray | None
            Optional attention mask

        Returns
        -------
        np.ndarray
            Shape (batch, seq_len, d_model)
        """
        attn_out, _ = self.self_attn.forward(
            input_tensor, input_tensor, input_tensor, mask
        )
        x_norm1 = self.norm1.forward(input_tensor + attn_out)
        ffn_out = self.ffn.forward(x_norm1)
        x_norm2 = self.norm2.forward(x_norm1 + ffn_out)
        return x_norm2


# -------------------------------
# 🔹 TransformerEncoder (stack)
# -------------------------------
class TransformerEncoder:
    def __init__(
        self,
        d_model: int,
        n_head: int,
        hidden_dim: int,
        num_layers: int,
        seed: Optional[int] = None,
    ) -> None:
        self.layers = [
            TransformerEncoderLayer(d_model, n_head, hidden_dim, seed)
            for _ in range(num_layers)
        ]

    def forward(
        self, input_tensor: np.ndarray, mask: np.ndarray | None = None
    ) -> np.ndarray:
        """
        Parameters
        ----------
        input_tensor : np.ndarray
            Shape (batch, seq_len, d_model)
        mask : np.ndarray | None
            Optional attention mask

        Returns
        -------
        np.ndarray
            Shape (batch, seq_len, d_model)
        """
        output = input_tensor
        for layer in self.layers:
            output = layer.forward(output, mask)
        return output


# -------------------------------
# 🔹 AttentionPooling
# -------------------------------
class AttentionPooling:
    def __init__(self, d_model: int, seed: Optional[int] = None) -> None:
        self.rng = np.random.default_rng(seed)
        self.w = self.rng.standard_normal((d_model,)) * math.sqrt(2.0 / d_model)
        self.b = 0.0

    def forward(
        self, input_tensor: np.ndarray, mask: np.ndarray | None = None
    ) -> tuple[np.ndarray, np.ndarray]:
        """
        Parameters
        ----------
        input_tensor : np.ndarray
            Shape (batch, seq_len, d_model)
        mask : np.ndarray | None
            Shape (batch, seq_len) where 1=valid, 0=pad

        Returns
        -------
        pooled : np.ndarray
            Shape (batch, d_model)
        attn_weights : np.ndarray
            Shape (batch, seq_len)
        """
        scores = np.tensordot(input_tensor, self.w, axes=([2], [0])) + self.b
        if mask is not None:
            scores = np.where(mask == 0, -1e9, scores)
        attn_weights = _softmax(scores, axis=-1)
        pooled = np.matmul(attn_weights[:, None, :], input_tensor).squeeze(1)
        return pooled, attn_weights


# -------------------------------
# 🔹 EEGTransformer
# -------------------------------
class EEGTransformer:
    def __init__(
        self,
        feature_dim: int,
        d_model: int = 128,
        n_head: int = 8,
        hidden_dim: int = 512,
        num_layers: int = 4,
        output_dim: int = 1,
        task_type: str = "regression",
        seed: Optional[int] = None,
    ) -> None:
        self.rng = np.random.default_rng(seed)
        self.feature_dim = feature_dim
        self.d_model = d_model
        self.task_type = task_type

        self.w_in = self.rng.standard_normal((feature_dim, d_model)) * math.sqrt(
            2.0 / (feature_dim + d_model)
        )
        self.b_in = np.zeros((d_model,))

        self.time2vec = Time2Vec(d_model, seed)
        self.encoder = TransformerEncoder(d_model, n_head, hidden_dim, num_layers, seed)
        self.pooling = AttentionPooling(d_model, seed)

        self.w_out = self.rng.standard_normal((d_model, output_dim)) * math.sqrt(
            2.0 / (d_model + output_dim)
        )
        self.b_out = np.zeros((output_dim,))

    def _input_proj(self, features: np.ndarray) -> np.ndarray:
        return np.tensordot(features, self.w_in, axes=([2], [0])) + self.b_in

    def forward(
        self, features: np.ndarray, mask: np.ndarray | None = None
    ) -> tuple[np.ndarray, np.ndarray]:
        """
        Parameters
        ----------
        features : np.ndarray
            Shape (batch, seq_len, feature_dim)
        mask : np.ndarray | None
            Optional mask

        Returns
        -------
        output : np.ndarray
            Shape (batch, output_dim)
        attn_weights : np.ndarray
            Shape (batch, seq_len)
        """
        batch_size, seq_len, _ = features.shape
        time_indices = np.arange(seq_len, dtype=float)[None, :, None]
        time_indices = np.tile(time_indices, (batch_size, 1, 1))

        time_emb = self.time2vec.forward(time_indices)
        x_proj = self._input_proj(features) + time_emb

        enc_out = self.encoder.forward(x_proj, mask)
        pooled, attn_weights = self.pooling.forward(enc_out, mask)

        output = np.tensordot(pooled, self.w_out, axes=([1], [0])) + self.b_out
        if self.task_type == "classification":
            output = _softmax(output, axis=-1)

        return output, attn_weights
