"""
Biomedical Statistical Analysis Module

This module provides implementations of statistical tests commonly used in
biomedical research, including non-parametric tests for comparing groups
and analyzing paired data.

Available Tests:
- Wilcoxon Signed-Rank Test: For paired data when normality assumptions
  are violated
- Mann-Whitney U Test: For comparing two independent groups
  (non-parametric alternative to t-test)

Features:
- Pure Python implementations following standard algorithms
- Comprehensive visualizations for result interpretation
- Educational examples with biomedical contexts
- Detailed documentation and theory explanations

Author: Contributed for Hacktoberfest
License: MIT
"""

from .mann_whitney_test import mann_whitney_u_test
from .statistical_visualizations import (
    plot_independent_groups,
    plot_mann_whitney_results,
    plot_paired_data,
    plot_wilcoxon_results,
)
from .wilcoxon_test import wilcoxon_signed_rank_test

__all__ = [
    "mann_whitney_u_test",
    "plot_independent_groups",
    "plot_mann_whitney_results",
    "plot_paired_data",
    "plot_wilcoxon_results",
    "wilcoxon_signed_rank_test",
]

__version__ = "1.0.0"
