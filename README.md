<div align="center">
<!-- Title: -->
  <a href="https://github.com/TheAlgorithms/">
    <img src="https://raw.githubusercontent.com/TheAlgorithms/website/1cd824df116b27029f17c2d1b42d81731f28a920/public/logo.svg" height="100">
  </a>
  <h1><a href="https://github.com/TheAlgorithms/">The Algorithms</a> - Python</h1>

<!-- Labels: -->
  <!-- First row: -->
  <a href="https://gitpod.io/#https://github.com/TheAlgorithms/Python">
    <img src="https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod&style=flat-square" height="20" alt="Gitpod Ready-to-Code">
  </a>
  <a href="https://github.com/TheAlgorithms/Python/blob/master/CONTRIBUTING.md">
    <img src="https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square" height="20" alt="Contributions Welcome">
  </a>
  <img src="https://img.shields.io/github/repo-size/TheAlgorithms/Python.svg?label=Repo%20size&style=flat-square" height="20">
  <a href="https://the-algorithms.com/discord">
    <img src="https://img.shields.io/discord/808045925556682782.svg?logo=discord&colorB=7289DA&style=flat-square" height="20" alt="Discord chat">
  </a>
  <a href="https://gitter.im/TheAlgorithms/community">
    <img src="https://img.shields.io/badge/Chat-Gitter-ff69b4.svg?label=Chat&logo=gitter&style=flat-square" height="20" alt="Gitter chat">
  </a>

  <!-- Second row: -->
  <br>
  <a href="https://github.com/TheAlgorithms/Python/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/TheAlgorithms/Python/build.yml?branch=master&label=CI&logo=github&style=flat-square" height="20" alt="GitHub Workflow Status">
  </a>
  <a href="https://github.com/pre-commit/pre-commit">
    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square" height="20" alt="pre-commit">
  </a>
  <a href="https://docs.astral.sh/ruff/formatter/">
    <img src="https://img.shields.io/static/v1?label=code%20style&message=ruff&color=black&style=flat-square" height="20" alt="code style: black">
  </a>

<!-- Short description: -->
  <h3>All algorithms implemented in Python - for education 📚</h3>
</div>

Implementations are for learning purposes only. They may be less efficient than the implementations in the Python standard library. Use them at your discretion.

## � Table of Contents

- [About](#-about)
- [Features](#-features)
- [Getting Started](#-getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [Algorithm Categories](#-algorithm-categories)
- [Community Channels](#-community-channels)
- [Contributing](#-contributing)
- [License](#-license)
- [List of Algorithms](#-list-of-algorithms)

## � About

This repository contains Python implementations of various algorithms and data structures for educational purposes. Whether you're a student learning algorithms, a developer preparing for technical interviews, or someone interested in computer science fundamentals, this collection provides clear and well-documented examples.

## ✨ Features

This repository includes implementations of algorithms across multiple categories:

- **Sorting Algorithms**: Bubble sort, Quick sort, Merge sort, Heap sort, and more
- **Searching Algorithms**: Binary search, Linear search, Jump search, Interpolation search
- **Data Structures**: Linked lists, Stacks, Queues, Trees, Graphs, Hash tables
- **Graph Algorithms**: BFS, DFS, Dijkstra's algorithm, Floyd-Warshall, Bellman-Ford
- **Dynamic Programming**: Knapsack, Longest Common Subsequence, Edit Distance
- **Machine Learning**: Neural networks, Linear regression, K-means clustering
- **Mathematical Algorithms**: Prime number algorithms, GCD, LCM, Number theory
- **String Algorithms**: Pattern matching, String manipulation, Parsing
- **Cryptography**: Various cipher implementations
- **Computer Vision**: Image processing algorithms
- **And many more!**

All implementations include:
- Clear documentation and explanations
- Type hints for better code readability
- Doctests for validation
- Educational comments

## 🚀 Getting Started

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/TheAlgorithms/Python.git
   cd Python
   ```

2. **Set up a virtual environment (recommended)**
   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

Each algorithm is self-contained in its own file. You can run any algorithm directly or import it into your own projects.

**Example 1: Running an algorithm directly**
```bash
python sorts/quick_sort.py
```

**Example 2: Importing and using an algorithm**
```python
from sorts.quick_sort import quick_sort

# Sort a list
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = quick_sort(numbers)
print(sorted_numbers)  # Output: [11, 12, 22, 25, 34, 64, 90]
```

**Example 3: Running doctests**
```bash
python -m doctest -v sorts/bubble_sort.py
```

## 📂 Algorithm Categories

For a complete list of all implemented algorithms organized by category, see our [DIRECTORY.md](DIRECTORY.md) file.

## 🌐 Community Channels

We are on [Discord](https://the-algorithms.com/discord) and [Gitter](https://gitter.im/TheAlgorithms/community)! Community channels are a great way for you to ask questions and get help. Please join us!

## 🤝 Contributing

We welcome contributions from the community! Before contributing:

1. 📋 Read through our [Contribution Guidelines](CONTRIBUTING.md)
2. 🔍 Check existing implementations to avoid duplicates
3. ✅ Ensure your code follows our coding standards
4. 🧪 Include doctests and proper documentation
5. 🎯 Make sure all tests pass before submitting

**Quick Start for Contributors:**
```bash
# Install pre-commit hooks
pip install pre-commit
pre-commit install

# Run tests
python -m pytest

# Format code
pip install ruff
ruff check
```

Contributions that are most welcome:
- New algorithm implementations
- Improvements to existing algorithms
- Better documentation and explanations
- Bug fixes
- Test coverage improvements

## 📄 License

This project is licensed under the [MIT License](LICENSE.md) - see the [LICENSE.md](LICENSE.md) file for details.

This means you are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software.

## 📜 List of Algorithms

See our [directory](DIRECTORY.md) for easier navigation and a better overview of the project.
