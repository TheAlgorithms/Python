"""
Vision Transformer (ViT) for Image Classification

This module implements the Vision Transformer architecture as described in the paper
"An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale"
by Dosovitskiy et al. (2020)

Paper: https://arxiv.org/abs/2010.11929

The Vision Transformer splits an image into fixed-size patches, linearly embeds each
patch, adds position embeddings, and feeds the resulting sequence of vectors to a
standard Transformer encoder. For classification, a learnable classification token
is prepended to the sequence.

Author: devvratpathak
"""

import numpy as np


def create_patches(
    image: np.ndarray, patch_size: int = 16
) -> tuple[np.ndarray, tuple[int, int]]:
    """
    Split an image into non-overlapping patches.

    Args:
        image: Input image array of shape (height, width, channels)
        patch_size: Size of each square patch (default: 16)

    Returns:
        A tuple containing:
        - patches: Array of shape (num_patches, patch_size, patch_size, channels)
        - grid_size: Tuple (height_patches, width_patches) representing the grid

    Examples:
        >>> img = np.random.rand(32, 32, 3)
        >>> patches, grid = create_patches(img, patch_size=16)
        >>> patches.shape
        (4, 16, 16, 3)
        >>> grid
        (2, 2)

        >>> img = np.random.rand(224, 224, 3)
        >>> patches, grid = create_patches(img, patch_size=16)
        >>> patches.shape
        (196, 16, 16, 3)
        >>> grid
        (14, 14)
    """
    if len(image.shape) != 3:
        msg = f"Expected 3D image, got shape {image.shape}"
        raise ValueError(msg)

    height, width, channels = image.shape

    if height % patch_size != 0 or width % patch_size != 0:
        msg = (
            f"Image dimensions ({height}x{width}) must be divisible by "
            f"patch_size ({patch_size})"
        )
        raise ValueError(msg)

    # Calculate number of patches in each dimension
    num_patches_h = height // patch_size
    num_patches_w = width // patch_size

    # Reshape image into patches
    patches = image.reshape(
        num_patches_h, patch_size, num_patches_w, patch_size, channels
    )
    # Transpose to get patches in sequence
    patches = patches.transpose(0, 2, 1, 3, 4)
    # Reshape to (num_patches, patch_size, patch_size, channels)
    patches = patches.reshape(-1, patch_size, patch_size, channels)

    return patches, (num_patches_h, num_patches_w)


def patch_embedding(patches: np.ndarray, embedding_dim: int = 768) -> np.ndarray:
    """
    Linearly project flattened patches to embedding dimension.

    Args:
        patches: Array of patches with shape
            (num_patches, patch_size, patch_size, channels)
        embedding_dim: Dimension of the embedding space (default: 768)

    Returns:
        Embedded patches of shape (num_patches, embedding_dim)

    Examples:
        >>> patches = np.random.rand(4, 16, 16, 3)
        >>> embeddings = patch_embedding(patches, embedding_dim=768)
        >>> embeddings.shape
        (4, 768)

        >>> patches = np.random.rand(196, 16, 16, 3)
        >>> embeddings = patch_embedding(patches, embedding_dim=512)
        >>> embeddings.shape
        (196, 512)
    """
    num_patches = patches.shape[0]
    # Flatten each patch
    flattened = patches.reshape(num_patches, -1)

    # Linear projection (simplified - in practice this is a learned weight matrix)
    # For demonstration, we use random projection
    patch_dim = flattened.shape[1]
    rng = np.random.default_rng()
    projection_matrix = rng.standard_normal((patch_dim, embedding_dim)) * 0.02

    embedded = flattened @ projection_matrix

    return embedded


def add_positional_encoding(
    embeddings: np.ndarray, num_positions: int | None = None
) -> np.ndarray:
    """
    Add learnable positional encodings to patch embeddings.

    Args:
        embeddings: Embedded patches of shape (num_patches, embedding_dim)
        num_positions: Number of positions (if None, uses num_patches + 1 for CLS token)

    Returns:
        Embeddings with positional encoding of shape (num_positions, embedding_dim)

    Examples:
        >>> embeddings = np.random.rand(4, 768)
        >>> pos_embeddings = add_positional_encoding(embeddings)
        >>> pos_embeddings.shape
        (5, 768)

        >>> embeddings = np.random.rand(196, 512)
        >>> pos_embeddings = add_positional_encoding(embeddings)
        >>> pos_embeddings.shape
        (197, 512)
    """
    num_patches, embedding_dim = embeddings.shape

    if num_positions is None:
        # Add 1 for the CLS token
        num_positions = num_patches + 1

    # Create learnable positional encodings (simplified - normally learned)
    rng = np.random.default_rng()
    positional_encodings = rng.standard_normal((num_positions, embedding_dim)) * 0.02

    # Prepend CLS token
    cls_token = rng.standard_normal((1, embedding_dim)) * 0.02

    # Concatenate CLS token with patch embeddings
    embeddings_with_cls = np.vstack([cls_token, embeddings])

    # Add positional encodings
    embeddings_with_pos = embeddings_with_cls + positional_encodings

    return embeddings_with_pos


def attention_mechanism(
    query: np.ndarray,
    key: np.ndarray,
    value: np.ndarray,
    mask: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Compute scaled dot-product attention.

    Attention(Q, K, V) = softmax(QK^T / sqrt(d_k))V

    Args:
        query: Query matrix of shape (seq_len, d_k)
        key: Key matrix of shape (seq_len, d_k)
        value: Value matrix of shape (seq_len, d_v)
        mask: Optional attention mask

    Returns:
        A tuple containing:
        - output: Attention output of shape (seq_len, d_v)
        - attention_weights: Attention weights of shape (seq_len, seq_len)

    Examples:
        >>> q = np.random.rand(10, 64)
        >>> k = np.random.rand(10, 64)
        >>> v = np.random.rand(10, 64)
        >>> output, weights = attention_mechanism(q, k, v)
        >>> output.shape
        (10, 64)
        >>> weights.shape
        (10, 10)
        >>> np.allclose(weights.sum(axis=1), 1.0)
        True
    """
    d_k = query.shape[-1]

    # Compute attention scores: QK^T / sqrt(d_k)
    scores = query @ key.T / np.sqrt(d_k)

    # Apply mask if provided
    if mask is not None:
        scores = np.where(mask, scores, -1e9)

    # Apply softmax to get attention weights
    exp_scores = np.exp(scores - np.max(scores, axis=-1, keepdims=True))
    attention_weights = exp_scores / np.sum(exp_scores, axis=-1, keepdims=True)

    # Compute weighted sum of values
    output = attention_weights @ value

    return output, attention_weights


def layer_norm(embeddings: np.ndarray, epsilon: float = 1e-6) -> np.ndarray:
    """
    Apply Layer Normalization.

    Args:
        embeddings: Input array of shape (seq_len, embedding_dim)
        epsilon: Small constant for numerical stability (default: 1e-6)

    Returns:
        Normalized array of same shape as input

    Examples:
        >>> embeddings = np.random.rand(10, 768)
        >>> normalized = layer_norm(embeddings)
        >>> normalized.shape
        (10, 768)
        >>> np.allclose(normalized.mean(axis=1), 0.0, atol=1e-6)
        True
        >>> np.allclose(normalized.std(axis=1), 1.0, atol=1e-6)
        True
    """
    mean = embeddings.mean(axis=-1, keepdims=True)
    std = embeddings.std(axis=-1, keepdims=True)
    return (embeddings - mean) / (std + epsilon)


def feedforward_network(embeddings: np.ndarray, hidden_dim: int = 3072) -> np.ndarray:
    """
    Apply position-wise feed-forward network.

    FFN(x) = max(0, xW1 + b1)W2 + b2

    Args:
        embeddings: Input array of shape (seq_len, embedding_dim)
        hidden_dim: Hidden dimension size (default: 3072, typically 4x embedding_dim)

    Returns:
        Output array of shape (seq_len, embedding_dim)

    Examples:
        >>> embeddings = np.random.rand(10, 768)
        >>> output = feedforward_network(embeddings, hidden_dim=3072)
        >>> output.shape
        (10, 768)

        >>> embeddings = np.random.rand(197, 512)
        >>> output = feedforward_network(embeddings, hidden_dim=2048)
        >>> output.shape
        (197, 512)
    """
    embedding_dim = embeddings.shape[1]
    rng = np.random.default_rng()

    # First linear layer
    w1 = rng.standard_normal((embedding_dim, hidden_dim)) * 0.02
    b1 = np.zeros(hidden_dim)
    hidden = embeddings @ w1 + b1

    # GELU activation (approximation)
    gelu_factor = np.sqrt(2 / np.pi) * (hidden + 0.044715 * hidden**3)
    hidden = 0.5 * hidden * (1 + np.tanh(gelu_factor))

    # Second linear layer
    w2 = rng.standard_normal((hidden_dim, embedding_dim)) * 0.02
    b2 = np.zeros(embedding_dim)
    output = hidden @ w2 + b2

    return output


def transformer_encoder_block(
    embeddings: np.ndarray,
    num_heads: int = 12,  # noqa: ARG001
    hidden_dim: int = 3072,
) -> np.ndarray:
    """
    Apply a single Transformer encoder block.

    The block consists of:
    1. Multi-head self-attention with residual connection and layer norm
    2. Feed-forward network with residual connection and layer norm

    Args:
        embeddings: Input array of shape (seq_len, embedding_dim)
        num_heads: Number of attention heads (default: 12, kept for API)
        hidden_dim: Hidden dimension for FFN (default: 3072)

    Returns:
        Output array of shape (seq_len, embedding_dim)

    Examples:
        >>> embeddings = np.random.rand(197, 768)
        >>> output = transformer_encoder_block(
        ...     embeddings, num_heads=12, hidden_dim=3072
        ... )
        >>> output.shape
        (197, 768)

        >>> embeddings = np.random.rand(50, 512)
        >>> output = transformer_encoder_block(
        ...     embeddings, num_heads=8, hidden_dim=2048
        ... )
        >>> output.shape
        (50, 512)
    """
    # Multi-head self-attention (simplified - using single head for demonstration)
    # In practice, this would split into multiple heads
    # num_heads parameter is kept for API compatibility
    attention_output, _ = attention_mechanism(embeddings, embeddings, embeddings)

    # Add residual connection and apply layer norm
    embeddings = layer_norm(embeddings + attention_output)

    # Feed-forward network
    ffn_output = feedforward_network(embeddings, hidden_dim)

    # Add residual connection and apply layer norm
    embeddings = layer_norm(embeddings + ffn_output)

    return embeddings


def vision_transformer(
    image: np.ndarray,
    patch_size: int = 16,
    embedding_dim: int = 768,
    num_layers: int = 12,
    num_heads: int = 12,
    hidden_dim: int = 3072,
    num_classes: int = 1000,
) -> np.ndarray:
    """
    Apply Vision Transformer for image classification.

    Architecture:
    1. Split image into patches
    2. Linear projection of flattened patches
    3. Add positional embeddings
    4. Pass through Transformer encoder layers
    5. Extract CLS token and apply classification head

    Args:
        image: Input image array of shape (height, width, channels)
        patch_size: Size of each patch (default: 16)
        embedding_dim: Embedding dimension (default: 768)
        num_layers: Number of Transformer layers (default: 12)
        num_heads: Number of attention heads (default: 12)
        hidden_dim: Hidden dimension in FFN (default: 3072)
        num_classes: Number of output classes (default: 1000)

    Returns:
        Class logits of shape (num_classes,)

    Examples:
        >>> img = np.random.rand(224, 224, 3)
        >>> logits = vision_transformer(img, patch_size=16, num_classes=10)
        >>> logits.shape
        (10,)

        >>> img = np.random.rand(32, 32, 3)
        >>> logits = vision_transformer(
        ...     img, patch_size=16, embedding_dim=512, num_layers=6, num_classes=100
        ... )
        >>> logits.shape
        (100,)
    """
    # Step 1: Create patches
    patches, _ = create_patches(image, patch_size)

    # Step 2: Embed patches
    embeddings = patch_embedding(patches, embedding_dim)

    # Step 3: Add positional encodings (includes CLS token)
    embeddings = add_positional_encoding(embeddings)

    # Step 4: Pass through Transformer encoder layers
    for _ in range(num_layers):
        embeddings = transformer_encoder_block(embeddings, num_heads, hidden_dim)

    # Step 5: Extract CLS token (first token)
    cls_token = embeddings[0]

    # Step 6: Classification head (linear layer)
    rng = np.random.default_rng()
    classifier_weights = rng.standard_normal((embedding_dim, num_classes)) * 0.02
    classifier_bias = np.zeros(num_classes)
    logits = cls_token @ classifier_weights + classifier_bias

    return logits


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example usage
    print("Vision Transformer Example")
    print("=" * 50)

    # Create a sample image (224x224x3 for ImageNet-style input)
    rng = np.random.default_rng()
    sample_image = rng.random((224, 224, 3))
    print(f"Input image shape: {sample_image.shape}")

    # Apply Vision Transformer
    logits = vision_transformer(
        sample_image,
        patch_size=16,
        embedding_dim=768,
        num_layers=12,
        num_heads=12,
        hidden_dim=3072,
        num_classes=1000,
    )

    print(f"Output logits shape: {logits.shape}")
    print(f"Predicted class: {np.argmax(logits)}")

    # Demonstrate patch creation
    print("\n" + "=" * 50)
    print("Patch Creation Example")
    patches, grid = create_patches(sample_image, patch_size=16)
    print(f"Number of patches: {patches.shape[0]}")
    print(f"Patch size: {patches.shape[1:3]}")
    print(f"Grid size: {grid}")
