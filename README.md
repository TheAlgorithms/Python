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

> **Note**: These implementations are for **learning purposes** only. They may be less efficient than the implementations in the Python standard library. Use them at your discretion.

---

### 🌟 Quick Links

[🚀 Get Started](#-getting-started) • [📖 Browse Algorithms](DIRECTORY.md) • [💻 Code Examples](#-usage-examples) • [🤝 Contribute](CONTRIBUTING.md) • [💬 Join Discord](https://the-algorithms.com/discord)

---

## 📑 Table of Contents

- [✨ Why Choose This Repository?](#-why-choose-this-repository)
- [🚀 Getting Started](#-getting-started)
- [📚 Algorithm Categories](#-algorithm-categories)
- [💡 Usage Examples](#-usage-examples)
- [🤝 Contributing](#-contributing)
- [🌐 Community Channels](#-community-channels)
- [🎓 Learning Path](#-learning-path)
- [🛠️ Development Setup](#️-development-setup)
- [🧪 Testing](#-testing)
- [📊 Project Stats](#-project-stats)
- [📖 Resources](#-resources)
- [🏆 Top Contributors](#-top-contributors)
- [📜 License](#-license)
- [💬 Get Help](#-get-help)
- [⭐ Show Your Support](#-show-your-support)

## ✨ Why Choose This Repository?

- **🎓 Perfect for Learning**: Clean, well-commented code designed specifically for educational purposes
- **📈 1300+ Implementations**: One of the most comprehensive algorithm collections on GitHub
- **✅ Quality Assured**: Every algorithm includes tests and passes continuous integration
- **🌍 Community-Driven**: Thousands of contributors worldwide, actively maintained
- **📝 Well-Documented**: Detailed docstrings, complexity analysis, and usage examples
- **🔬 Multiple Domains**: From basic sorting to machine learning, cryptography to computer vision
- **🚀 Ready to Use**: Copy, learn from, and adapt code for your projects
- **🎯 Interview Prep**: Perfect resource for coding interviews and competitive programming

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/TheAlgorithms/Python.git
cd Python
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run any algorithm:
```bash
python3 sorts/quick_sort.py
python3 searches/binary_search.py
```

### Running Tests

```bash
pytest
```

## 📚 Algorithm Categories

<table>
<tr>
<td width="50%">

**Computer Science Fundamentals**
- 🗂️ Data Structures (Arrays, Trees, Graphs, Heaps)
- 🔄 Sorting (Quick, Merge, Heap, Radix, etc.)
- 🔍 Searching (Binary, Ternary, Jump, etc.)
- 🔙 Backtracking (N-Queens, Sudoku, Maze)
- 🌊 Divide and Conquer
- 💰 Dynamic Programming
- 🎯 Greedy Algorithms
- 📊 Graph Algorithms (BFS, DFS, Dijkstra, Floyd-Warshall)

**Mathematics & Science**
- ➕ Mathematical Algorithms
- 🔢 Number Theory
- 📐 Geometry & Computational Geometry
- 🧮 Linear Algebra & Matrix Operations
- 📈 Statistics & Probability
- ⚛️ Physics Simulations
- 🌍 Geodesy

</td>
<td width="50%">

**Machine Learning & AI**
- 🤖 Machine Learning (Regression, Classification)
- 🧠 Neural Networks
- 🧬 Genetic Algorithms
- 🎲 Fuzzy Logic
- 📊 Data Mining

**Applied Computer Science**
- 🔐 Cryptography & Ciphers
- 🖼️ Computer Vision
- 🎨 Digital Image Processing
- 🎵 Audio Filters
- 🌐 Web Programming
- 📡 Networking & Data Transfer
- 🗜️ Data Compression
- 💹 Financial Algorithms
- ⚡ Electronics & Circuit Design

</td>
</tr>
</table>

📖 See our complete **[DIRECTORY.md](DIRECTORY.md)** for the full list of all 1300+ implementations.

## 💡 Usage Examples

### Quick Start - Sorting
```python
from sorts.quick_sort import quick_sort

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)
print(sorted_arr)  # [11, 12, 22, 25, 34, 64, 90]
```

### Binary Search
```python
from searches.binary_search import binary_search

sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 7
index = binary_search(sorted_list, target)
print(f"Found {target} at index {index}")  # Found 7 at index 3
```

### Graph Algorithms - Dijkstra's Shortest Path
```python
from graphs.dijkstra import dijkstra

# Graph represented as adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}

distances = dijkstra(graph, 'A')
print(distances)  # {'A': 0, 'B': 1, 'C': 3, 'D': 4}
```

### Machine Learning - Linear Regression
```python
from machine_learning.linear_regression import LinearRegression

X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

model = LinearRegression()
model.fit(X, y)
prediction = model.predict([[6]])
print(prediction)  # ~12
```

### Cryptography - Caesar Cipher
```python
from ciphers.caesar_cipher import encrypt, decrypt

message = "HELLO WORLD"
encrypted = encrypt(message, shift=3)
print(encrypted)  # "KHOOR ZRUOG"

decrypted = decrypt(encrypted, shift=3)
print(decrypted)  # "HELLO WORLD"
```

## 🤝 Contributing

We love contributions! This project exists thanks to all the people who contribute.

📋 Read through our [Contribution Guidelines](CONTRIBUTING.md) before you contribute.

### How to Contribute

1. Fork the repository
2. Create a new branch (`git checkout -b feature/algorithm-name`)
3. Make your changes and commit (`git commit -am 'Add new algorithm'`)
4. Push to the branch (`git push origin feature/algorithm-name`)
5. Create a Pull Request

## 🌐 Community Channels

We are on [Discord](https://the-algorithms.com/discord) and [Gitter](https://gitter.im/TheAlgorithms/community)! Community channels are a great way for you to ask questions and get help. Please join us!

## 🎓 Learning Path

New to algorithms? Follow this recommended learning path:

1. **Start with Basics**: `sorts/` → `searches/` → `data_structures/`
2. **Build Foundation**: `recursion/` → `backtracking/` → `divide_and_conquer/`
3. **Advanced Topics**: `dynamic_programming/` → `graphs/` → `greedy_methods/`
4. **Specialized Areas**: `machine_learning/` → `ciphers/` → `neural_network/`

Each directory contains a README with explanations and complexity analysis.

## 🛠️ Development Setup

### Using Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Using pre-commit hooks
```bash
pip install pre-commit
pre-commit install
```

This will automatically format your code and run checks before each commit.

## 🧪 Testing

```bash
# Run all tests
pytest

# Run tests for a specific module
pytest sorts/test_sorts.py

# Run with coverage
pytest --cov=. --cov-report=html
```

## 📊 Project Stats

- **Total Implementations**: 1300+ algorithms
- **Lines of Code**: 100,000+
- **Contributors**: 1000+
- **Stars**: Check the repo!
- **Programming Language**: Python 3.8+

## 📖 Resources

- 🌐 [The Algorithms Website](https://the-algorithms.com/)
- 📚 [Python Algorithm Documentation](https://the-algorithms.com/language/python)
- 📝 [Contributing Guide](CONTRIBUTING.md)
- 🤝 [Code of Conduct](https://github.com/TheAlgorithms/.github/blob/master/CODE_OF_CONDUCT.md)
- 🎥 [Video Tutorials](https://www.youtube.com/c/thealgorithms)

## 🏆 Top Contributors

A huge thanks to all our contributors! This project wouldn't be possible without you.

<a href="https://github.com/TheAlgorithms/Python/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=TheAlgorithms/Python" />
</a>

## 📜 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 💬 Get Help

- 📫 Create an [Issue](https://github.com/TheAlgorithms/Python/issues/new/choose) for bug reports or feature requests
- 💭 Join our [Discord](https://the-algorithms.com/discord) for discussions
- 🗨️ Ask questions on [Gitter](https://gitter.im/TheAlgorithms/community)

## ⭐ Show Your Support

If you find this project helpful:
- Give it a ⭐ star on GitHub
- Share it with your friends and colleagues
- Contribute by adding new algorithms or improving existing ones
- Help us translate documentation

---

<div align="center">
  Made with ❤️ by <a href="https://github.com/TheAlgorithms/Python/graphs/contributors">contributors</a> around the 🌍
  <br>
  <sub>Happy Coding! 🚀</sub>
</div>
