#imports
import torch
import torch.nn as nn
import math
#Time2Vec layer for positional encoding of real-time data like EEG
class Time2Vec(nn.Module):
    #Encodes time steps into a continuous embedding space so to help the transformer learn temporal dependencies.
    def __init__(self, d_model):
        super().__init__()
        self.w0 = nn.Parameter(torch.randn(1, 1))
        self.b0 = nn.Parameter(torch.randn(1, 1))
        self.w = nn.Parameter(torch.randn(1, d_model - 1))
        self.b = nn.Parameter(torch.randn(1, d_model - 1))

    def forward(self, t):
        linear = self.w0 * t + self.b0           
        periodic = torch.sin(self.w * t + self.b)    
        return torch.cat([linear, periodic], dim=-1) 
      
#positionwise feedforward network
class PositionwiseFeedForward(nn.Module):
    def __init__(self, d_model, hidden, drop_prob=0.1):
        super().__init__()
        self.fc1 = nn.Linear(d_model, hidden)
        self.fc2 = nn.Linear(hidden, d_model)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(drop_prob)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.dropout(x)
        return self.fc2(x)
#scaled dot product attention
class ScaleDotProductAttention(nn.Module):
    def __init__(self):
        super().__init__()
        self.softmax = nn.Softmax(dim=-1)

    def forward(self, q, k, v, mask=None):
        _, _, _, d_k = k.size()
        scores = (q @ k.transpose(2, 3)) / math.sqrt(d_k)

        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)

        attn = self.softmax(scores)
        context = attn @ v
        return context, attn
#multi head attention
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, n_head):
        super().__init__()
        self.n_head = n_head
        self.attn = ScaleDotProductAttention()
        self.w_q = nn.Linear(d_model, d_model)
        self.w_k = nn.Linear(d_model, d_model)
        self.w_v = nn.Linear(d_model, d_model)
        self.w_out = nn.Linear(d_model, d_model)

    def forward(self, q, k, v, mask=None):
        q, k, v = self.w_q(q), self.w_k(k), self.w_v(v)
        q, k, v = self.split_heads(q), self.split_heads(k), self.split_heads(v)

        context, _ = self.attn(q, k, v, mask)
        out = self.w_out(self.concat_heads(context))
        return out

    def split_heads(self, x):
        batch, seq_len, d_model = x.size()
        d_k = d_model // self.n_head
        return x.view(batch, seq_len, self.n_head, d_k).transpose(1, 2)

    def concat_heads(self, x):
        batch, n_head, seq_len, d_k = x.size()
        return x.transpose(1, 2).contiguous().view(batch, seq_len, n_head * d_k)

#Layer normalization
class LayerNorm(nn.Module):
    def __init__(self, d_model, eps=1e-12):
        super().__init__()
        self.gamma = nn.Parameter(torch.ones(d_model))
        self.beta = nn.Parameter(torch.zeros(d_model))
        self.eps = eps

    def forward(self, x):
        mean = x.mean(-1, keepdim=True)
        var = x.var(-1, unbiased=False, keepdim=True)
        return self.gamma * (x - mean) / torch.sqrt(var + self.eps) + self.beta

#transformer encoder layer
class TransformerEncoderLayer(nn.Module):
    def __init__(self, d_model, n_head, hidden_dim, drop_prob=0.1):
        super().__init__()
        self.self_attn = MultiHeadAttention(d_model, n_head)
        self.ffn = PositionwiseFeedForward(d_model, hidden_dim, drop_prob)
        self.norm1 = LayerNorm(d_model)
        self.norm2 = LayerNorm(d_model)
        self.dropout = nn.Dropout(drop_prob)

    def forward(self, x, mask=None):
        attn_out = self.self_attn(x, x, x, mask)
        x = self.norm1(x + self.dropout(attn_out))
        ffn_out = self.ffn(x)
        x = self.norm2(x + self.dropout(ffn_out))

        return x

#encoder stack
class TransformerEncoder(nn.Module):
    def __init__(self, d_model, n_head, hidden_dim, num_layers, drop_prob=0.1):
        super().__init__()
        self.layers = nn.ModuleList([
            TransformerEncoderLayer(d_model, n_head, hidden_dim, drop_prob)
            for _ in range(num_layers)
        ])

    def forward(self, x, mask=None):
        for layer in self.layers:
            x = layer(x, mask)
        return x


#attention pooling layer
class AttentionPooling(nn.Module):
    def __init__(self, d_model):
        super().__init__()
        self.attn_score = nn.Linear(d_model, 1)

    def forward(self, x, mask=None):
        attn_weights = torch.softmax(self.attn_score(x).squeeze(-1), dim=-1)

        if mask is not None:
            attn_weights = attn_weights.masked_fill(mask == 0, 0)
            attn_weights = attn_weights / (attn_weights.sum(dim=1, keepdim=True) + 1e-8)

        pooled = torch.bmm(attn_weights.unsqueeze(1), x).squeeze(1)
        return pooled, attn_weights

# transformer model

class EEGTransformer(nn.Module):

    def __init__(self, feature_dim, d_model=128, n_head=8, hidden_dim=512,
                 num_layers=4, drop_prob=0.1, output_dim=1, task_type='regression'):
        super().__init__()
        self.task_type = task_type
        self.input_proj = nn.Linear(feature_dim, d_model)

        # Time encoding for temporal understanding
        self.time2vec = Time2Vec(d_model)

        # Transformer encoder for sequence modeling
        self.encoder = TransformerEncoder(d_model, n_head, hidden_dim, num_layers, drop_prob)

        # Attention pooling to summarize time dimension
        self.pooling = AttentionPooling(d_model)

        # Final output layer
        self.output_layer = nn.Linear(d_model, output_dim)

    def forward(self, x, mask=None):

        b, t, _ = x.size()

        # Create time indices and embed them
        t_idx = torch.arange(t, device=x.device).view(1, t, 1).expand(b, t, 1).float()
        time_emb = self.time2vec(t_idx)

        # Add time embedding to feature projection
        x = self.input_proj(x) + time_emb

        # Pass through the Transformer encoder
        x = self.encoder(x, mask)

        # Aggregate features across time with attention
        pooled, attn_weights = self.pooling(x, mask)

        # Final output (regression or classification)
        out = self.output_layer(pooled)

        if self.task_type == 'classification':
            out = torch.softmax(out, dim=-1)

        return out, attn_weights
