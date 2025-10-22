from __future__ import annotations

import math

import numpy as np
import pandas as pd


# --------------------------------------------------
# Utility functions
# --------------------------------------------------
def _softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    x_max = np.max(x, axis=axis, keepdims=True)
    e = np.exp(x - x_max)
    return e / (np.sum(e, axis=axis, keepdims=True) + 1e-12)


def _stable_div(x: np.ndarray, denom: np.ndarray) -> np.ndarray:
    return x / (denom + 1e-12)


# --------------------------------------------------
# Time2Vec
# --------------------------------------------------
class Time2Vec:
    """Time2Vec positional encoding for real-valued time steps."""

    def __init__(self, d_model: int, seed: int | None = None):
        if d_model < 2:
            raise ValueError("d_model must be >= 2 for Time2Vec")
        self.rng = np.random.default_rng(seed)
        self.w0 = self.rng.standard_normal((1, 1))
        self.b0 = self.rng.standard_normal((1, 1))
        self.w = self.rng.standard_normal((1, d_model - 1))
        self.b = self.rng.standard_normal((1, d_model - 1))

    def forward(self, time_steps: np.ndarray) -> np.ndarray:
        """time_steps: (batch, seq_len, 1) or (batch, seq_len)."""
        ts = time_steps if time_steps.ndim == 3 else time_steps[..., None]
        linear = (self.w0 * ts) + self.b0
        periodic = np.sin((ts * self.w) + self.b)
        return np.concatenate([linear, periodic], axis=-1)


# --------------------------------------------------
# Positionwise FeedForward
# --------------------------------------------------
class PositionwiseFeedForward:
    def __init__(self, d_model: int, hidden: int, drop_prob: float = 0.0, seed: int | None = None):
        self.rng = np.random.default_rng(seed)
        self.w1 = self.rng.standard_normal((d_model, hidden)) * math.sqrt(2.0 / (d_model + hidden))
        self.b1 = np.zeros(hidden)
        self.w2 = self.rng.standard_normal((hidden, d_model)) * math.sqrt(2.0 / (hidden + d_model))
        self.b2 = np.zeros(d_model)

    def forward(self, x: np.ndarray) -> np.ndarray:
        h = np.tensordot(x, self.w1, axes=([2], [0])) + self.b1
        h = np.maximum(h, 0.0)
        return np.tensordot(h, self.w2, axes=([2], [0])) + self.b2


# --------------------------------------------------
# Scaled Dot-Product Attention
# --------------------------------------------------
class ScaledDotProductAttention:
    def forward(
        self,
        q: np.ndarray,
        k: np.ndarray,
        v: np.ndarray,
        mask: np.ndarray | None = None,
    ) -> tuple[np.ndarray, np.ndarray]:
        b, n_head, seq_len, d_k = q.shape
        scores = np.matmul(q, k.transpose(0, 1, 3, 2)) / math.sqrt(d_k)

        if mask is not None:
            mask2 = mask[:, None, None, :] if mask.ndim == 2 else mask
            scores = np.where(mask2 == 0, -1e9, scores)

        attn = _softmax(scores, axis=-1)
        context = np.matmul(attn, v)
        return context, attn


# --------------------------------------------------
# Multi-Head Attention
# --------------------------------------------------
class MultiHeadAttention:
    def __init__(self, d_model: int, n_head: int, seed: int | None = None):
        if d_model % n_head != 0:
            raise ValueError("d_model must be divisible by n_head")

        self.d_model = d_model
        self.n_head = n_head
        self.d_k = d_model // n_head
        self.rng = np.random.default_rng(seed)

        self.w_q = self.rng.standard_normal((d_model, d_model)) * math.sqrt(2.0 / (2 * d_model))
        self.b_q = np.zeros(d_model)
        self.w_k = self.rng.standard_normal((d_model, d_model)) * math.sqrt(2.0 / (2 * d_model))
        self.b_k = np.zeros(d_model)
        self.w_v = self.rng.standard_normal((d_model, d_model)) * math.sqrt(2.0 / (2 * d_model))
        self.b_v = np.zeros(d_model)
        self.w_out = self.rng.standard_normal((d_model, d_model)) * math.sqrt(2.0 / (2 * d_model))
        self.b_out = np.zeros(d_model)

        self.attn = ScaledDotProductAttention()

    def _linear(self, x: np.ndarray, w: np.ndarray, b: np.ndarray) -> np.ndarray:
        return np.tensordot(x, w, axes=([2], [0])) + b

    def _split_heads(self, x: np.ndarray) -> np.ndarray:
        b, seq_len, _ = x.shape
        return x.reshape(b, seq_len, self.n_head, self.d_k).transpose(0, 2, 1, 3)

    def _concat_heads(self, x: np.ndarray) -> np.ndarray:
        b, n_head, seq_len, d_k = x.shape
        return x.transpose(0, 2, 1, 3).reshape(b, seq_len, n_head * d_k)

    def forward(
        self,
        query: np.ndarray,
        key: np.ndarray,
        value: np.ndarray,
        mask: np.ndarray | None = None,
    ) -> tuple[np.ndarray, np.ndarray]:
        q = self._linear(query, self.w_q, self.b_q)
        k = self._linear(key, self.w_k, self.b_k)
        v = self._linear(value, self.w_v, self.b_v)
        qh, kh, vh = self._split_heads(q), self._split_heads(k), self._split_heads(v)
        context, attn = self.attn.forward(qh, kh, vh, mask)
        concat = self._concat_heads(context)
        out = np.tensordot(concat, self.w_out, axes=([2], [0])) + self.b_out
        return out, attn


# --------------------------------------------------
# Layer Normalization
# --------------------------------------------------
class LayerNorm:
    def __init__(self, d_model: int, eps: float = 1e-12):
        self.gamma = np.ones(d_model)
        self.beta = np.zeros(d_model)
        self.eps = eps

    def forward(self, x: np.ndarray) -> np.ndarray:
        mean = np.mean(x, axis=-1, keepdims=True)
        var = np.mean((x - mean) ** 2, axis=-1, keepdims=True)
        x_norm = (x - mean) / np.sqrt(var + self.eps)
        return self.gamma * x_norm + self.beta


# --------------------------------------------------
# Transformer Encoder Layer
# --------------------------------------------------
class TransformerEncoderLayer:
    def __init__(self, d_model: int, n_head: int, hidden_dim: int, seed: int | None = None):
        self.self_attn = MultiHeadAttention(d_model, n_head, seed=seed)
        self.ffn = PositionwiseFeedForward(d_model, hidden_dim, seed=seed)
        self.norm1 = LayerNorm(d_model)
        self.norm2 = LayerNorm(d_model)

    def forward(self, x: np.ndarray, mask: np.ndarray | None = None) -> np.ndarray:
        attn_out, _ = self.self_attn.forward(x, x, x, mask)
        x2 = self.norm1.forward(x + attn_out)
        ffn_out = self.ffn.forward(x2)
        return self.norm2.forward(x2 + ffn_out)


# --------------------------------------------------
# Transformer Encoder Stack
# --------------------------------------------------
class TransformerEncoder:
    def __init__(self, d_model: int, n_head: int, hidden_dim: int, num_layers: int, seed: int | None = None):
        self.layers = [TransformerEncoderLayer(d_model, n_head, hidden_dim, seed=seed) for _ in range(num_layers)]

    def forward(self, x: np.ndarray, mask: np.ndarray | None = None) -> np.ndarray:
        out = x
        for layer in self.layers:
            out = layer.forward(out, mask)
        return out


# --------------------------------------------------
# Attention Pooling
# --------------------------------------------------
class AttentionPooling:
    def __init__(self, d_model: int, seed: int | None = None):
        self.rng = np.random.default_rng(seed)
        self.w = self.rng.standard_normal(d_model) * math.sqrt(2.0 / d_model)
        self.b = 0.0

    def forward(self, x: np.ndarray, mask: np.ndarray | None = None) -> tuple[np.ndarray, np.ndarray]:
        scores = np.tensordot(x, self.w, axes=([2], [0])) + self.b
        if mask is not None:
            scores = np.where(mask == 0, -1e9, scores)
        weights = _softmax(scores, axis=-1)
        pooled = np.matmul(weights[:, None, :], x).squeeze(1)
        return pooled, weights


# --------------------------------------------------
# EEG Transformer (forward-only)
# --------------------------------------------------
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
        seed: int | None = None,
    ):
        self.rng = np.random.default_rng(seed)
        self.feature_dim = feature_dim
        self.d_model = d_model
        self.task_type = task_type

        self.w_in = self.rng.standard_normal((feature_dim, d_model)) * math.sqrt(2.0 / (feature_dim + d_model))
        self.b_in = np.zeros(d_model)
        self.time2vec = Time2Vec(d_model, seed=seed)
        self.encoder = TransformerEncoder(d_model, n_head, hidden_dim, num_layers, seed=seed)
        self.pooling = AttentionPooling(d_model, seed=seed)
        self.w_out = self.rng.standard_normal((d_model, output_dim)) * math.sqrt(2.0 / (d_model + output_dim))
        self.b_out = np.zeros(output_dim)

    def _input_proj(self, x: np.ndarray) -> np.ndarray:
        return np.tensordot(x, self.w_in, axes=([2], [0])) + self.b_in

    def forward(self, x: np.ndarray, mask: np.ndarray | None = None) -> tuple[np.ndarray, np.ndarray]:
        b, t, _ = x.shape
        t_idx = np.arange(t, dtype=float)[None, :, None]
        t_idx = np.tile(t_idx, (b, 1, 1))
        time_emb = self.time2vec.forward(t_idx)
        x_proj = self._input_proj(x) + time_emb
        enc = self.encoder.forward(x_proj, mask)
        pooled, attn_weights = self.pooling.forward(enc, mask)
        out = np.tensordot(pooled, self.w_out, axes=([1], [0])) + self.b_out
        if self.task_type == "classification":
            out = _softmax(out, axis=-1)
        return out, attn_weights


# --------------------------------------------------
# Example usage
# --------------------------------------------------
if __name__ == "__main__":
    batch, seq_len, feature_dim = 2, 10, 8
    rng = np.random.default_rng(42)
    X = rng.standard_normal((batch, seq_len, feature_dim))

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

    # Example with pandas DataFrame
    channels = [f"ch{i}" for i in range(feature_dim)]
    df = pd.DataFrame(rng.standard_normal((seq_len, feature_dim)), columns=channels)
    trial_np = df[channels].to_numpy().reshape(1, seq_len, feature_dim)
    out2, attn2 = model.forward(trial_np)
    print("Single-trial output:", out2)
    print("Single-trial pooling attn:", attn2)
