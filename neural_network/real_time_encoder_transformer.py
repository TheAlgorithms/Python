from __future__ import annotations
import math
from typing import Optional, Tuple

import numpy as np
import pandas as pd


def _softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    x_max = np.max(x, axis=axis, keepdims=True)
    e = np.exp(x - x_max)
    return e / (np.sum(e, axis=axis, keepdims=True) + 1e-12)


def _stable_div(x: np.ndarray, denom: np.ndarray) -> np.ndarray:
    return x / (denom + 1e-12)


# Time2Vec


class Time2Vec:
    """
    Time2Vec positional encoding (simple) for real-valued time steps.
    Produces shape (..., d_model)
    """

    def __init__(self, d_model: int, seed: Optional[int] = None):
        if seed is not None:
            np.random.seed(seed)
        # linear term params (scalar per batch/time)
        self.w0 = np.random.randn(1, 1)  # multiply time scalar
        self.b0 = np.random.randn(1, 1)
        # periodic terms params (d_model - 1)
        if d_model < 2:
            raise ValueError("d_model must be >= 2 for Time2Vec")
        self.w = np.random.randn(1, d_model - 1)
        self.b = np.random.randn(1, d_model - 1)

    def forward(self, time_steps: np.ndarray) -> np.ndarray:
        """
        time_steps: shape (batch, seq_len, 1) or (batch, seq_len) (will be reshaped)
        returns: (batch, seq_len, d_model)
        """
        ts = time_steps
        if ts.ndim == 2:
            ts = ts[..., None]
        linear = (self.w0 * ts) + self.b0  # (b, t, 1)
        periodic = np.sin((ts * self.w) + self.b)  # broadcasting -> (b,t,d_model-1)
        return np.concatenate([linear, periodic], axis=-1)


# PositionwiseFeedForward


class PositionwiseFeedForward:
    def __init__(
        self,
        d_model: int,
        hidden: int,
        drop_prob: float = 0.0,
        seed: Optional[int] = None,
    ):
        if seed is not None:
            np.random.seed(seed)
        # simple linear layers (no dropout during forward-only inference, but kept shape)
        self.w1 = np.random.randn(d_model, hidden) * math.sqrt(2.0 / (d_model + hidden))
        self.b1 = np.zeros((hidden,))
        self.w2 = np.random.randn(hidden, d_model) * math.sqrt(2.0 / (hidden + d_model))
        self.b2 = np.zeros((d_model,))

    def forward(self, x: np.ndarray) -> np.ndarray:
        # x: (b, t, d_model)
        b, t, d = x.shape
        h = np.tensordot(x, self.w1, axes=([2], [0])) + self.b1  # (b,t,hidden)
        h = np.maximum(h, 0.0)  # ReLU
        out = np.tensordot(h, self.w2, axes=([2], [0])) + self.b2  # (b,t,d_model)
        return out


# Scaled Dot-Product Attention


class ScaledDotProductAttention:
    def forward(
        self,
        q: np.ndarray,
        k: np.ndarray,
        v: np.ndarray,
        mask: Optional[np.ndarray] = None,
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        q,k,v: shapes (b, n_head, seq_len, d_k)
        mask: optional boolean or 0/1 mask of shape (b, seq_len) or (b, 1, 1, seq_len)
        returns: context (b, n_head, seq_len, d_k), attn_weights (b, n_head, seq_len, seq_len)
        """
        b, n_head, seq_len, d_k = q.shape
        # scores: (b, n_head, seq_len, seq_len)
        scores = np.matmul(q, k.transpose(0, 1, 3, 2)) / math.sqrt(d_k)

        if mask is not None:
            # normalize mask to shape (b, 1, 1, seq_len) broadcasting over heads and queries
            if mask.ndim == 2:
                mask2 = mask[:, None, None, :]  # (b,1,1,seq_len)
            elif mask.ndim == 3:
                # if provided as (b, n_head, seq_len) or (b, 1, seq_len)
                mask2 = (
                    mask[:, None, :, :]
                    if mask.shape[1] != seq_len
                    else mask[:, None, None, :]
                )
            else:
                mask2 = mask
            # mask2==0 => masked
            scores = np.where(mask2 == 0, -1e9, scores)

        attn = _softmax(scores, axis=-1)  # (b, n_head, seq_len, seq_len)
        context = np.matmul(attn, v)  # (b, n_head, seq_len, d_k)
        return context, attn


# MultiHeadAttention


class MultiHeadAttention:
    def __init__(self, d_model: int, n_head: int, seed: Optional[int] = None):
        if d_model % n_head != 0:
            raise ValueError("d_model must be divisible by n_head")
        if seed is not None:
            np.random.seed(seed)
        self.d_model = d_model
        self.n_head = n_head
        self.d_k = d_model // n_head

        # weight matrices for q,k,v and output
        self.w_q = np.random.randn(d_model, d_model) * math.sqrt(
            2.0 / (d_model + d_model)
        )
        self.b_q = np.zeros((d_model,))
        self.w_k = np.random.randn(d_model, d_model) * math.sqrt(
            2.0 / (d_model + d_model)
        )
        self.b_k = np.zeros((d_model,))
        self.w_v = np.random.randn(d_model, d_model) * math.sqrt(
            2.0 / (d_model + d_model)
        )
        self.b_v = np.zeros((d_model,))
        self.w_out = np.random.randn(d_model, d_model) * math.sqrt(
            2.0 / (d_model + d_model)
        )
        self.b_out = np.zeros((d_model,))

        self.attn = ScaledDotProductAttention()

    def _linear(self, x: np.ndarray, W: np.ndarray, b: np.ndarray) -> np.ndarray:
        # x: (b, seq_len, d_model) -> (b, seq_len, d_model)
        return np.tensordot(x, W, axes=([2], [0])) + b

    def _split_heads(self, x: np.ndarray) -> np.ndarray:
        # x: (b, seq_len, d_model) -> (b, n_head, seq_len, d_k)
        b, seq_len, _ = x.shape
        return x.reshape(b, seq_len, self.n_head, self.d_k).transpose(0, 2, 1, 3)

    def _concat_heads(self, x: np.ndarray) -> np.ndarray:
        # x: (b, n_head, seq_len, d_k) -> (b, seq_len, d_model)
        b, n_head, seq_len, d_k = x.shape
        return x.transpose(0, 2, 1, 3).reshape(b, seq_len, n_head * d_k)

    def forward(
        self,
        query: np.ndarray,
        key: np.ndarray,
        value: np.ndarray,
        mask: Optional[np.ndarray] = None,
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        query/key/value: (b, seq_len, d_model)
        returns: out (b, seq_len, d_model), attn_weights (b, n_head, seq_len, seq_len)
        """
        q = self._linear(query, self.w_q, self.b_q)
        k = self._linear(key, self.w_k, self.b_k)
        v = self._linear(value, self.w_v, self.b_v)
        qh = self._split_heads(q)
        kh = self._split_heads(k)
        vh = self._split_heads(v)

        context, attn = self.attn.forward(qh, kh, vh, mask)
        concat = self._concat_heads(context)  # (b, seq_len, d_model)
        out = np.tensordot(concat, self.w_out, axes=([2], [0])) + self.b_out
        return out, attn


# LayerNorm


class LayerNorm:
    def __init__(self, d_model: int, eps: float = 1e-12):
        self.gamma = np.ones((d_model,))
        self.beta = np.zeros((d_model,))
        self.eps = eps

    def forward(self, x: np.ndarray) -> np.ndarray:
        # x: (b, seq_len, d_model)
        mean = np.mean(x, axis=-1, keepdims=True)
        var = np.mean((x - mean) ** 2, axis=-1, keepdims=True)
        x_norm = (x - mean) / np.sqrt(var + self.eps)
        return self.gamma * x_norm + self.beta


# TransformerEncoderLayer


class TransformerEncoderLayer:
    def __init__(
        self, d_model: int, n_head: int, hidden_dim: int, seed: Optional[int] = None
    ):
        self.self_attn = MultiHeadAttention(d_model, n_head, seed=seed)
        self.ffn = PositionwiseFeedForward(d_model, hidden_dim, seed=seed)
        self.norm1 = LayerNorm(d_model)
        self.norm2 = LayerNorm(d_model)

    def forward(self, x: np.ndarray, mask: Optional[np.ndarray] = None) -> np.ndarray:
        # Self-attention
        attn_out, _ = self.self_attn.forward(x, x, x, mask)  # (b, seq_len, d_model)
        x2 = self.norm1.forward(x + attn_out)
        ffn_out = self.ffn.forward(x2)
        x3 = self.norm2.forward(x2 + ffn_out)
        return x3


# TransformerEncoder (stack)


class TransformerEncoder:
    def __init__(
        self,
        d_model: int,
        n_head: int,
        hidden_dim: int,
        num_layers: int,
        seed: Optional[int] = None,
    ):
        self.layers = [
            TransformerEncoderLayer(d_model, n_head, hidden_dim, seed=seed)
            for _ in range(num_layers)
        ]

    def forward(self, x: np.ndarray, mask: Optional[np.ndarray] = None) -> np.ndarray:
        out = x
        for layer in self.layers:
            out = layer.forward(out, mask)
        return out


# AttentionPooling


class AttentionPooling:
    def __init__(self, d_model: int, seed: Optional[int] = None):
        if seed is not None:
            np.random.seed(seed)
        self.w = np.random.randn(d_model) * math.sqrt(2.0 / d_model)
        self.b = 0.0

    def forward(
        self, x: np.ndarray, mask: Optional[np.ndarray] = None
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        x: (b, seq_len, d_model)
        mask: (b, seq_len) where 1 = valid, 0 = pad
        returns: pooled (b, d_model), attn_weights (b, seq_len)
        """
        # raw scores: (b, seq_len)
        scores = np.tensordot(x, self.w, axes=([2], [0])) + self.b

        if mask is not None:
            scores = np.where(mask == 0, -1e9, scores)

        weights = _softmax(scores, axis=-1)  # (b, seq_len)
        pooled = np.matmul(weights[:, None, :], x).squeeze(1)  # (b, d_model)
        return pooled, weights


# EEGTransformer (forward-only)


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
    ):
        if seed is not None:
            np.random.seed(seed)
        self.feature_dim = feature_dim
        self.d_model = d_model
        self.task_type = task_type
        # input projection
        self.w_in = np.random.randn(feature_dim, d_model) * math.sqrt(
            2.0 / (feature_dim + d_model)
        )
        self.b_in = np.zeros((d_model,))
        # time embedding
        self.time2vec = Time2Vec(d_model, seed=seed)
        self.encoder = TransformerEncoder(
            d_model, n_head, hidden_dim, num_layers, seed=seed
        )
        self.pooling = AttentionPooling(d_model, seed=seed)
        # output
        self.w_out = np.random.randn(d_model, output_dim) * math.sqrt(
            2.0 / (d_model + output_dim)
        )
        self.b_out = np.zeros((output_dim,))

    def _input_proj(self, x: np.ndarray) -> np.ndarray:
        # x: (b, seq_len, feature_dim) -> (b, seq_len, d_model)
        return np.tensordot(x, self.w_in, axes=([2], [0])) + self.b_in

    def forward(
        self, x: np.ndarray, mask: Optional[np.ndarray] = None
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        x: (b, seq_len, feature_dim)
        mask: optional (b, seq_len) 1=valid,0=pad
        returns: out (b, output_dim), attn_weights_from_pooling (b, seq_len)
        """
        b, t, f = x.shape
        # time indices
        t_idx = np.arange(t, dtype=float)[None, :, None]  # (1,t,1)
        t_idx = np.tile(t_idx, (b, 1, 1))  # (b,t,1)
        time_emb = self.time2vec.forward(t_idx)  # (b,t,d_model)
        x_proj = self._input_proj(x) + time_emb  # broadcast add -> (b,t,d_model)
        enc = self.encoder.forward(x_proj, mask)
        pooled, attn_weights = self.pooling.forward(enc, mask)
        out = (
            np.tensordot(pooled, self.w_out, axes=([1], [0])) + self.b_out
        )  # (b,output_dim)
        if self.task_type == "classification":
            out = _softmax(out, axis=-1)
        return out, attn_weights


# Example usage

if __name__ == "__main__":
    # Example 1: Synthetic EEG-like array
    batch = 2
    seq_len = 10
    feature_dim = 8  # e.g., 8 channels
    rng = np.random.RandomState(42)
    X = rng.randn(batch, seq_len, feature_dim).astype(float)

    model = EEGTransformer(
        feature_dim=feature_dim,
        d_model=32,
        n_head=4,
        hidden_dim=64,
        num_layers=2,
        output_dim=1,
        seed=0,
    )
    out, attn_weights = model.forward(X)
    print("Output shape:", out.shape)
    print("Output:", out)
    print("Pooling attn shape:", attn_weights.shape)
    print("Pooling attn (per sample):", attn_weights)

    # Example 2: Loading EEG from a pandas DataFrame (CSV-like)
    # Suppose CSV has columns: time, ch1, ch2, ..., chN
    # We'll simulate a DataFrame first:
    channels = [f"ch{i}" for i in range(feature_dim)]
    # create a long single-trial dataframe with seq_len rows
    df = pd.DataFrame(rng.randn(seq_len, feature_dim), columns=channels)
    # convert to numpy trial (1, seq_len, feature_dim)
    trial_np = df[channels].values.reshape(1, seq_len, feature_dim)
    out2, attn2 = model.forward(trial_np)
    print("Single-trial output:", out2)
    print("Single-trial pooling attn:", attn2)
