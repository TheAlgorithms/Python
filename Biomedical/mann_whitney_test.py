"""
Mann-Whitney U Test Implementation

The Mann-Whitney U test (also known as the Wilcoxon rank-sum test) is a
non-parametric statistical test used to compare two independent groups
when the data doesn't meet the assumptions of a parametric test like
the independent t-test.

This test is commonly used in biomedical research when:
- Comparing outcomes between two independent groups (e.g., treatment vs control)
- Data is ordinal or continuous but not normally distributed
- Variances between groups are unequal
- Sample sizes are small

Algorithm:
1. Combine both samples and rank all observations
2. Sum ranks for each group
3. Calculate U statistics for both groups
4. Test statistic is the smaller U value
5. Compare against critical values or calculate p-value

Author: Contributed for Hacktoberfest
"""

import math


def mann_whitney_u_test(
    group1: list[int | float], group2: list[int | float], alternative: str = "two-sided"
) -> tuple[float, float, dict]:
    """
    Perform Mann-Whitney U test on two independent samples.

    Parameters:
    -----------
    group1 : list[Union[int, float]]
        First group (e.g., treatment group)
    group2 : list[Union[int, float]]
        Second group (e.g., control group)
    alternative : str, optional
        Alternative hypothesis ('two-sided', 'greater', 'less')
        Default is 'two-sided'

    Returns:
    --------
    tuple[float, float, dict]
        - U statistic (test statistic)
        - p-value (approximate using normal approximation for large samples)
        - Additional statistics dictionary

    Raises:
    -------
    ValueError
        If groups are empty or contain non-numeric values

    Examples:
    ---------
    >>> # Drug efficacy study
    >>> treatment = [23, 25, 28, 30, 32, 35, 38]
    >>> control = [18, 20, 22, 24, 26, 28, 30]
    >>> u_stat, p_val, stats = mann_whitney_u_test(treatment, control)
    >>> print(f"U statistic: {u_stat}, p-value: {p_val:.4f}")
    """

    # Input validation
    if len(group1) == 0 or len(group2) == 0:
        raise ValueError("Groups cannot be empty")

    # Check for numeric values
    try:
        group1 = [float(x) for x in group1]
        group2 = [float(x) for x in group2]
    except (ValueError, TypeError):
        raise ValueError("All values must be numeric")

    n1, n2 = len(group1), len(group2)

    # Combine groups with group labels
    combined = [(val, 1) for val in group1] + [(val, 2) for val in group2]

    # Sort by value
    combined.sort(key=lambda x: x[0])

    # Assign ranks (handle ties by averaging)
    ranks = _assign_ranks_combined(combined)

    # Sum ranks for each group
    rank_sum1 = sum(rank for rank, group in zip(ranks, combined) if group[1] == 1)
    rank_sum2 = sum(rank for rank, group in zip(ranks, combined) if group[1] == 2)

    # Calculate U statistics
    u1 = rank_sum1 - (n1 * (n1 + 1)) / 2
    u2 = rank_sum2 - (n2 * (n2 + 1)) / 2

    # Test statistic (smaller U value)
    u_statistic = min(u1, u2)

    # Calculate p-value
    if n1 * n2 <= 20:
        # For small samples, use exact critical values (simplified here)
        p_value = _calculate_exact_p_value_mw(u_statistic, n1, n2, alternative)
    else:
        # Normal approximation for large samples
        mean_u = (n1 * n2) / 2

        # Calculate variance (adjusted for ties if present)
        n_total = n1 + n2
        tie_correction = _calculate_tie_correction(combined)
        var_u = (n1 * n2 * (n_total + 1 - tie_correction)) / 12

        std_u = math.sqrt(var_u)

        # Continuity correction
        if alternative == "two-sided":
            z = (abs(u_statistic - mean_u) - 0.5) / std_u
            p_value = 2 * (1 - _normal_cdf(abs(z)))
        elif alternative == "greater":
            z = (u_statistic - mean_u + 0.5) / std_u
            p_value = 1 - _normal_cdf(z)
        else:  # alternative == "less"
            z = (u_statistic - mean_u - 0.5) / std_u
            p_value = _normal_cdf(z)

    # Effect size (r = Z / sqrt(N))
    effect_size = abs(z) / math.sqrt(n1 + n2) if n1 * n2 > 20 else None

    # Additional statistics
    stats = {
        "n1": n1,
        "n2": n2,
        "u1": u1,
        "u2": u2,
        "rank_sum1": rank_sum1,
        "rank_sum2": rank_sum2,
        "effect_size": effect_size,
        "median1": _median(group1),
        "median2": _median(group2),
        "median_difference": _median(group1) - _median(group2),
    }

    return u_statistic, p_value, stats


def _assign_ranks_combined(combined: list[tuple]) -> list[float]:
    """
    Assign ranks to combined data, handling ties by averaging.

    Parameters:
    -----------
    combined : list[tuple]
        List of (value, group) tuples, already sorted by value

    Returns:
    --------
    list[float]
        Ranks corresponding to input values
    """
    ranks = []
    i = 0
    n = len(combined)

    while i < n:
        # Find all values equal to current value
        current_value = combined[i][0]
        j = i
        while j < n and combined[j][0] == current_value:
            j += 1

        # Assign average rank to all tied values
        avg_rank = (i + 1 + j) / 2
        for _ in range(i, j):
            ranks.append(avg_rank)

        i = j

    return ranks


def _calculate_tie_correction(combined: list[tuple]) -> float:
    """
    Calculate tie correction factor for variance adjustment.

    Parameters:
    -----------
    combined : list[tuple]
        List of (value, group) tuples, sorted by value

    Returns:
    --------
    float
        Tie correction factor
    """
    tie_correction = 0
    i = 0
    n = len(combined)

    while i < n:
        # Count tied values
        current_value = combined[i][0]
        j = i
        while j < n and combined[j][0] == current_value:
            j += 1

        tie_count = j - i
        if tie_count > 1:
            tie_correction += (tie_count**3 - tie_count) / (n * (n - 1))

        i = j

    return tie_correction


def _calculate_exact_p_value_mw(u: float, n1: int, n2: int, alternative: str) -> float:
    """
    Calculate exact p-value for small samples.

    This is a simplified implementation. In practice, you would use
    pre-computed critical value tables or exact algorithms.
    """
    # Simplified approach - use critical values for alpha = 0.05
    # These are approximations for demonstration
    critical_values = {
        (3, 3): 0,
        (3, 4): 0,
        (3, 5): 1,
        (4, 4): 1,
        (4, 5): 2,
        (5, 5): 4,
        (3, 6): 1,
        (4, 6): 3,
        (5, 6): 5,
        (6, 6): 7,
    }

    key = (min(n1, n2), max(n1, n2))
    critical_val = critical_values.get(key, u)

    if alternative == "two-sided":
        return 0.05 if u <= critical_val else 0.10
    else:
        return 0.025 if u <= critical_val else 0.05


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
    print("Mann-Whitney U Test Examples")
    print("=" * 40)

    # Example 1: Drug efficacy study
    print("\nExample 1: Drug efficacy study")
    treatment_group = [85, 88, 90, 92, 95, 98, 100, 102, 105]
    control_group = [78, 80, 82, 85, 87, 89, 91, 93]

    u_stat, p_val, stats = mann_whitney_u_test(
        treatment_group, control_group, alternative="greater"
    )

    print(f"Treatment group: {treatment_group}")
    print(f"Control group:   {control_group}")
    print(f"U statistic: {u_stat}")
    print(f"p-value: {p_val:.4f}")
    print(f"Treatment median: {stats['median1']:.1f}")
    print(f"Control median: {stats['median2']:.1f}")
    print(f"Median difference: {stats['median_difference']:.1f}")
    effect_size_str = (
        f"Effect size: {stats['effect_size']:.3f}"
        if stats["effect_size"]
        else "N/A (small sample)"
    )
    print(effect_size_str)

    # Example 2: Biomarker levels between groups
    print("\nExample 2: Biomarker levels study")
    patients = [120, 125, 130, 135, 140, 145, 150]
    healthy = [100, 105, 110, 115, 118, 120, 125, 128]

    u_stat2, p_val2, stats2 = mann_whitney_u_test(
        patients, healthy, alternative="greater"
    )

    print(f"Patient group: {patients}")
    print(f"Healthy group: {healthy}")
    print(f"U statistic: {u_stat2}")
    print(f"p-value: {p_val2:.4f}")
    print(f"Patient median: {stats2['median1']:.1f}")
    print(f"Healthy median: {stats2['median2']:.1f}")
    print(f"Median difference: {stats2['median_difference']:.1f}")
    effect_size_str2 = (
        f"Effect size: {stats2['effect_size']:.3f}"
        if stats2["effect_size"]
        else "N/A (small sample)"
    )
    print(effect_size_str2)
