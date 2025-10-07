"""
Vision Transformer (ViT) Implementation

This module contains a PyTorch implementation of the Vision Transformer (ViT) 
architecture based on the paper "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale".

Key Components:
- Patch Embedding
- Multi-Head Self Attention
- MLP Block
- Transformer Encoder
- Vision Transformer Model
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import Tensor
from typing import Optional, Tuple
import math


class PatchEmbedding(nn.Module):
    """
    Creates patch embeddings from input images as described in Equation 1 of ViT paper.
    
    Args:
        img_size (int): Size of input image (assumed square)
        patch_size (int): Size of each patch (assumed square)
        in_channels (int): Number of input channels
        embed_dim (int): Dimension of embedding
    """
    
    def __init__(self, img_size: int = 224, patch_size: int = 16, in_channels: int = 3, embed_dim: int = 768):
        super().__init__()
        self.img_size = img_size
        self.patch_size = patch_size
        self.n_patches = (img_size // patch_size) ** 2
        
        self.proj = nn.Conv2d(
            in_channels=in_channels,
            out_channels=embed_dim,
            kernel_size=patch_size,
            stride=patch_size
        )
        
    def forward(self, x: Tensor) -> Tensor:
        """
        Forward pass for patch embedding.
        
        Args:
            x (Tensor): Input tensor of shape (B, C, H, W)
            
        Returns:
            Tensor: Patch embeddings of shape (B, n_patches, embed_dim)
        """
        x = self.proj(x)  # (B, embed_dim, H//patch_size, W//patch_size)
        x = x.flatten(2)  # (B, embed_dim, n_patches)
        x = x.transpose(1, 2)  # (B, n_patches, embed_dim)
        return x


class MultiHeadSelfAttention(nn.Module):
    """
    Multi-Head Self Attention (MSA) block as described in Equation 2 of ViT paper.
    
    Args:
        embed_dim (int): Dimension of embedding
        num_heads (int): Number of attention heads
        dropout (float): Dropout rate
    """
    
    def __init__(self, embed_dim: int = 768, num_heads: int = 12, dropout: float = 0.0):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads
        
        assert self.head_dim * num_heads == embed_dim, "embed_dim must be divisible by num_heads"
        
        self.qkv = nn.Linear(embed_dim, embed_dim * 3)
        self.attn_dropout = nn.Dropout(dropout)
        self.proj = nn.Linear(embed_dim, embed_dim)
        self.proj_dropout = nn.Dropout(dropout)
        
    def forward(self, x: Tensor) -> Tensor:
        """
        Forward pass for multi-head self attention.
        
        Args:
            x (Tensor): Input tensor of shape (B, n_patches, embed_dim)
            
        Returns:
            Tensor: Output tensor of same shape as input
        """
        B, N, C = x.shape
        
        # Create Q, K, V
        qkv = self.qkv(x).reshape(B, N, 3, self.num_heads, self.head_dim).permute(2, 0, 3, 1, 4)
        q, k, v = qkv[0], qkv[1], qkv[2]  # (B, num_heads, N, head_dim)
        
        # Scaled dot-product attention
        attn = (q @ k.transpose(-2, -1)) * (self.head_dim ** -0.5)  # (B, num_heads, N, N)
        attn = F.softmax(attn, dim=-1)
        attn = self.attn_dropout(attn)
        
        # Apply attention to values
        x = (attn @ v).transpose(1, 2).reshape(B, N, C)  # (B, N, embed_dim)
        
        # Projection
        x = self.proj(x)
        x = self.proj_dropout(x)
        
        return x


class MLPBlock(nn.Module):
    """
    Multilayer Perceptron (MLP) block as described in Equation 3 of ViT paper.
    
    Args:
        embed_dim (int): Dimension of embedding
        mlp_ratio (float): Ratio of MLP hidden dimension to embed_dim
        dropout (float): Dropout rate
    """
    
    def __init__(self, embed_dim: int = 768, mlp_ratio: float = 4.0, dropout: float = 0.0):
        super().__init__()
        hidden_dim = int(embed_dim * mlp_ratio)
        
        self.fc1 = nn.Linear(embed_dim, hidden_dim)
        self.act = nn.GELU()
        self.fc2 = nn.Linear(hidden_dim, embed_dim)
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, x: Tensor) -> Tensor:
        """
        Forward pass for MLP block.
        
        Args:
            x (Tensor): Input tensor of shape (B, n_patches, embed_dim)
            
        Returns:
            Tensor: Output tensor of same shape as input
        """
        x = self.fc1(x)
        x = self.act(x)
        x = self.dropout(x)
        x = self.fc2(x)
        x = self.dropout(x)
        return x


class TransformerEncoderBlock(nn.Module):
    """
    Transformer Encoder Block combining MSA and MLP with residual connections.
    
    Args:
        embed_dim (int): Dimension of embedding
        num_heads (int): Number of attention heads
        mlp_ratio (float): Ratio of MLP hidden dimension to embed_dim
        dropout (float): Dropout rate
    """
    
    def __init__(self, embed_dim: int = 768, num_heads: int = 12, mlp_ratio: float = 4.0, dropout: float = 0.1):
        super().__init__()
        
        self.norm1 = nn.LayerNorm(embed_dim)
        self.attn = MultiHeadSelfAttention(embed_dim, num_heads, dropout)
        self.norm2 = nn.LayerNorm(embed_dim)
        self.mlp = MLPBlock(embed_dim, mlp_ratio, dropout)
        
    def forward(self, x: Tensor) -> Tensor:
        """
        Forward pass for transformer encoder block.
        
        Args:
            x (Tensor): Input tensor of shape (B, n_patches, embed_dim)
            
        Returns:
            Tensor: Output tensor of same shape as input
        """
        # Multi-head self attention with residual connection
        x = x + self.attn(self.norm1(x))
        
        # MLP with residual connection
        x = x + self.mlp(self.norm2(x))
        
        return x


class VisionTransformer(nn.Module):
    """
    Vision Transformer (ViT) model.
    
    Args:
        img_size (int): Input image size
        patch_size (int): Patch size
        in_channels (int): Number of input channels
        num_classes (int): Number of output classes
        embed_dim (int): Embedding dimension
        depth (int): Number of transformer blocks
        num_heads (int): Number of attention heads
        mlp_ratio (float): Ratio of MLP hidden dimension to embed_dim
        dropout (float): Dropout rate
        emb_dropout (float): Embedding dropout rate
    """
    
    def __init__(
        self,
        img_size: int = 224,
        patch_size: int = 16,
        in_channels: int = 3,
        num_classes: int = 1000,
        embed_dim: int = 768,
        depth: int = 12,
        num_heads: int = 12,
        mlp_ratio: float = 4.0,
        dropout: float = 0.1,
        emb_dropout: float = 0.1
    ):
        super().__init__()
        
        self.img_size = img_size
        self.patch_size = patch_size
        self.in_channels = in_channels
        
        # Patch embedding
        self.patch_embed = PatchEmbedding(img_size, patch_size, in_channels, embed_dim)
        n_patches = self.patch_embed.n_patches
        
        # Class token and position embedding
        self.cls_token = nn.Parameter(torch.zeros(1, 1, embed_dim))
        self.pos_embed = nn.Parameter(torch.zeros(1, n_patches + 1, embed_dim))
        self.pos_dropout = nn.Dropout(emb_dropout)
        
        # Transformer encoder blocks
        self.blocks = nn.ModuleList([
            TransformerEncoderBlock(embed_dim, num_heads, mlp_ratio, dropout)
            for _ in range(depth)
        ])
        
        # Layer normalization and classifier
        self.norm = nn.LayerNorm(embed_dim)
        self.head = nn.Linear(embed_dim, num_classes)
        
        # Initialize weights
        self._init_weights()
        
    def _init_weights(self):
        """Initialize weights for the ViT model."""
        # Initialize patch embedding like a linear layer
        nn.init.xavier_uniform_(self.patch_embed.proj.weight)
        if self.patch_embed.proj.bias is not None:
            nn.init.zeros_(self.patch_embed.proj.bias)
            
        # Initialize class token and position embedding
        nn.init.trunc_normal_(self.cls_token, std=0.02)
        nn.init.trunc_normal_(self.pos_embed, std=0.02)
        
        # Initialize linear layers
        self.apply(self._init_linear_weights)
        
    def _init_linear_weights(self, module):
        """Initialize weights for linear layers."""
        if isinstance(module, nn.Linear):
            nn.init.trunc_normal_(module.weight, std=0.02)
            if module.bias is not None:
                nn.init.zeros_(module.bias)
                
    def forward(self, x: Tensor) -> Tensor:
        """
        Forward pass for Vision Transformer.
        
        Args:
            x (Tensor): Input tensor of shape (B, C, H, W)
            
        Returns:
            Tensor: Output logits of shape (B, num_classes)
        """
        B = x.shape[0]
        
        # Create patch embeddings
        x = self.patch_embed(x)  # (B, n_patches, embed_dim)
        
        # Add class token
        cls_tokens = self.cls_token.expand(B, -1, -1)  # (B, 1, embed_dim)
        x = torch.cat((cls_tokens, x), dim=1)  # (B, n_patches + 1, embed_dim)
        
        # Add position embedding and apply dropout
        x = x + self.pos_embed
        x = self.pos_dropout(x)
        
        # Apply transformer blocks
        for block in self.blocks:
            x = block(x)
            
        # Apply final normalization and get class token output
        x = self.norm(x)
        cls_token_final = x[:, 0]  # Use class token for classification
        
        # Classifier
        x = self.head(cls_token_final)
        
        return x


def create_vit_model(
    img_size: int = 224,
    patch_size: int = 16,
    in_channels: int = 3,
    num_classes: int = 1000,
    embed_dim: int = 768,
    depth: int = 12,
    num_heads: int = 12,
    mlp_ratio: float = 4.0,
    dropout: float = 0.1,
    emb_dropout: float = 0.1
) -> VisionTransformer:
    """
    Factory function to create a Vision Transformer model.
    
    Args:
        img_size (int): Input image size
        patch_size (int): Patch size
        in_channels (int): Number of input channels
        num_classes (int): Number of output classes
        embed_dim (int): Embedding dimension
        depth (int): Number of transformer blocks
        num_heads (int): Number of attention heads
        mlp_ratio (float): Ratio of MLP hidden dimension to embed_dim
        dropout (float): Dropout rate
        emb_dropout (float): Embedding dropout rate
        
    Returns:
        VisionTransformer: Configured ViT model
    """
    return VisionTransformer(
        img_size=img_size,
        patch_size=patch_size,
        in_channels=in_channels,
        num_classes=num_classes,
        embed_dim=embed_dim,
        depth=depth,
        num_heads=num_heads,
        mlp_ratio=mlp_ratio,
        dropout=dropout,
        emb_dropout=emb_dropout
    )





def count_parameters(model: nn.Module) -> int:
    """
    Count the number of trainable parameters in a model.
    
    Args:
        model (nn.Module): PyTorch model
        
    Returns:
        int: Number of trainable parameters
    """
    return sum(p.numel() for p in model.parameters() if p.requires_grad)


if __name__ == "__main__":
    # Example usage
    model = create_vit_model(
        img_size=224,
        patch_size=16,
        num_classes=3,  # pizza, steak, sushi
        embed_dim=768,
        depth=12,
        num_heads=12
    )
    
    print(f"Model created with {count_parameters(model):,} parameters")
    
    # Test forward pass
    x = torch.randn(2, 3, 224, 224)
    out = model(x)
    print(f"Input shape: {x.shape}")
    print(f"Output shape: {out.shape}")