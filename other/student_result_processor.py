"""
Student Result Processor

This module provides utility functions to process student results,
including separating passed and failed students, identifying top
performers, and calculating pass percentage.
"""


def separate_students(students, pass_mark=75):
    """
    Separate students into passed and failed lists.

    :param students: List of dictionaries with keys 'name' and 'marks'
    :param pass_mark: Minimum marks required to pass
    :return: Tuple (passed_students, failed_students)
    """
    passed = [s for s in students if s["marks"] >= pass_mark]
    failed = [s for s in students if s["marks"] < pass_mark]
    return passed, failed


def top_performers(students, threshold=90):
    """
    Get students scoring above a given threshold.

    :param students: List of student dictionaries
    :param threshold: Minimum marks for top performers
    :return: List of top-performing students
    """
    return [s for s in students if s["marks"] >= threshold]


def pass_percentage(students, pass_mark=75):
    """
    Calculate pass percentage.

    :param students: List of student dictionaries
    :param pass_mark: Minimum marks required to pass
    :return: Pass percentage as float
    """
    if not students:
        return 0.0

    passed_count = sum(1 for s in students if s["marks"] >= pass_mark)
    return (passed_count / len(students)) * 100


if __name__ == "__main__":
    sample_students = [
        {"name": "Pranav", "marks": 90},
        {"name": "Amit", "marks": 40},
        {"name": "Sneha", "marks": 95},
        {"name": "Rahul", "marks": 72},
    ]

    passed, failed = separate_students(sample_students)
    top = top_performers(sample_students)
    percentage = pass_percentage(sample_students)

    print("Passed:", passed)
    print("Failed:", failed)
    print("Top Performers:", top)
    print("Pass Percentage:", percentage)
