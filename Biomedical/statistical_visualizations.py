"""
Statistical Visualization Utilities for Biomedical Analysis

This module provides visualization functions for Wilcoxon and Mann-Whitney tests
to help interpret results and communicate findings effectively.

Functions include:
- Box plots for comparing groups
- Histogram overlays for distribution comparison
- Before/after plots for paired data
- Effect size visualizations
- P-value and statistical significance indicators

Author: Contributed for Hacktoberfest
"""


def plot_wilcoxon_results(
    sample1: list[float],
    sample2: list[float],
    labels: tuple[str, str] = ("Before", "After"),
    title: str = "Wilcoxon Signed-Rank Test Results",
) -> None:
    """
    Create visualization for Wilcoxon signed-rank test results.

    This function creates a simple text-based visualization since we're avoiding
    external dependencies. In a full implementation, you would use matplotlib.

    Parameters:
    -----------
    sample1 : list[float]
        First sample (e.g., pre-treatment)
    sample2 : list[float]
        Second sample (e.g., post-treatment)
    labels : tuple[str, str]
        Labels for the two samples
    title : str
        Title for the plot
    """
    print(f"\n{title}")
    print("=" * len(title))

    # Calculate basic statistics
    mean1, mean2 = sum(sample1) / len(sample1), sum(sample2) / len(sample2)
    median1, median2 = _median(sample1), _median(sample2)
    differences = [x - y for x, y in zip(sample1, sample2)]
    mean_diff = sum(differences) / len(differences)

    print(f"\n{labels[0]} group statistics:")
    print(f"  Mean: {mean1:.2f}")
    print(f"  Median: {median1:.2f}")
    print(f"  Range: {min(sample1):.1f} - {max(sample1):.1f}")

    print(f"\n{labels[1]} group statistics:")
    print(f"  Mean: {mean2:.2f}")
    print(f"  Median: {median2:.2f}")
    print(f"  Range: {min(sample2):.1f} - {max(sample2):.1f}")

    print("\nPaired differences:")
    print(f"  Mean difference: {mean_diff:.2f}")
    print(f"  Median difference: {_median(differences):.2f}")

    # Simple text-based paired data visualization
    print("\nPaired data visualization:")
    print(f"{'Subject':<8} {labels[0]:<10} {labels[1]:<10} {'Difference':<10}")
    print("-" * 40)
    for i, (val1, val2) in enumerate(zip(sample1, sample2)):
        diff = val1 - val2
        diff_indicator = "↑" if diff > 0 else "↓" if diff < 0 else "="
        print(f"{i + 1:<8} {val1:<10.1f} {val2:<10.1f} {diff:<7.1f} {diff_indicator}")


def plot_mann_whitney_results(
    group1: list[float],
    group2: list[float],
    labels: tuple[str, str] = ("Group 1", "Group 2"),
    title: str = "Mann-Whitney U Test Results",
) -> None:
    """
    Create visualization for Mann-Whitney U test results.

    Parameters:
    -----------
    group1 : list[float]
        First group
    group2 : list[float]
        Second group
    labels : tuple[str, str]
        Labels for the two groups
    title : str
        Title for the plot
    """
    print(f"\n{title}")
    print("=" * len(title))

    # Calculate basic statistics
    mean1, mean2 = sum(group1) / len(group1), sum(group2) / len(group2)
    median1, median2 = _median(group1), _median(group2)

    print(f"\n{labels[0]} statistics (n={len(group1)}):")
    print(f"  Mean: {mean1:.2f}")
    print(f"  Median: {median1:.2f}")
    print(f"  Range: {min(group1):.1f} - {max(group1):.1f}")

    print(f"\n{labels[1]} statistics (n={len(group2)}):")
    print(f"  Mean: {mean2:.2f}")
    print(f"  Median: {median2:.2f}")
    print(f"  Range: {min(group2):.1f} - {max(group2):.1f}")

    # Simple text-based comparison
    print("\nGroup comparison:")
    print(f"  Mean difference: {mean1 - mean2:.2f}")
    print(f"  Median difference: {median1 - median2:.2f}")

    # Text-based box plot representation
    _print_text_boxplot(group1, group2, labels)


def plot_paired_data(
    sample1: list[float],
    sample2: list[float],
    labels: tuple[str, str] = ("Before", "After"),
) -> None:
    """
    Create a simple paired data plot.

    Parameters:
    -----------
    sample1 : list[float]
        First sample
    sample2 : list[float]
        Second sample
    labels : tuple[str, str]
        Labels for the samples
    """
    print(f"\nPaired Data Plot: {labels[0]} vs {labels[1]}")
    print("=" * 50)

    print(f"\n{labels[0]:<15} {labels[1]:<15} Change")
    print("-" * 45)

    for val1, val2 in zip(sample1, sample2):
        # Simple visualization of change
        change = val2 - val1
        change_str = f"{change:+.1f}"
        trend = "↑" if change > 0 else "↓" if change < 0 else "="

        print(f"{val1:<15.1f} {val2:<15.1f} {change_str:<6} {trend}")

    # Summary
    total_change = sum(val2 - val1 for val1, val2 in zip(sample1, sample2))
    avg_change = total_change / len(sample1)
    improved = sum(1 for val1, val2 in zip(sample1, sample2) if val2 > val1)
    worsened = sum(1 for val1, val2 in zip(sample1, sample2) if val2 < val1)
    unchanged = len(sample1) - improved - worsened

    print("\nSummary:")
    print(f"  Average change: {avg_change:.2f}")
    print(f"  Improved: {improved} subjects")
    print(f"  Worsened: {worsened} subjects")
    print(f"  Unchanged: {unchanged} subjects")


def plot_independent_groups(
    group1: list[float],
    group2: list[float],
    labels: tuple[str, str] = ("Group 1", "Group 2"),
) -> None:
    """
    Create a simple independent groups comparison plot.

    Parameters:
    -----------
    group1 : list[float]
        First group
    group2 : list[float]
        Second group
    labels : tuple[str, str]
        Labels for the groups
    """
    print(f"\nIndependent Groups Comparison: {labels[0]} vs {labels[1]}")
    print("=" * 60)

    # Display data side by side
    max_len = max(len(group1), len(group2))

    print(f"\n{labels[0]:<20} {labels[1]:<20}")
    print("-" * 42)

    for i in range(max_len):
        val1_str = f"{group1[i]:.1f}" if i < len(group1) else "-"
        val2_str = f"{group2[i]:.1f}" if i < len(group2) else "-"
        print(f"{val1_str:<20} {val2_str:<20}")

    # Create simple histogram representation
    _print_histogram_comparison(group1, group2, labels)


def _print_text_boxplot(
    group1: list[float], group2: list[float], labels: tuple[str, str]
) -> None:
    """Create a simple text-based box plot representation."""
    print("\nText-based box plot comparison:")
    print("-" * 40)

    for group, label in [(group1, labels[0]), (group2, labels[1])]:
        sorted_group = sorted(group)
        n = len(sorted_group)

        # Calculate quartiles
        q1 = sorted_group[n // 4]
        median = _median(sorted_group)
        q3 = sorted_group[(3 * n) // 4]
        min_val, max_val = sorted_group[0], sorted_group[-1]

        print(f"\n{label}:")
        print(f"  Min:    {min_val:.1f}")
        print(f"  Q1:     {q1:.1f}")
        print(f"  Median: {median:.1f}")
        print(f"  Q3:     {q3:.1f}")
        print(f"  Max:    {max_val:.1f}")

        # Simple box representation
        scale = 30
        box_repr = _create_box_representation(min_val, q1, median, q3, max_val, scale)
        print(f"  Box:    {box_repr}")


def _print_histogram_comparison(
    group1: list[float], group2: list[float], labels: tuple[str, str]
) -> None:
    """Create a simple histogram comparison."""
    print("\nHistogram comparison:")
    print("-" * 30)

    # Combine data to get overall range
    all_data = group1 + group2
    min_val, max_val = min(all_data), max(all_data)

    # Create bins
    n_bins = 5
    bin_width = (max_val - min_val) / n_bins

    print(f"\n{'Bin Range':<15} {labels[0]:<10} {labels[1]:<10}")
    print("-" * 35)

    for i in range(n_bins):
        bin_start = min_val + i * bin_width
        bin_end = min_val + (i + 1) * bin_width

        count1 = sum(1 for x in group1 if bin_start <= x < bin_end)
        count2 = sum(1 for x in group2 if bin_start <= x < bin_end)

        # For last bin, include the maximum value
        if i == n_bins - 1:
            count1 = sum(1 for x in group1 if bin_start <= x <= bin_end)
            count2 = sum(1 for x in group2 if bin_start <= x <= bin_end)

        bin_range = f"{bin_start:.1f}-{bin_end:.1f}"
        bar1 = "*" * count1
        bar2 = "*" * count2

        print(f"{bin_range:<15} {bar1:<10} {bar2:<10}")
        print(f"{'Count:':<15} {count1:<10} {count2:<10}")


def _create_box_representation(
    min_val: float, q1: float, median: float, q3: float, max_val: float, width: int
) -> str:
    """Create a simple ASCII box plot representation."""
    # Normalize positions to fit within width
    range_val = max_val - min_val
    if range_val == 0:
        return "=" * width

    pos_min = 0
    pos_q1 = int((q1 - min_val) / range_val * width)
    pos_median = int((median - min_val) / range_val * width)
    pos_q3 = int((q3 - min_val) / range_val * width)
    pos_max = width - 1

    # Create representation
    repr_chars = ["-"] * width

    # Mark quartiles and median
    if pos_q1 < width:
        repr_chars[pos_q1] = "["
    if pos_median < width:
        repr_chars[pos_median] = "|"
    if pos_q3 < width:
        repr_chars[pos_q3] = "]"

    # Mark min and max
    repr_chars[pos_min] = "("
    repr_chars[pos_max] = ")"

    return "".join(repr_chars)


def _median(values: list[float]) -> float:
    """Calculate median of a list of values."""
    sorted_values = sorted(values)
    n = len(sorted_values)

    if n % 2 == 0:
        return (sorted_values[n // 2 - 1] + sorted_values[n // 2]) / 2
    else:
        return sorted_values[n // 2]


if __name__ == "__main__":
    # Example usage
    print("Statistical Visualization Examples")
    print("=" * 40)

    # Wilcoxon test visualization
    before_treatment = [145, 142, 138, 150, 155, 148, 152, 160]
    after_treatment = [140, 138, 135, 145, 148, 142, 147, 152]

    plot_wilcoxon_results(
        before_treatment,
        after_treatment,
        ("Before Treatment", "After Treatment"),
        "Blood Pressure Study Results",
    )

    plot_paired_data(before_treatment, after_treatment, ("Before", "After"))

    # Mann-Whitney test visualization
    treatment_group = [85, 88, 90, 92, 95, 98, 100]
    control_group = [78, 80, 82, 85, 87, 89, 91]

    plot_mann_whitney_results(
        treatment_group,
        control_group,
        ("Treatment", "Control"),
        "Drug Efficacy Study Results",
    )

    plot_independent_groups(treatment_group, control_group, ("Treatment", "Control"))
