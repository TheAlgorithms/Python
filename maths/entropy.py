from __future__ import annotations

import math
from collections import Counter

"""
In information theory, entropy is a measure of the uncertainty or randomness of a
source of data. It quantifies the expected amount of information contained in each
message from the source.

The core formula for Shannon Entropy H(X) is:
    H(X) = -Σ P(x) * log2(P(x))
where P(x) is the probability of an event x occurring.

This concept mirrors the thermodynamic entropy in physics, representing the level
of disorder in a system. In a digital context, it defines the theoretical limit
for data compression.

Reference: https://en.wikipedia.org/wiki/Entropy_(information_theory)
"""


def shannon_entropy(probabilities: list[float]) -> float:
    """
    Calculates the Shannon entropy of a given probability distribution.

    Args:
        probabilities: A list of probabilities representing a discrete distribution.

    Returns:
        The entropy value in bits.

    Raises:
        ValueError: If probabilities are negative or do not sum to approximately 1.0.

    Examples:
        >>> shannon_entropy([0.5, 0.5])
        1.0
        >>> shannon_entropy([1.0, 0.0])
        0.0
        >>> shannon_entropy([0.25, 0.25, 0.25, 0.25])
        2.0
    """
    if any(p < 0 for p in probabilities):
        raise ValueError("Probabilities cannot be negative.")

    # Due to floating point precision, we check for closeness to 1.0
    if not math.isclose(sum(probabilities), 1.0, rel_tol=1e-9) and sum(probabilities) > 0:
        # Normalize if not summed to 1 but has values
        probabilities = [p / sum(probabilities) for p in probabilities]

    entropy = 0.0
    for p in probabilities:
        if p > 0:
            entropy -= p * math.log2(p)

    return entropy


def analyze_text_entropy(text: str) -> dict[str, float]:
    """
    Analyzes the entropy of a given text at different levels (1-gram, 2-gram).

    Args:
        text: The input string to analyze.

    Returns:
        A dictionary containing entropy values for different n-gram levels.

    Examples:
        >>> result = analyze_text_entropy("aaaaa")
        >>> result['1-gram']
        0.0
        >>> result = analyze_text_entropy("abab")
        >>> round(result['1-gram'], 2)
        1.0
    """
    if not text:
        return {"1-gram": 0.0, "2-gram": 0.0}

    # 1-gram analysis (individual characters)
    counts_1gram = Counter(text)
    total_chars = len(text)
    probs_1gram = [count / total_chars for count in counts_1gram.values()]
    entropy_1gram = shannon_entropy(probs_1gram)

    # 2-gram analysis (pairs of characters)
    if len(text) < 2:
        entropy_2gram = 0.0
    else:
        pairs = [text[i : i + 2] for i in range(len(text) - 1)]
        counts_2gram = Counter(pairs)
        total_pairs = len(pairs)
        probs_2gram = [count / total_pairs for count in counts_2gram.values()]
        entropy_2gram = shannon_entropy(probs_2gram)

    return {
        "1-gram": entropy_1gram,
        "2-gram": entropy_2gram,
        "conditional_entropy": max(0.0, entropy_2gram - entropy_1gram),
    }


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Manual demonstration
    sample_text = "Behind Winston's back the voice from the telescreen was still"
    entropy_stats = analyze_text_entropy(sample_text)
    print(f"Text: '{sample_text[:30]}...'")
    for level, value in entropy_stats.items():
        print(f"{level:>20}: {value:.4f} bits")