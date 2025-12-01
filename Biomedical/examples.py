"""
Comprehensive Examples of Biomedical Statistical Analysis

This script demonstrates practical applications of the Wilcoxon and Mann-Whitney
tests in various biomedical research scenarios. Each example includes:
- Realistic biomedical data
- Appropriate test selection and justification
- Complete statistical analysis
- Interpretation of results
- Visualization of findings

Run this script to see all examples in action:
    python examples.py

Author: Contributed for Hacktoberfest
"""

from wilcoxon_test import wilcoxon_signed_rank_test
from mann_whitney_test import mann_whitney_u_test
from statistical_visualizations import (
    plot_wilcoxon_results,
    plot_mann_whitney_results,
    plot_paired_data,
    plot_independent_groups,
)


def example_1_blood_pressure_study():
    """
    Example 1: Antihypertensive Drug Study

    Scenario: Clinical trial testing effectiveness of a new blood pressure
    medication. 15 hypertensive patients had their systolic BP measured
    before and after 4 weeks of treatment.

    Test: Wilcoxon signed-rank test (paired data, non-normal distribution)
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 1: ANTIHYPERTENSIVE DRUG EFFICACY STUDY")
    print("=" * 60)

    print("\nStudy Design:")
    print("- Paired design: same patients before/after treatment")
    print("- Outcome: Systolic blood pressure (mmHg)")
    print("- Sample size: n=15 patients")
    print("- Treatment duration: 4 weeks")

    # Realistic blood pressure data
    before_treatment = [
        165,
        158,
        170,
        162,
        175,
        160,
        168,
        172,
        155,
        163,
        169,
        174,
        161,
        166,
        159,
    ]
    after_treatment = [
        142,
        145,
        155,
        148,
        160,
        145,
        150,
        158,
        140,
        147,
        152,
        165,
        144,
        149,
        143,
    ]

    print(f"\nData:")
    print(f"Before treatment: {before_treatment}")
    print(f"After treatment:  {after_treatment}")

    # Perform Wilcoxon signed-rank test
    w_stat, p_value, stats = wilcoxon_signed_rank_test(
        before_treatment, after_treatment, alternative="greater"
    )

    # Display results
    print(f"\nStatistical Analysis:")
    print(f"Test: Wilcoxon Signed-Rank Test (one-tailed)")
    print(f"H₀: Median difference ≤ 0 (no reduction)")
    print(f"H₁: Median difference > 0 (blood pressure reduced)")
    print(f"W statistic: {w_stat}")
    print(f"p-value: {p_value:.4f}")
    print(f"Mean BP reduction: {stats['mean_difference']:.1f} mmHg")
    print(f"Median BP reduction: {stats['median_difference']:.1f} mmHg")

    if stats["effect_size"]:
        print(f"Effect size (r): {stats['effect_size']:.3f}")

    # Interpretation
    print(f"\nInterpretation:")
    if p_value < 0.05:
        print("✓ SIGNIFICANT: The medication significantly reduces blood pressure")
        if stats["median_difference"] >= 10:
            print("✓ CLINICALLY MEANINGFUL: >10 mmHg reduction is clinically important")
        else:
            print(
                "? CLINICAL SIGNIFICANCE: Reduction may be statistically but not clinically significant"
            )
    else:
        print("✗ NOT SIGNIFICANT: No evidence of blood pressure reduction")

    # Visualize results
    plot_wilcoxon_results(
        before_treatment,
        after_treatment,
        ("Before Treatment", "After Treatment"),
        "Blood Pressure Reduction Study",
    )

    plot_paired_data(before_treatment, after_treatment, ("Before", "After"))


def example_2_pain_management_study():
    """
    Example 2: Post-Operative Pain Management

    Scenario: Comparing pain scores (0-10 scale) before and after
    administration of a new analgesic in post-operative patients.

    Test: Wilcoxon signed-rank test (paired ordinal data)
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 2: POST-OPERATIVE PAIN MANAGEMENT STUDY")
    print("=" * 60)

    print("\nStudy Design:")
    print("- Paired design: same patients before/after analgesic")
    print("- Outcome: Pain intensity (0-10 numerical rating scale)")
    print("- Sample size: n=12 post-operative patients")
    print("- Time points: Pre-medication and 2 hours post-medication")

    # Pain scores (0=no pain, 10=worst possible pain)
    pain_before = [8, 7, 9, 6, 8, 7, 9, 8, 7, 6, 8, 9]
    pain_after = [3, 4, 5, 2, 4, 3, 5, 4, 3, 2, 4, 5]

    print(f"\nData:")
    print(f"Pain before medication: {pain_before}")
    print(f"Pain after medication:  {pain_after}")

    # Perform test
    w_stat, p_value, stats = wilcoxon_signed_rank_test(
        pain_before, pain_after, alternative="greater"
    )

    print(f"\nStatistical Analysis:")
    print(f"Test: Wilcoxon Signed-Rank Test (one-tailed)")
    print(f"H₀: Pain scores unchanged or increased")
    print(f"H₁: Pain scores decreased after medication")
    print(f"W statistic: {w_stat}")
    print(f"p-value: {p_value:.4f}")
    print(f"Mean pain reduction: {stats['mean_difference']:.1f} points")
    print(f"Median pain reduction: {stats['median_difference']:.1f} points")

    # Clinical interpretation
    print(f"\nClinical Interpretation:")
    if p_value < 0.05:
        print("✓ SIGNIFICANT: Pain significantly reduced after medication")
        if stats["median_difference"] >= 2:
            print(
                "✓ CLINICALLY MEANINGFUL: ≥2-point reduction is clinically significant"
            )
        else:
            print("? Modest but significant pain reduction")
    else:
        print("✗ NOT SIGNIFICANT: No evidence of pain reduction")

    # Count responders (≥50% pain reduction)
    responders = sum(
        1
        for before, after in zip(pain_before, pain_after)
        if (before - after) / before >= 0.5
    )
    print(f"Responders (≥50% pain reduction): {responders}/{len(pain_before)} patients")

    plot_wilcoxon_results(
        pain_before,
        pain_after,
        ("Pre-medication", "Post-medication"),
        "Post-Operative Pain Management",
    )


def example_3_drug_comparison_study():
    """
    Example 3: Comparing Two Drug Formulations

    Scenario: Comparing the efficacy of two different formulations of
    the same drug by measuring biomarker response in independent groups.

    Test: Mann-Whitney U test (independent groups, non-normal data)
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 3: DRUG FORMULATION COMPARISON STUDY")
    print("=" * 60)

    print("\nStudy Design:")
    print("- Independent groups design")
    print("- Outcome: Biomarker response (% change from baseline)")
    print("- Groups: Standard formulation vs New formulation")
    print("- Sample sizes: n₁=10, n₂=12")

    # Biomarker response (% improvement)
    standard_formulation = [15, 18, 22, 25, 19, 21, 17, 23, 20, 16]
    new_formulation = [28, 32, 35, 30, 33, 29, 31, 36, 34, 27, 30, 33]

    print(f"\nData:")
    print(f"Standard formulation: {standard_formulation}")
    print(f"New formulation:      {new_formulation}")

    # Perform Mann-Whitney U test
    u_stat, p_value, stats = mann_whitney_u_test(
        new_formulation, standard_formulation, alternative="greater"
    )

    print(f"\nStatistical Analysis:")
    print(f"Test: Mann-Whitney U Test (one-tailed)")
    print(f"H₀: New formulation ≤ Standard formulation")
    print(f"H₁: New formulation > Standard formulation")
    print(f"U statistic: {u_stat}")
    print(f"p-value: {p_value:.4f}")
    print(f"New formulation median: {stats['median1']:.1f}%")
    print(f"Standard formulation median: {stats['median2']:.1f}%")
    print(f"Median difference: {stats['median_difference']:.1f}%")

    if stats["effect_size"]:
        print(f"Effect size (r): {stats['effect_size']:.3f}")

    print(f"\nInterpretation:")
    if p_value < 0.05:
        print("✓ SIGNIFICANT: New formulation is significantly better")
        improvement = (stats["median1"] - stats["median2"]) / stats["median2"] * 100
        print(f"✓ CLINICAL IMPACT: {improvement:.1f}% relative improvement")
    else:
        print("✗ NOT SIGNIFICANT: No evidence that new formulation is better")

    plot_mann_whitney_results(
        new_formulation,
        standard_formulation,
        ("New Formulation", "Standard Formulation"),
        "Drug Formulation Efficacy Comparison",
    )

    plot_independent_groups(new_formulation, standard_formulation, ("New", "Standard"))


def example_4_biomarker_disease_study():
    """
    Example 4: Biomarker Levels in Disease vs Healthy

    Scenario: Investigating whether a novel biomarker can distinguish
    between patients with a specific disease and healthy controls.

    Test: Mann-Whitney U test (independent groups)
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 4: BIOMARKER DIAGNOSTIC STUDY")
    print("=" * 60)

    print("\nStudy Design:")
    print("- Case-control design")
    print("- Outcome: Biomarker concentration (ng/mL)")
    print("- Groups: Disease patients vs Healthy controls")
    print("- Sample sizes: n₁=15 patients, n₂=15 controls")

    # Biomarker concentrations (ng/mL)
    disease_patients = [45, 52, 48, 55, 62, 47, 59, 51, 44, 56, 49, 53, 58, 46, 54]
    healthy_controls = [28, 32, 25, 35, 30, 26, 33, 29, 31, 27, 34, 28, 30, 32, 29]

    print(f"\nData:")
    print(f"Disease patients:  {disease_patients}")
    print(f"Healthy controls:  {healthy_controls}")

    # Perform test
    u_stat, p_value, stats = mann_whitney_u_test(
        disease_patients, healthy_controls, alternative="greater"
    )

    print(f"\nStatistical Analysis:")
    print(f"Test: Mann-Whitney U Test (one-tailed)")
    print(f"H₀: Disease biomarker levels ≤ Healthy levels")
    print(f"H₁: Disease biomarker levels > Healthy levels")
    print(f"U statistic: {u_stat}")
    print(f"p-value: {p_value:.4f}")
    print(f"Disease median: {stats['median1']:.1f} ng/mL")
    print(f"Healthy median: {stats['median2']:.1f} ng/mL")
    print(f"Fold difference: {stats['median1'] / stats['median2']:.2f}")

    if stats["effect_size"]:
        print(f"Effect size (r): {stats['effect_size']:.3f}")

    # Diagnostic utility assessment
    print(f"\nDiagnostic Utility:")
    if p_value < 0.001:
        print("✓ EXCELLENT: Very strong evidence for biomarker elevation")
    elif p_value < 0.01:
        print("✓ STRONG: Strong evidence for biomarker elevation")
    elif p_value < 0.05:
        print("✓ MODERATE: Moderate evidence for biomarker elevation")
    else:
        print("✗ POOR: No evidence for biomarker elevation")

    # Simple discrimination analysis
    cutoff = (stats["median1"] + stats["median2"]) / 2
    true_positive = sum(1 for x in disease_patients if x > cutoff)
    true_negative = sum(1 for x in healthy_controls if x <= cutoff)
    sensitivity = true_positive / len(disease_patients) * 100
    specificity = true_negative / len(healthy_controls) * 100

    print(f"Using cutoff {cutoff:.1f} ng/mL:")
    print(f"Sensitivity: {sensitivity:.1f}%")
    print(f"Specificity: {specificity:.1f}%")

    plot_mann_whitney_results(
        disease_patients,
        healthy_controls,
        ("Disease Patients", "Healthy Controls"),
        "Biomarker Diagnostic Performance",
    )


def example_5_treatment_response_study():
    """
    Example 5: Treatment Response Assessment

    Scenario: Evaluating patient response to immunotherapy by measuring
    tumor size before and after treatment in cancer patients.

    Test: Wilcoxon signed-rank test (paired data with potential outliers)
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 5: CANCER IMMUNOTHERAPY RESPONSE STUDY")
    print("=" * 60)

    print("\nStudy Design:")
    print("- Paired design: tumor measurements before/after immunotherapy")
    print("- Outcome: Tumor diameter (cm)")
    print("- Sample size: n=10 cancer patients")
    print("- Treatment duration: 12 weeks")

    # Tumor diameters (cm)
    tumor_baseline = [4.2, 3.8, 5.1, 2.9, 6.3, 3.5, 4.7, 5.8, 3.2, 4.1]
    tumor_week12 = [3.1, 2.9, 4.2, 2.1, 4.8, 2.7, 3.2, 4.1, 2.4, 3.0]

    print(f"\nData:")
    print(f"Baseline tumor size: {tumor_baseline}")
    print(f"Week 12 tumor size:  {tumor_week12}")

    # Calculate percent changes
    percent_changes = [
        (baseline - week12) / baseline * 100
        for baseline, week12 in zip(tumor_baseline, tumor_week12)
    ]

    print(f"Percent reductions:  {[f'{x:.1f}%' for x in percent_changes]}")

    # Perform test
    w_stat, p_value, stats = wilcoxon_signed_rank_test(
        tumor_baseline, tumor_week12, alternative="greater"
    )

    print(f"\nStatistical Analysis:")
    print(f"Test: Wilcoxon Signed-Rank Test (one-tailed)")
    print(f"H₀: No tumor shrinkage")
    print(f"H₁: Tumor shrinkage after immunotherapy")
    print(f"W statistic: {w_stat}")
    print(f"p-value: {p_value:.4f}")
    print(f"Mean size reduction: {stats['mean_difference']:.2f} cm")
    print(f"Median size reduction: {stats['median_difference']:.2f} cm")

    # Clinical response assessment
    print(f"\nClinical Response Assessment:")
    complete_response = sum(1 for after in tumor_week12 if after == 0)
    partial_response = sum(
        1
        for baseline, after in zip(tumor_baseline, tumor_week12)
        if (baseline - after) / baseline >= 0.3 and after > 0
    )
    stable_disease = sum(
        1
        for baseline, after in zip(tumor_baseline, tumor_week12)
        if abs(baseline - after) / baseline < 0.3
    )
    progressive_disease = sum(
        1
        for baseline, after in zip(tumor_baseline, tumor_week12)
        if (after - baseline) / baseline > 0.2
    )

    print(f"Complete Response (CR): {complete_response}/10 patients")
    print(f"Partial Response (PR): {partial_response}/10 patients")
    print(f"Stable Disease (SD): {stable_disease}/10 patients")
    print(f"Progressive Disease (PD): {progressive_disease}/10 patients")

    overall_response_rate = (complete_response + partial_response) / 10 * 100
    print(f"Overall Response Rate: {overall_response_rate:.1f}%")

    if p_value < 0.05:
        print("✓ SIGNIFICANT: Immunotherapy shows statistical efficacy")
        if overall_response_rate >= 20:
            print("✓ CLINICALLY MEANINGFUL: Response rate suggests clinical benefit")
    else:
        print("✗ NOT SIGNIFICANT: No evidence of immunotherapy efficacy")

    plot_wilcoxon_results(
        tumor_baseline,
        tumor_week12,
        ("Baseline", "Week 12"),
        "Immunotherapy Response Assessment",
    )


def run_all_examples():
    """Run all biomedical examples with a summary."""
    print("BIOMEDICAL STATISTICAL ANALYSIS EXAMPLES")
    print("=" * 80)
    print("This script demonstrates practical applications of non-parametric")
    print("statistical tests in biomedical research scenarios.")
    print("\nTests demonstrated:")
    print("• Wilcoxon Signed-Rank Test (paired/dependent data)")
    print("• Mann-Whitney U Test (independent groups)")
    print("\nScenarios covered:")
    print("• Clinical trials and drug studies")
    print("• Diagnostic biomarker research")
    print("• Treatment response assessment")
    print("• Pain and symptom management")

    # Run all examples
    example_1_blood_pressure_study()
    example_2_pain_management_study()
    example_3_drug_comparison_study()
    example_4_biomarker_disease_study()
    example_5_treatment_response_study()

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY OF KEY LEARNING POINTS")
    print("=" * 80)
    print("\n1. TEST SELECTION:")
    print("   • Use Wilcoxon for paired/dependent data")
    print("   • Use Mann-Whitney for independent groups")
    print("   • Both handle non-normal data well")

    print("\n2. INTERPRETATION:")
    print("   • p-value indicates statistical significance")
    print("   • Effect size indicates practical importance")
    print("   • Always consider clinical significance")

    print("\n3. REPORTING:")
    print("   • State test used and justification")
    print("   • Report exact p-values when possible")
    print("   • Include effect sizes and confidence intervals")
    print("   • Provide clinical interpretation")

    print("\n4. ASSUMPTIONS:")
    print("   • Independence of observations")
    print("   • Ordinal or continuous data")
    print("   • For location comparisons: similar distribution shapes")

    print("\nFor more details, see the README.md file!")
    print("Happy analyzing! 🧬📊")


if __name__ == "__main__":
    run_all_examples()
