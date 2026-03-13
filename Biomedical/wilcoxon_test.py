"""
Wilcoxon Signed-Rank Test Implementation

The Wilcoxon signed-rank test is a non-parametric statistical test used to compare
two related samples, matched samples, or repeated measurements on a single sample
to assess whether their population mean ranks differ.

This test is commonly used in biomedical research when:
- Data is paired (e.g., before/after treatment measurements)
- The differences are not normally distributed
- The data is ordinal or continuous but doesn't meet parametric test assumptions

Algorithm:
1. Calculate differences between paired observations
2. Remove zero differences
3. Rank absolute differences (assign average rank for ties)
4. Sum ranks for positive and negative differences
5. Calculate test statistic W (smaller of the two sums)
6. Compare against critical values or calculate p-value

Author: Contributed for Hacktoberfest
"""

import math
from typing import Union


def wilcoxon_signed_rank_test(
    sample1: list[Union[int, float]],
    sample2: list[Union[int, float]],
    alternative: str = "two-sided",
) -> tuple[float, float, dict]:
    """
    Perform Wilcoxon signed-rank test on paired samples.

    Parameters:
    -----------
    sample1 : list[Union[int, float]]
        First sample (e.g., pre-treatment measurements)
    sample2 : list[Union[int, float]]
        Second sample (e.g., post-treatment measurements)
    alternative : str, optional
        Alternative hypothesis ('two-sided', 'greater', 'less')
        Default is 'two-sided'

    Returns:
    --------
    tuple[float, float, dict]
        - W statistic (test statistic)
        - p-value (approximate using normal approximation for n > 10)
        - Additional statistics dictionary

    Raises:
    -------
    ValueError
        If samples have different lengths or contain non-numeric values

    Examples:
    ---------
    >>> # Blood pressure before and after treatment
    >>> before = [120, 125, 118, 130, 135, 122, 128, 140]
    >>> after = [115, 120, 116, 125, 128, 118, 122, 135]
    >>> w_stat, p_val, stats = wilcoxon_signed_rank_test(before, after)
    >>> print(f"W statistic: {w_stat}, p-value: {p_val:.4f}")
    """

    # Input validation
    if len(sample1) != len(sample2):
        raise ValueError("Sample sizes must be equal")

    if len(sample1) == 0:
        raise ValueError("Samples cannot be empty")

    # Check for numeric values
    try:
        sample1 = [float(x) for x in sample1]
        sample2 = [float(x) for x in sample2]
    except (ValueError, TypeError):
        raise ValueError("All values must be numeric")

    # Calculate differences
    differences = [x - y for x, y in zip(sample1, sample2)]

    # Remove zero differences
    non_zero_diffs = [d for d in differences if d != 0]
    n = len(non_zero_diffs)

    if n == 0:
        return (
            0.0,
            1.0,
            {
                "n_pairs": len(sample1),
                "n_non_zero": 0,
                "w_positive": 0,
                "w_negative": 0,
                "effect_size": 0.0,
            },
        )

    # Calculate absolute differences and their ranks
    abs_diffs = [abs(d) for d in non_zero_diffs]
    ranks = _assign_ranks(abs_diffs)

    # Sum positive and negative ranks
    w_positive = sum(rank for diff, rank in zip(non_zero_diffs, ranks) if diff > 0)
    w_negative = sum(rank for diff, rank in zip(non_zero_diffs, ranks) if diff < 0)

    # Test statistic (smaller of the two sums)
    w_statistic = min(w_positive, w_negative)

    # Calculate p-value using normal approximation for n > 10
    if n <= 10:
        # For small samples, use exact critical values (simplified here)
        p_value = _calculate_exact_p_value(w_statistic, n, alternative)
    else:
        # Normal approximation
        mean_w = n * (n + 1) / 4
        var_w = n * (n + 1) * (2 * n + 1) / 24
        std_w = math.sqrt(var_w)

        # Continuity correction
        if alternative == "two-sided":
            z = (abs(w_statistic - mean_w) - 0.5) / std_w
            p_value = 2 * (1 - _normal_cdf(abs(z)))
        elif alternative == "greater":
            z = (w_statistic - mean_w + 0.5) / std_w
            p_value = 1 - _normal_cdf(z)
        else:  # alternative == "less"
            z = (w_statistic - mean_w - 0.5) / std_w
            p_value = _normal_cdf(z)

    # Effect size (r = Z / sqrt(N))
    effect_size = abs(z) / math.sqrt(n) if n > 10 else None

    # Additional statistics
    stats = {
        "n_pairs": len(sample1),
        "n_non_zero": n,
        "w_positive": w_positive,
        "w_negative": w_negative,
        "effect_size": effect_size,
        "mean_difference": sum(differences) / len(differences),
        "median_difference": _median(differences),
    }

    return w_statistic, p_value, stats


def _assign_ranks(values: list[float]) -> list[float]:
    """
    Assign ranks to values, handling ties by averaging.

    Parameters:
    -----------
    values : list[float]
        Values to rank

    Returns:
    --------
    list[float]
        Ranks corresponding to input values
    """
    # Create list of (value, original_index) pairs
    indexed_values = [(val, idx) for idx, val in enumerate(values)]

    # Sort by value
    indexed_values.sort(key=lambda x: x[0])

    # Assign ranks
    ranks = [0] * len(values)
    i = 0

    while i < len(indexed_values):
        # Find all values equal to current value
        current_value = indexed_values[i][0]
        j = i
        while j < len(indexed_values) and indexed_values[j][0] == current_value:
            j += 1

        # Assign average rank to all tied values
        avg_rank = (i + 1 + j) / 2
        for k in range(i, j):
            original_idx = indexed_values[k][1]
            ranks[original_idx] = avg_rank

        i = j

    return ranks


def _calculate_exact_p_value(w: float, n: int, alternative: str) -> float:
    """
    Calculate exact p-value for small samples (n <= 10).

    This is a simplified implementation. In practice, you would use
    pre-computed critical value tables.
    """
    # Simplified critical values for two-sided test at alpha = 0.05
    critical_values = {5: 0, 6: 2, 7: 3, 8: 5, 9: 8, 10: 10}

    if n < 5:
        return 1.0  # Too small for reliable test

    critical_val = critical_values.get(n, 0)

    if alternative == "two-sided":
        if w <= critical_val:
            return 0.05  # Approximate
        else:
            return 0.10  # Approximate
    else:
        # For one-sided tests, adjust accordingly
        return 0.05 if w <= critical_val else 0.10


def _normal_cdf(z: float) -> float:
    """
    Cumulative distribution function for standard normal distribution.

    Using approximation for computational efficiency.
    """
    # Abramowitz and Stegun approximation
    if z < 0:
        return 1 - _normal_cdf(-z)

    # Constants
    a1, a2, a3, a4, a5 = (
        0.254829592,
        -0.284496736,
        1.421413741,
        -1.453152027,
        1.061405429,
    )
    p = 0.3275911

    t = 1.0 / (1.0 + p * z)
    y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * math.exp(
        -z * z / 2
    )

    return y


def _median(values: list[float]) -> float:
    """Calculate median of a list of values."""
    sorted_values = sorted(values)
    n = len(sorted_values)

    if n % 2 == 0:
        return (sorted_values[n // 2 - 1] + sorted_values[n // 2]) / 2
    else:
        return sorted_values[n // 2]


if __name__ == "__main__":
    # Example usage with biomedical data
    print("Wilcoxon Signed-Rank Test Example")
    print("=" * 40)

    # Example 1: Blood pressure before and after treatment
    print("\nExample 1: Blood pressure study")
    before_treatment = [145, 142, 138, 150, 155, 148, 152, 160, 144, 149]
    after_treatment = [140, 138, 135, 145, 148, 142, 147, 152, 139, 143]

    w_stat, p_val, stats = wilcoxon_signed_rank_test(
        before_treatment, after_treatment, alternative="greater"
    )

    print(f"Before treatment: {before_treatment}")
    print(f"After treatment:  {after_treatment}")
    print(f"W statistic: {w_stat}")
    print(f"p-value: {p_val:.4f}")
    print(f"Mean difference: {stats['mean_difference']:.2f}")
    print(f"Effect size: {stats['effect_size']:.3f}" if stats["effect_size"] else "N/A")

    # Example 2: Pain scores before and after medication
    print("\nExample 2: Pain score study")
    pain_before = [8, 7, 9, 6, 8, 7, 9, 8, 7, 6]
    pain_after = [4, 3, 5, 3, 4, 3, 5, 4, 3, 2]

    w_stat2, p_val2, stats2 = wilcoxon_signed_rank_test(
        pain_before, pain_after, alternative="greater"
    )

    print(f"Pain before medication: {pain_before}")
    print(f"Pain after medication:  {pain_after}")
    print(f"W statistic: {w_stat2}")
    print(f"p-value: {p_val2:.4f}")
    print(f"Mean difference: {stats2['mean_difference']:.2f}")
    effect_size_str = (
        f"Effect size: {stats2['effect_size']:.3f}" if stats2["effect_size"] else "N/A"
    )
    print(effect_size_str)
