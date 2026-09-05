# Project Overview

TheAlgorithms/Python is an open-source collection of algorithms implemented in Python. TheAlgorithms organization provides implementations of algorithms in various programming languages; for this project, we chose the Python repository.

The project contains implementations across numerous categories, including mathematics, data structures, sorting, machine learning, computer vision, and more.

# Key Quality Metrics

* **Correctness**

  * How reliably do algorithm implementations produce the expected results?
  * Measured using existing test cases and additional tests developed throughout the project.

* **Maintainability**

  * How easily can algorithm implementations be understood and modified?
  * **Code Structure**

    * Lines of Code (LOC)
    * LOC per file and category
    * Comment density
    * Code complexity

* **Testability**

  * How thoroughly is the project currently tested?
  * Measured using:

    * Number of explicit test suites
    * Number of explicit test cases
    * Number of doctests
    * Test coverage

# How to Run the Metrics

## Maintainability Metrics

Run the LOC and comment-density metric collector from the repository root:

```bash
python courseProjectCode/Metrics/loc_counter.py
```
Outputs for loc_counter.py are stored in ```courseProjectCode/Metrics/loc_results.py```

The script analyzes Python files throughout the repository and reports LOC, comment count, and comment density by category.

## Testability Metrics

Run the test counter from the repository root:

```bash
python courseProjectCode/Metrics/test_counter.py
```
Outputs for test_counter.py are stored in ```courseProjectCode/Metrics/test_results.csv```

The script uses Python's Abstract Syntax Tree (AST) to statically analyze the repository's explicit test files and count test suites and test cases without executing the tests.

### Testing Environment and Limitations

The project's automated tests are primarily executed through a Linux-based CI environment. Attempts to reproduce the complete test suite on Windows encountered dependency compatibility issues, particularly with TensorFlow and OpenCV.

Therefore, test_counter.py uses static AST analysis to identify and count existing test suites and test cases without executing them. This metric measures the presence of tests, not whether the tests pass or fail. Test execution and coverage are evaluated separately.

### Scope

* Explicit test files beginning with `test_` are analyzed.
* Test functions and methods beginning with `test_` are counted as test cases.
* The static count represents test definitions in the source code and may differ from the number of tests collected by pytest
