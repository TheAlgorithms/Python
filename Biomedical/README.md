# Biomedical Statistical Analysis Module

A comprehensive Python module providing implementations of non-parametric statistical tests commonly used in biomedical research, along with visualization utilities and educational examples.

## 📊 Overview

This module implements two fundamental non-parametric statistical tests:

- **Wilcoxon Signed-Rank Test**: For analyzing paired/dependent samples
- **Mann-Whitney U Test**: For comparing two independent groups

Both tests are essential when data doesn't meet the assumptions required for parametric tests (normality, equal variances, etc.).

## 🔬 Features

### Core Implementations
- **Pure Python**: No external dependencies required for core functionality
- **Educational Focus**: Clear, well-documented algorithms for learning
- **Biomedical Context**: Examples and documentation tailored for biomedical research
- **Statistical Rigor**: Proper handling of ties, effect sizes, and p-value calculations

### Visualization Tools
- Text-based visualizations (no external plotting libraries required)
- Box plot representations
- Paired data change visualization
- Group comparison histograms
- Statistical summary displays

### Quality Assurance
- Comprehensive error handling and input validation
- Type hints for better code maintainability
- Extensive documentation and examples
- Educational comments explaining algorithms

## 📚 Theory and Applications

### Wilcoxon Signed-Rank Test

**When to use:**
- Paired or dependent samples (before/after, matched pairs)
- Data is ordinal or continuous but not normally distributed
- Dependent variable measured at least at ordinal level
- Differences between pairs are not normally distributed

**Examples in biomedical research:**
- Blood pressure before and after treatment
- Pain scores pre and post medication
- Biomarker levels before and after intervention
- Patient quality of life scores over time

**Algorithm:**
1. Calculate differences between paired observations
2. Remove zero differences
3. Rank absolute differences (handle ties by averaging)
4. Sum ranks for positive and negative differences
5. Test statistic W = smaller of the two sums
6. Calculate p-value using exact tables (small n) or normal approximation (large n)

### Mann-Whitney U Test

**When to use:**
- Two independent groups
- Data is ordinal or continuous but not normally distributed
- Independent observations
- No assumption of equal variances required

**Examples in biomedical research:**
- Treatment vs control group outcomes
- Disease vs healthy population comparisons
- Different drug dosage group comparisons
- Gender differences in biomarker levels

**Algorithm:**
1. Combine both samples and rank all observations
2. Sum ranks for each group
3. Calculate U statistics: U₁ = R₁ - n₁(n₁+1)/2
4. Test statistic = min(U₁, U₂)
5. Calculate p-value using exact tables (small n) or normal approximation (large n)

## 🚀 Quick Start

### Basic Usage

```python
from Biomedical import wilcoxon_signed_rank_test, mann_whitney_u_test
from Biomedical import plot_wilcoxon_results, plot_mann_whitney_results

# Wilcoxon test example: Blood pressure study
before_treatment = [145, 142, 138, 150, 155, 148, 152, 160]
after_treatment = [140, 138, 135, 145, 148, 142, 147, 152]

w_stat, p_value, stats = wilcoxon_signed_rank_test(
    before_treatment,
    after_treatment,
    alternative="greater"  # one-sided: treatment reduces BP
)

print(f"W statistic: {w_stat}")
print(f"p-value: {p_value:.4f}")
print(f"Effect size: {stats['effect_size']:.3f}")

# Visualize results
plot_wilcoxon_results(
    before_treatment,
    after_treatment,
    ("Before Treatment", "After Treatment"),
    "Blood Pressure Reduction Study"
)

# Mann-Whitney test example: Drug efficacy study
treatment_group = [85, 88, 90, 92, 95, 98, 100]
control_group = [78, 80, 82, 85, 87, 89, 91]

u_stat, p_value, stats = mann_whitney_u_test(
    treatment_group,
    control_group,
    alternative="greater"  # treatment > control
)

print(f"U statistic: {u_stat}")
print(f"p-value: {p_value:.4f}")
print(f"Median difference: {stats['median_difference']:.1f}")

# Visualize results
plot_mann_whitney_results(
    treatment_group,
    control_group,
    ("Treatment", "Control"),
    "Drug Efficacy Comparison"
)
```

## 📖 Detailed Examples

### Example 1: Clinical Trial - Pain Medication

```python
# Pre and post medication pain scores (1-10 scale)
pain_before = [8, 7, 9, 6, 8, 7, 9, 8, 7, 6]
pain_after = [4, 3, 5, 3, 4, 3, 5, 4, 3, 2]

w_stat, p_val, stats = wilcoxon_signed_rank_test(
    pain_before, pain_after, alternative="greater"
)

print("Pain Medication Study Results:")
print(f"Median pain reduction: {stats['median_difference']:.1f} points")
print(f"Statistical significance: p = {p_val:.4f}")

if p_val < 0.05:
    print("✓ Medication significantly reduces pain")
else:
    print("✗ No significant pain reduction detected")
```

### Example 2: Biomarker Comparison Study

```python
# Biomarker levels: patients vs healthy controls
patients = [120, 125, 130, 135, 140, 145, 150, 155]
healthy = [100, 105, 110, 115, 118, 120, 125, 128]

u_stat, p_val, stats = mann_whitney_u_test(
    patients, healthy, alternative="greater"
)

print("Biomarker Level Comparison:")
print(f"Patient median: {stats['median1']:.1f}")
print(f"Healthy median: {stats['median2']:.1f}")
print(f"Difference: {stats['median_difference']:.1f}")
print(f"Effect size: {stats['effect_size']:.3f}")

if p_val < 0.05:
    print("✓ Significant difference between groups")
else:
    print("✗ No significant difference detected")
```

## 📊 Interpretation Guidelines

### P-value Interpretation
- **p < 0.001**: Very strong evidence against null hypothesis
- **p < 0.01**: Strong evidence against null hypothesis
- **p < 0.05**: Moderate evidence against null hypothesis
- **p ≥ 0.05**: Insufficient evidence to reject null hypothesis

### Effect Size Interpretation (for large samples)
- **Small effect**: r ≈ 0.1 (explains 1% of variance)
- **Medium effect**: r ≈ 0.3 (explains 9% of variance)
- **Large effect**: r ≈ 0.5 (explains 25% of variance)

### Assumptions and Limitations

**Wilcoxon Signed-Rank Test:**
- ✓ Pairs are independent
- ✓ Data is at least ordinal
- ✓ Distribution of differences is approximately symmetric
- ✗ Cannot handle tied differences well (uses average ranks)

**Mann-Whitney U Test:**
- ✓ Observations are independent
- ✓ Data is at least ordinal
- ✓ No assumption of equal variances
- ✗ Assumes similar distribution shapes for location comparison

## 🔧 API Reference

### `wilcoxon_signed_rank_test(sample1, sample2, alternative='two-sided')`

**Parameters:**
- `sample1`: First sample (list of numbers)
- `sample2`: Second sample (list of numbers, same length as sample1)
- `alternative`: 'two-sided', 'greater', or 'less'

**Returns:**
- `w_statistic`: Test statistic (float)
- `p_value`: P-value (float)
- `stats`: Dictionary with additional statistics

### `mann_whitney_u_test(group1, group2, alternative='two-sided')`

**Parameters:**
- `group1`: First group (list of numbers)
- `group2`: Second group (list of numbers)
- `alternative`: 'two-sided', 'greater', or 'less'

**Returns:**
- `u_statistic`: Test statistic (float)
- `p_value`: P-value (float)
- `stats`: Dictionary with additional statistics

## 🎯 Best Practices

### Study Design Considerations
1. **Sample Size**: Consider power analysis for adequate sample size
2. **Data Collection**: Ensure independence of observations
3. **Multiple Comparisons**: Apply Bonferroni correction when appropriate
4. **Effect Size**: Always report effect sizes alongside p-values
5. **Visualization**: Use plots to understand data distribution

### Code Usage Tips
1. Always validate your data before analysis
2. Choose appropriate alternative hypothesis
3. Check sample size recommendations for test validity
4. Document your analysis assumptions
5. Provide context for statistical significance

## 🤝 Contributing

This module was created as part of Hacktoberfest 2024. Contributions welcome!

### Areas for Enhancement
- [ ] Additional non-parametric tests (Kruskal-Wallis, Friedman)
- [ ] Integration with popular plotting libraries (matplotlib, seaborn)
- [ ] Power analysis functions
- [ ] Bootstrap confidence intervals
- [ ] Multiple comparison corrections

### Development Guidelines
- Follow existing code style and documentation patterns
- Include comprehensive tests for new features
- Maintain educational focus with clear explanations
- Ensure compatibility with existing API

## 📝 License

MIT License - See LICENSE file for details.

## 🔗 References

1. Wilcoxon, F. (1945). Individual comparisons by ranking methods. *Biometrics Bulletin*, 1(6), 80-83.
2. Mann, H. B., & Whitney, D. R. (1947). On a test of whether one of two random variables is stochastically larger than the other. *Annals of Mathematical Statistics*, 18(1), 50-60.
3. Hollander, M., Wolfe, D. A., & Chicken, E. (2013). *Nonparametric Statistical Methods* (3rd ed.). John Wiley & Sons.

## 📧 Contact

Created for Hacktoberfest 2024 - Educational implementation of biomedical statistical methods.

---

*Happy analyzing! 🧬📈*