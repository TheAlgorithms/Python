# Testing and Coverage Guide

This guide explains how to run lint, tests, coverage, and optional benchmarks
for the recently restored algorithms.

## 1) Lint checks

```bash
ruff check machine_learning/ neural_network/ tests/ examples/
```

## 2) Run focused tests

```bash
python -m pytest \
  tests/test_machine_learning_ensembles.py \
  tests/test_searches_and_sorts_core.py \
  machine_learning/gaussian_naive_bayes.py \
  machine_learning/random_forest_classifier.py \
  machine_learning/random_forest_regressor.py \
  machine_learning/gradient_boosting_regressor.py \
  neural_network/perceptron.py
```

## 3) Coverage report

The project can export `coverage.xml` for CI/reporting.

```bash
python -m pytest \
  --cov=machine_learning \
  --cov=neural_network \
  --cov=searches \
  --cov=sorts \
  --cov-report=xml:coverage.xml \
  tests/test_machine_learning_ensembles.py \
  tests/test_searches_and_sorts_core.py
```

If this command fails with `unrecognized arguments: --cov=...`, install
`pytest-cov` first:

```bash
python -m pip install pytest-cov
```

## 4) Optional benchmark run

```bash
python examples/ml_benchmarks.py
```

The benchmark script compares fit/predict time for local pure-Python modules and
compares against scikit-learn if it is available in your environment.

## Recommendation for maintainers

To improve CI quality gates, consider adding a dedicated GitHub Actions job that:

1. Installs `pytest-cov`
2. Runs coverage export (`coverage.xml`)
3. Uploads coverage artifacts
4. Optionally enforces a minimum coverage threshold for critical directories
