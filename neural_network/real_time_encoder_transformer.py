from __future__ import annotations
import math
from typing import Optional

import numpy as np
import pandas as pd


def _softmax(array: np.ndarray, axis: int = -1) -> np.ndarray:
    max_val = np.max(array, axis=axis, keepdims=True)
    exp = np.exp(array - max_val)
    return exp / (np.sum(exp, axis=axis, keepdims=True) + 1e-12)


def _stable_div(numerator: np.ndarray, denominator: np.ndarray) -> np.ndarray:
    return numerator / (denominator + 1e-12)


# -------------------------------
# 🔹 Time2Vec
# -------------------------------

class Time2Vec:
    def __init__(self, d_model: int, seed: Optional[int] = None) -> None:
        if d_model < 2:
            raise ValueError("d_model must be >= 2 for Time2Vec")

        self.rng = np.random.default_rng(seed)
        self.w0: np.ndarray = self.rng.standard_normal((1, 1))
        self.b0: np.ndarray = self.rng.standard_normal((1, 1))
        self.w: np.ndarray = self.rng.standard_normal((1, d_model - 1))
        self.b: np.ndarray = self.rng.standard_normal((1, d_model - 1))

    def forward(self, time_indices: np.ndarray) -> np.ndarray:
        """
        Parameters
        ----------
        time_indices : np.ndarray
            Shape (batch, seq_len) or (batch, seq_len, 1)

        Returns
        -------
        np.ndarray
            Shape (batch, seq_len, d_model)

        Example
        -------
        >>> t2v = Time2Vec(4, seed=0)
        >>> ts = np.arange(3).reshape(1, 3, 1)
        >>> out = t2v.forward(ts)
        >>> out.shape
        (1, 3, 4)
        """
        if time_indices.ndim == 2:
            time_indices = time_indices[..., None]

        linear_term = (self.w0 * time_indices) + self.b0
        periodic_term = np.sin((time_indices * self.w) + self.b)
        return np.concatenate([linear_term, periodic_term], axis=-1)


# -------------------------------
# 🔹 Positionwise FeedForward
# -------------------------------

class PositionwiseFeedForward:
    def __init__(self, d_model: int, hidden_dim: int, drop_prob: float = 0.0, seed: Optional[int] = None) -> None:
        self.rng = np.random.default_rng(seed)
        self.w1: np.ndarray = self.rng.standard_normal((d_model, hidden_dim)) * math.sqrt(2.0 / (d_model + hidden_dim))
        self.b1: np.ndarray = np.zeros((hidden_dim,))
        self.w2: np.ndarray = self.rng.standard_normal((hidden_dim, d_model)) * math.sqrt(2.0 / (hidden_dim + d_model))
        self.b2: np.ndarray = np.zeros((d_model,))

    def forward(self, input_tensor: np.ndarray) -> np.ndarray:
        hidden = np.tensordot(input_tensor, self.w1, axes=([2], [0])) + self.b1
        hidden = np.maximum(hidden, 0.0)  # ReLU
        output_tensor = np.tensordot(hidden, self.w2, axes=([2], [0])) + self.b2
        return output_tensor


# -------------------------------
# 🔹 Scaled Dot-Product Attention
# -------------------------------

class ScaledDotProductAttention:
    def forward(
        self,
        query: np.ndarray,
        key: np.ndarray,
        value: np.ndarray,
        mask: Optional[np.ndarray] = None,
    ) -> tuple[np.ndarray, np.ndarray]:
        batch_size, n_head, seq_len, d_k = query.shape
        scores = np.matmul(query, key.transpose(0, 1, 3, 2)) / math.sqrt(d_k)

        if mask is not None:
            if mask.ndim == 2:
                mask_reshaped = mask[:, None, None, :]
            elif mask.ndim == 3:
                mask_reshaped = mask[:, None, :, :] if mask.shape[1] != seq_len else mask[:, None, None, :]
            else:
                mask_reshaped = mask
            scores = np.where(mask_reshaped == 0, -1e9, scores)

        attn_weights = _softmax(scores, axis=-1)
        context = np.matmul(attn_weights, value)
        return context, attn_weights


# -------------------------------
# 🔹 Multi-Head Attention
# -------------------------------

class MultiHeadAttention:
    def __init__(self, d_model: int, n_head: int, seed: Optional[int] = None) -> None:
        if d_model % n_head != 0:
            raise ValueError("d_model must be divisible by n_head")
        self.rng = np.random.default_rng(seed)

        self.d_model = d_model
        self.n_head = n_head
        self.d_k = d_model // n_head

        self.w_q = self.rng.standard_normal((d_model, d_model)) * math.sqrt(2.0 / (d_model + d_model))
        self.b_q = np.zeros((d_model,))
        self.w_k = self.rng.standard_normal((d_model, d_model)) * math.sqrt(2.0 / (d_model + d_model))
        self.b_k = np.zeros((d_model,))
        self.w_v = self.rng.standard_normal((d_model, d_model)) * math.sqrt(2.0 / (d_model + d_model))
        self.b_v = np.zeros((d_model,))
        self.w_out = self.rng.standard_normal((d_model, d_model)) * math.sqrt(2.0 / (d_model + d_model))
        self.b_out = np.zeros((d_model,))

        self.attn = ScaledDotProductAttention()

    def _linear(self, input_tensor: np.ndarray, weight: np.ndarray, bias: np.ndarray) -> np.ndarray:
        return np.tensordot(input_tensor, weight, axes=([2], [0])) + bias

    def _split_heads(self, input_tensor: np.ndarray) -> np.ndarray:
        batch_size, seq_len, _ = input_tensor.shape
        return input_tensor.reshape(batch_size, seq_len, self.n_head, self.d_k).transpose(0, 2, 1, 3)

    def _concat_heads(self, input_tensor: np.ndarray) -> np.ndarray:
        batch_size, n_head, seq_len, d_k = input_tensor.shape
        return input_tensor.transpose(0, 2, 1, 3).reshape(batch_size, seq_len, n_head * d_k)

    def forward(
        self,
        query_tensor: np.ndarray,
        key_tensor: np.ndarray,
        value_tensor: np.ndarray,
        mask: Optional[np.ndarray] = None,
    ) -> tuple[np.ndarray, np.ndarray]:
        """
        Forward pass of multi-head attention.

        Returns
        -------
        out: np.ndarray
            Shape (batch, seq_len, d_model)
        attn_weights: np.ndarray
            Shape (batch, n_head, seq_len, seq_len)
        """
        qh = self._split_heads(self._linear(query_tensor, self.w_q, self.b_q))
        kh = self._split_heads(self._linear(key_tensor, self.w_k, self.b_k))
        vh = self._split_heads(self._linear(value_tensor, self.w_v, self.b_v))

        context, attn_weights = self.attn.forward(qh, kh, vh, mask)
        concat = self._concat_heads(context)
        out_tensor = np.tensordot(concat, self.w_out, axes=([2], [0])) + self.b_out
        return out_tensor, attn_weights


# -------------------------------
# 🔹 LayerNorm
# -------------------------------

class LayerNorm:
    def __init__(self, d_model: int, eps: float = 1e-12) -> None:
        self.gamma: np.ndarray = np.ones((d_model,))
        self.beta: np.ndarray = np.zeros((d_model,))
        self.eps = eps

    def forward(self, input_tensor: np.ndarray) -> np.ndarray:
        mean = np.mean(input_tensor, axis=-1, keepdims=True)
        var = np.mean((input_tensor - mean) ** 2, axis=-1, keepdims=True)
        normalized_tensor = (input_tensor - mean) / np.sqrt(var + self.eps)
        return self.gamma * normalized_tensor + self.beta
# -------------------------------
# 🔹 Transformer Encoder Layer
# -------------------------------

class TransformerEncoderLayer:
    def __init__(self, d_model: int, n_head: int, hidden_dim: int, seed: Optional[int] = None) -> None:
        self.self_attn = MultiHeadAttention(d_model, n_head, seed=seed)
        self.ffn = PositionwiseFeedForward(d_model, hidden_dim, seed=seed)
        self.norm1 = LayerNorm(d_model)
        self.norm2 = LayerNorm(d_model)

    def forward(self, encoded_input: np.ndarray, mask: Optional[np.ndarray] = None) -> np.ndarray:
        """
        Forward pass for one encoder layer.

        Parameters
        ----------
        encoded_input : np.ndarray
            Shape (batch, seq_len, d_model)
        mask : np.ndarray | None
            Optional mask (batch, seq_len)

        Returns
        -------
        np.ndarray
            Shape (batch, seq_len, d_model)

        Example
        -------
        >>> layer = TransformerEncoderLayer(d_model=4, n_head=2, hidden_dim=8, seed=0)
        >>> x = np.random.randn(1, 3, 4)
        >>> out = layer.forward(x)
        >>> out.shape
        (1, 3, 4)
        """
        attn_output, _ = self.self_attn.forward(encoded_input, encoded_input, encoded_input, mask)
        out1 = self.norm1.forward(encoded_input + attn_output)
        ffn_output = self.ffn.forward(out1)
        out2 = self.norm2.forward(out1 + ffn_output)
        return out2


# -------------------------------
# 🔹 Transformer Encoder Stack
# -------------------------------

class TransformerEncoder:
    def __init__(self, d_model: int, n_head: int, hidden_dim: int, num_layers: int, seed: Optional[int] = None) -> None:
        self.layers = [TransformerEncoderLayer(d_model, n_head, hidden_dim, seed=seed) for _ in range(num_layers)]

    def forward(self, encoded_input: np.ndarray, mask: Optional[np.ndarray] = None) -> np.ndarray:
        """
        Forward pass for encoder stack.

        Parameters
        ----------
        encoded_input : np.ndarray
            Shape (batch, seq_len, d_model)
        mask : np.ndarray | None
            Optional mask

        Returns
        -------
        np.ndarray
            Shape (batch, seq_len, d_model)

        Example
        -------
        >>> encoder = TransformerEncoder(d_model=4, n_head=2, hidden_dim=8, num_layers=2, seed=0)
        >>> x = np.random.randn(1, 3, 4)
        >>> out = encoder.forward(x)
        >>> out.shape
        (1, 3, 4)
        """
        out = encoded_input
        for layer in self.layers:
            out = layer.forward(out, mask)
        return out


# -------------------------------
# 🔹 Attention Pooling
# -------------------------------

class AttentionPooling:
    def __init__(self, d_model: int, seed: Optional[int] = None) -> None:
        self.rng = np.random.default_rng(seed)
        self.w: np.ndarray = self.rng.standard_normal(d_model) * math.sqrt(2.0 / d_model)
        self.b: float = 0.0

    def forward(self, encoded_features: np.ndarray, mask: Optional[np.ndarray] = None) -> tuple[np.ndarray, np.ndarray]:
        """
        Attention-based pooling.

        Parameters
        ----------
        encoded_features : np.ndarray
            Shape (batch, seq_len, d_model)
        mask : np.ndarray | None
            Optional mask (batch, seq_len), 1=valid, 0=pad

        Returns
        -------
        pooled_output : np.ndarray
            Shape (batch, d_model)
        attention_weights : np.ndarray
            Shape (batch, seq_len)

        Example
        -------
        >>> pooling = AttentionPooling(d_model=4, seed=0)
        >>> x = np.random.randn(1, 3, 4)
        >>> pooled, weights = pooling.forward(x)
        >>> pooled.shape
        (1, 4)
        >>> weights.shape
        (1, 3)
        """
        scores = np.tensordot(encoded_features, self.w, axes=([2], [0])) + self.b
        if mask is not None:
            scores = np.where(mask == 0, -1e9, scores)
        weights = _softmax(scores, axis=-1)
        pooled_output = np.matmul(weights[:, None, :], encoded_features).squeeze(1)
        return pooled_output, weights


# -------------------------------
# 🔹 EEG Transformer
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

        self.w_in: np.ndarray = self.rng.standard_normal((feature_dim, d_model)) * math.sqrt(2.0 / (feature_dim + d_model))
        self.b_in: np.ndarray = np.zeros((d_model,))

        self.time2vec = Time2Vec(d_model, seed=seed)
        self.encoder = TransformerEncoder(d_model, n_head, hidden_dim, num_layers, seed=seed)
        self.pooling = AttentionPooling(d_model, seed=seed)

        self.w_out: np.ndarray = self.rng.standard_normal((d_model, output_dim)) * math.sqrt(2.0 / (d_model + output_dim))
        self.b_out: np.ndarray = np.zeros((output_dim,))

    def _input_projection(self, input_tensor: np.ndarray) -> np.ndarray:
        return np.tensordot(input_tensor, self.w_in, axes=([2], [0])) + self.b_in

    def forward(self, input_tensor: np.ndarray, mask: Optional[np.ndarray] = None) -> tuple[np.ndarray, np.ndarray]:
        """
        Forward pass for EEG Transformer.

        Parameters
        ----------
        input_tensor : np.ndarray
            Shape (batch, seq_len, feature_dim)
        mask : np.ndarray | None
            Optional mask (batch, seq_len), 1=valid, 0=pad

        Returns
        -------
        output_tensor : np.ndarray
            Shape (batch, output_dim)
        attention_weights : np.ndarray
            Shape (batch, seq_len)

        Example
        -------
        >>> model = EEGTransformer(feature_dim=8, d_model=32, n_head=4, hidden_dim=64, num_layers=2, output_dim=1, seed=0)
        >>> x = np.random.randn(2, 10, 8)
        >>> out, attn = model.forward(x)
        >>> out.shape
        (2, 1)
        >>> attn.shape
        (2, 10)
        """
        batch_size, seq_len, _ = input_tensor.shape
        time_indices = np.arange(seq_len, dtype=float)[None, :, None]
        time_indices = np.tile(time_indices, (batch_size, 1, 1))

        time_embedding = self.time2vec.forward(time_indices)
        projected_input = self._input_projection(input_tensor) + time_embedding

        encoded_features = self.encoder.forward(projected_input, mask)
        pooled_output, attention_weights = self.pooling.forward(encoded_features, mask)

        output_tensor = np.tensordot(pooled_output, self.w_out, axes=([1], [0])) + self.b_out
        if self.task_type == "classification":
            output_tensor = _softmax(output_tensor, axis=-1)

        return output_tensor, attention_weights
