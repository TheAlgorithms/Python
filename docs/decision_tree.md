# Decision Tree Algorithm

## Overview
A **Decision Tree** is a supervised machine learning algorithm used for both classification and regression tasks.
It works by recursively splitting the dataset into smaller subsets based on feature values until a stopping criterion is met.

---

## Mathematical Concept

Decision Trees use measures like **Entropy**, **Information Gain**, and **Gini Impurity** to decide where to split.

### 1. Entropy
Entropy measures the amount of uncertainty or impurity in the dataset:

H(S) = - Σ p(x) log₂ p(x)


Where:
- `p(x)` = probability of class `x`
- Lower entropy = more pure dataset

---

### 2. Information Gain
Information Gain measures the reduction in entropy after splitting on an attribute:



IG(S, A) = H(S) - Σ ( |Sv| / |S| ) * H(Sv)


Where:
- `S` = dataset
- `A` = attribute (feature)
- `Sv` = subset after splitting by `A`

A split with the **highest information gain** is chosen.

---

### 3. Gini Index
An alternative to entropy for impurity:



Gini(S) = 1 - Σ (p(i)²)


Where:
- `p(i)` = probability of class `i` in dataset `S`

A pure dataset has Gini = 0.

---

## Practical Use Cases
- **Business**: Predicting customer churn
- **Finance**: Credit scoring / loan approval
- **Healthcare**: Diagnosing diseases based on symptoms
- **Cybersecurity**: Spam / phishing detection

---

## Advantages
- Simple to understand and visualize
- Handles both numerical and categorical data
- Requires little preprocessing (no normalization or scaling)

---

## Limitations
- Prone to overfitting (can be solved using pruning or ensembles like Random Forests)
- Small changes in data can lead to different trees (instability)

---

## Example Usage

```python
from machine_learning.decision_tree import DecisionTree

# Sample dataset
X = [[1], [2], [3], [4], [5]]
y = [0, 0, 1, 1, 1]

# Train model
tree = DecisionTree(max_depth=2)
tree.fit(X, y)

# Prediction
print(tree.predict([[2]]))   # Output: [0]