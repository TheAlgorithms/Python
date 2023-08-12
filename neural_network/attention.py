"""
Single query attention.
References:
    - https://arxiv.org/abs/1706.03762
    - https://arxiv.org/abs/2207.09238
"""

import numpy as np


class SingleQueryAttention:
    def __init__(self, d_attn: int, d_in: int, d_out: int):
        """
        This function initializes the parameters with random values.

        Args:
            d_attn: the dimensionality of attention
            d_in: the input dimension (i.e., dimension of the token embeddings)
            d_out: the output dimension
        """
        self.d_attn = d_attn
        self.d_in = d_in
        self.d_out = d_out

        self.normalization = np.sqrt(self.d_attn)

        # parameters for the linear projections
        self.weights_query = np.random.rand(self.d_attn, self.d_in)
        self.weights_key = np.random.rand(self.d_attn, self.d_in)
        self.weights_value = np.random.rand(self.d_out, self.d_in)

        self.bias_query = np.random.rand(self.d_attn)
        self.bias_key = np.random.rand(self.d_attn)
        self.bias_value = np.random.rand(self.d_out)

    def __call__(
        self, token_embedding: np.ndarray, context_token_embeddings: np.ndarray
    ) -> np.ndarray:
        """

        Args:
            token_embedding: token vector representation
            context_token_embeddings: context token vector representations

        Returns:
            vector representation of the token and context combined

        >>> d_in = 2
        >>> d_out = 3
        >>> d_attn = 4
        >>> attention = SingleQueryAttention(d_attn=d_attn, d_in=d_in, d_out=d_out)
        >>> attention.weights_query = np.array([[1, 0], [2, 1], [3, -1], [4, 0]])
        >>> attention.weights_key = np.array([[2, -1], [3, -2], [0, 1], [1, 0]])
        >>> attention.weights_value = np.array([[1, 0], [2, 1], [3, 0]])
        >>> attention.bias_query = np.array([-1, -2, 1, 2])
        >>> attention.bias_key = np.array([-2, 1, 0, 2])
        >>> attention.bias_value = np.array([-1, 0, 1])
        >>> test_token_embedding = np.array([-1, 1])
        >>> test_context_token_embeddings = np.array([[2, -2], [3, 1]])
        >>> expected = np.array([1, 2, 7]) / 2 + np.array([2, 7, 10]) / 2
        >>> output = attention(test_token_embedding, test_context_token_embeddings)
        >>> output.shape == (d_out,)
        True
        >>> (expected == output).all()
        True
        """
        # calculate query, keys, values
        query = self.weights_query @ token_embedding + self.bias_query
        keys = [
            self.weights_key @ context_token_embedding + self.bias_key
            for context_token_embedding in context_token_embeddings
        ]
        values = [
            self.weights_value @ context_token_embedding + self.bias_value
            for context_token_embedding in context_token_embeddings
        ]

        # calculate the softmax
        exponential_s = np.exp(
            [np.transpose(query) @ key / self.normalization for key in keys]
        )
        softmax = [exponential / np.sum(exponential_s) for exponential in exponential_s]

        # generate the output
        output = np.add.reduce(
            [
                token_importance * value
                for token_importance, value in zip(softmax, values)
            ]
        )
        return output


if __name__ == "__main__":
    import doctest

    doctest.testmod()
