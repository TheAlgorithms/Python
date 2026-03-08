# Algorithms Implementation Status (Focused Snapshot)

This document provides a **focused, maintainable status view** for recently reworked
algorithms, including complexity notes and quick usage snippets.

## Machine Learning

| Module | Status | Time Complexity (high-level) | Space Complexity | Notes |
|---|---|---:|---:|---|
| `machine_learning/gaussian_naive_bayes.py` | OK | Train: `O(n * d)` / Predict: `O(k * c * d)` | `O(c * d)` | Multi-class Gaussian Naive Bayes in pure Python. |
| `machine_learning/random_forest_classifier.py` | OK | Approx. `O(t * n * d)` | `O(t)` stumps | Bagged decision stumps + feature subsampling. |
| `machine_learning/random_forest_regressor.py` | OK | Approx. `O(t * n * d)` | `O(t)` stumps | Regression version using averaged stump outputs. |
| `machine_learning/gradient_boosting_regressor.py` | OK | Approx. `O(m * n)` (single-feature weak learner) | `O(m)` | Residual fitting with weighted stumps. |
| `neural_network/perceptron.py` | OK | Train: `O(e * n * d)` / Predict: `O(d)` | `O(d)` | Binary labels `{-1, 1}` with deterministic behavior. |

- `n`: number of samples, `d`: number of features, `c`: number of classes,
  `t`: number of trees, `m`: number of boosting rounds, `e`: epochs.

## Searches and Sorts (tested snapshot)

| Module | Status | Time Complexity | Space Complexity |
|---|---|---:|---:|
| `searches/binary_search.py` | OK | Best `O(1)`, Avg/Worst `O(log n)` | `O(1)` |
| `sorts/insertion_sort.py` | OK | Best `O(n)`, Avg/Worst `O(n^2)` | `O(1)` |

## Quick usage examples

```python
from machine_learning.gaussian_naive_bayes import GaussianNaiveBayes

model = GaussianNaiveBayes().fit([[1.0, 2.0], [5.0, 8.0]], [0, 1])
print(model.predict([[1.1, 2.1], [4.9, 7.9]]))
```

```python
from machine_learning.random_forest_classifier import RandomForestClassifier

clf = RandomForestClassifier(num_trees=25, random_seed=42)
clf.fit([[0.0], [0.1], [1.0], [1.2]], [0, 0, 1, 1])
print(clf.predict([[0.05], [1.1]]))
```


## Benchmark helper

Run `python examples/ml_benchmarks.py` to compare pure-Python model timings and optional scikit-learn baselines (when installed).

## References

- Binary search: <https://en.wikipedia.org/wiki/Binary_search_algorithm>
- Insertion sort: <https://en.wikipedia.org/wiki/Insertion_sort>
- Naive Bayes classifier: <https://en.wikipedia.org/wiki/Naive_Bayes_classifier>
- Random forest: Breiman, L. (2001). Random Forests. *Machine Learning*.
- Gradient boosting: Friedman, J. H. (2001). Greedy Function Approximation.

- Hastie, Tibshirani, Friedman. *The Elements of Statistical Learning* (ESL).
- James, Witten, Hastie, Tibshirani. *An Introduction to Statistical Learning* (ISLR).
- Rosenblatt, F. (1958). The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain.


## Quantum (restored snapshot)

| Module | Status | Time Complexity | Space Complexity |
|---|---|---:|---:|
| `quantum/bb84.py` | OK | `O(key_len)` | `O(key_len)` |
| `quantum/deutsch_jozsa.py` | OK | `O(2^n)` | `O(1)` |
| `quantum/superdense_coding.py` | OK | `O(1)` | `O(1)` |
| `quantum/quantum_teleportation.py` | OK | `O(1)` | `O(1)` |
| `quantum/ripple_adder_classic.py` | OK | `O(max_bits)` | `O(1)` |
