import math

import torch
from torch import Tensor, nn


class Time2Vec(nn.Module):
    """
    Time2Vec layer for positional encoding of real-time data like EEG.

    >>> import torch
    >>> layer = Time2Vec(4)
    >>> t = torch.ones(1, 3, 1)
    >>> output = layer.forward(t)
    >>> output.shape
    torch.Size([1, 3, 4])
    """

    def __init__(self, d_model: int) -> None:
        super().__init__()
        self.w0 = nn.Parameter(torch.randn(1, 1))
        self.b0 = nn.Parameter(torch.randn(1, 1))
        self.w = nn.Parameter(torch.randn(1, d_model - 1))
        self.b = nn.Parameter(torch.randn(1, d_model - 1))

    def forward(self, time_steps: Tensor) -> Tensor:
        linear = self.w0 * time_steps + self.b0
        periodic = torch.sin(self.w * time_steps + self.b)
        return torch.cat([linear, periodic], dim=-1)


class PositionwiseFeedForward(nn.Module):
    """
    Positionwise feedforward network.

    >>> import torch
    >>> layer = PositionwiseFeedForward(8, 16)
    >>> x = torch.rand(4, 10, 8)
    >>> out = layer.forward(x)
    >>> out.shape
    torch.Size([4, 10, 8])
    """

    def __init__(self, d_model: int, hidden: int, drop_prob: float = 0.1) -> None:
        super().__init__()
        self.fc1 = nn.Linear(d_model, hidden)
        self.fc2 = nn.Linear(hidden, d_model)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(drop_prob)

    def forward(self, input_tensor: Tensor) -> Tensor:
        x = self.fc1(input_tensor)
        x = self.relu(x)
        x = self.dropout(x)
        return self.fc2(x)


class ScaleDotProductAttention(nn.Module):
    """
    Scaled dot product attention.

    >>> import torch
    >>> attn = ScaleDotProductAttention()
    >>> query_tensor = torch.rand(2, 8, 10, 16)
    >>> key_tensor = torch.rand(2, 8, 10, 16)
    >>> value_tensor = torch.rand(2, 8, 10, 16)
    >>> ctx, attn_w = attn.forward(query_tensor, key_tensor, value_tensor)
    >>> ctx.shape
    torch.Size([2, 8, 10, 16])
    """

    def __init__(self) -> None:
        super().__init__()
        self.softmax = nn.Softmax(dim=-1)

    def forward(
        self,
        query_tensor: Tensor,
        key_tensor: Tensor,
        value_tensor: Tensor,
        mask: Tensor = None,
    ) -> tuple[Tensor, Tensor]:
        _, _, _, d_k = key_tensor.size()
        scores = (query_tensor @ key_tensor.transpose(2, 3)) / math.sqrt(d_k)

        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)

        attn = self.softmax(scores)
        context = attn @ value_tensor
        return context, attn


class MultiHeadAttention(nn.Module):
    """
    Multi-head attention.

    >>> import torch
    >>> attn = MultiHeadAttention(16, 4)
    >>> query_tensor = torch.rand(2, 10, 16)
    >>> out = attn.forward(query_tensor, query_tensor, query_tensor)
    >>> out.shape
    torch.Size([2, 10, 16])
    """

    def __init__(self, d_model: int, n_head: int) -> None:
        super().__init__()
        self.n_head = n_head
        self.attn = ScaleDotProductAttention()
        self.w_q = nn.Linear(d_model, d_model)
        self.w_k = nn.Linear(d_model, d_model)
        self.w_v = nn.Linear(d_model, d_model)
        self.w_out = nn.Linear(d_model, d_model)

    def forward(
        self,
        query_tensor: Tensor,
        key_tensor: Tensor,
        value_tensor: Tensor,
        mask: Tensor = None,
    ) -> Tensor:
        query_tensor, key_tensor, value_tensor = (
            self.w_q(query_tensor),
            self.w_k(key_tensor),
            self.w_v(value_tensor),
        )
        query_tensor = self.split_heads(query_tensor)
        key_tensor = self.split_heads(key_tensor)
        value_tensor = self.split_heads(value_tensor)

        context, _ = self.attn(query_tensor, key_tensor, value_tensor, mask)
        out = self.w_out(self.concat_heads(context))
        return out

    def split_heads(self, input_tensor: Tensor) -> Tensor:
        batch, seq_len, d_model = input_tensor.size()
        d_k = d_model // self.n_head
        return input_tensor.view(batch, seq_len, self.n_head, d_k).transpose(1, 2)

    def concat_heads(self, input_tensor: Tensor) -> Tensor:
        batch, n_head, seq_len, d_k = input_tensor.size()
        return (
            input_tensor.transpose(1, 2).contiguous().view(batch, seq_len, n_head * d_k)
        )


class LayerNorm(nn.Module):
    """
    Layer normalization.

    >>> import torch
    >>> ln = LayerNorm(8)
    >>> x = torch.rand(4, 10, 8)
    >>> out = ln.forward(x)
    >>> out.shape
    torch.Size([4, 10, 8])
    """

    def __init__(self, d_model: int, eps: float = 1e-12) -> None:
        super().__init__()
        self.gamma = nn.Parameter(torch.ones(d_model))
        self.beta = nn.Parameter(torch.zeros(d_model))
        self.eps = eps

    def forward(self, input_tensor: Tensor) -> Tensor:
        mean = input_tensor.mean(-1, keepdim=True)
        var = input_tensor.var(-1, unbiased=False, keepdim=True)
        return (
            self.gamma * (input_tensor - mean) / torch.sqrt(var + self.eps) + self.beta
        )


class TransformerEncoderLayer(nn.Module):
    """
    Transformer encoder layer.

    >>> import torch
    >>> layer = TransformerEncoderLayer(8, 2, 16)
    >>> x = torch.rand(4, 10, 8)
    >>> out = layer.forward(x)
    >>> out.shape
    torch.Size([4, 10, 8])
    """

    def __init__(
        self,
        d_model: int,
        n_head: int,
        hidden_dim: int,
        drop_prob: float = 0.1,
    ) -> None:
        super().__init__()
        self.self_attn = MultiHeadAttention(d_model, n_head)
        self.ffn = PositionwiseFeedForward(d_model, hidden_dim, drop_prob)
        self.norm1 = LayerNorm(d_model)
        self.norm2 = LayerNorm(d_model)
        self.dropout = nn.Dropout(drop_prob)

    def forward(self, input_tensor: Tensor, mask: Tensor = None) -> Tensor:
        attn_out = self.self_attn(input_tensor, input_tensor, input_tensor, mask)
        x = self.norm1(input_tensor + self.dropout(attn_out))
        ffn_out = self.ffn(x)
        x = self.norm2(x + self.dropout(ffn_out))
        return x


class TransformerEncoder(nn.Module):
    """
    Encoder stack.

    >>> import torch
    >>> enc = TransformerEncoder(8, 2, 16, 2)
    >>> x = torch.rand(4, 10, 8)
    >>> out = enc.forward(x)
    >>> out.shape
    torch.Size([4, 10, 8])
    """

    def __init__(
        self,
        d_model: int,
        n_head: int,
        hidden_dim: int,
        num_layers: int,
        drop_prob: float = 0.1,
    ) -> None:
        super().__init__()
        self.layers = nn.ModuleList(
            [
                TransformerEncoderLayer(d_model, n_head, hidden_dim, drop_prob)
                for _ in range(num_layers)
            ]
        )

    def forward(self, input_tensor: Tensor, mask: Tensor = None) -> Tensor:
        x = input_tensor
        for layer in self.layers:
            x = layer(x, mask)
        return x


class AttentionPooling(nn.Module):
    """
    Attention pooling layer.

    >>> import torch
    >>> pooling = AttentionPooling(8)
    >>> x = torch.rand(4, 10, 8)
    >>> pooled, weights = pooling.forward(x)
    >>> pooled.shape
    torch.Size([4, 8])
    >>> weights.shape
    torch.Size([4, 10])
    """

    def __init__(self, d_model: int) -> None:
        super().__init__()
        self.attn_score = nn.Linear(d_model, 1)

    def forward(
        self, input_tensor: Tensor, mask: Tensor = None
    ) -> tuple[Tensor, Tensor]:
        attn_weights = torch.softmax(self.attn_score(input_tensor).squeeze(-1), dim=-1)

        if mask is not None:
            attn_weights = attn_weights.masked_fill(mask == 0, 0)
            attn_weights = attn_weights / (attn_weights.sum(dim=1, keepdim=True) + 1e-8)

        pooled = torch.bmm(attn_weights.unsqueeze(1), input_tensor).squeeze(1)
        return pooled, attn_weights


class EEGTransformer(nn.Module):
    """
    EEG Transformer model.

    >>> import torch
    >>> model = EEGTransformer(feature_dim=8)
    >>> x = torch.rand(2, 10, 8)
    >>> out, attn_w = model.forward(x)
    >>> out.shape
    torch.Size([2, 1])
    """

    def __init__(
        self,
        feature_dim: int,
        d_model: int = 128,
        n_head: int = 8,
        hidden_dim: int = 512,
        num_layers: int = 4,
        drop_prob: float = 0.1,
        output_dim: int = 1,
        task_type: str = "regression",
    ) -> None:
        super().__init__()
        self.task_type = task_type
        self.input_proj = nn.Linear(feature_dim, d_model)
        self.time2vec = Time2Vec(d_model)
        self.encoder = TransformerEncoder(
            d_model, n_head, hidden_dim, num_layers, drop_prob
        )
        self.pooling = AttentionPooling(d_model)
        self.output_layer = nn.Linear(d_model, output_dim)

    def forward(
        self, input_tensor: Tensor, mask: Tensor = None
    ) -> tuple[Tensor, Tensor]:
        b, t, _ = input_tensor.size()
        t_idx = (
            torch.arange(t, device=input_tensor.device)
            .view(1, t, 1)
            .expand(b, t, 1)
            .float()
        )
        time_emb = self.time2vec(t_idx)
        x = self.input_proj(input_tensor) + time_emb
        x = self.encoder(x, mask)
        pooled, attn_weights = self.pooling(x, mask)
        out = self.output_layer(pooled)
        if self.task_type == "classification":
            out = torch.softmax(out, dim=-1)
        return out, attn_weights
