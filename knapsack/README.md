# A naive recursive implementation of 0-1 Knapsack Problem

This overview is taken from:

    https://en.wikipedia.org/wiki/Knapsack_problem

---

## Overview

The knapsack problem is a problem in combinatorial optimization: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. It derives its name from the problem faced by someone who is constrained by a fixed-size knapsack and must fill it with the most valuable items. The problem often arises in resource allocation where the decision makers have to choose from a set of non-divisible projects or tasks under a fixed budget or time constraint, respectively.

There are 3 approaches to solve the knapsack problem-
1. Brute Force approach-
Brute force is a straightforward approach to solving a problem, based on the problem statement and definitions of the concepts involved.
According to it, if there are n given items, then there will be 2^n possible combinations of the items to be chosen for the knapsack. A bit string of 0’s and 1’s of length n is generated such that if the i^th symbol of a bit string is 0, then the i^th item is not chosen and if it is 1, the i^th item is chosen. Provided that an item is either chosen completely or not chosen at all.
2. Greedy apprach-
Greedy approach is used for optimization.
According to it, for the given weights and values of N items, put the items in the knapsack of capacity W to get the maximum total value in the knapsack. The value of the items can be broken into fraction for maximizing the total value of the knapsack. therefore, it is also known as fractional knapsack.
3. Dynamic Programming approach -
Dynamic Programming is a technique for solving problems whose solutions satisfy recurrence relations with overlapping subproblems.
according to it, for a given N items where each item is having some weight (wi) and value (vi) and the capacity of knapsack is W. The aim is to put the items such that the sum of item values is the maximum. Provided that an item is either chosen completely or not chosen at all.
This approach has a lower time and space complexity than other approaches and is more effective.

The knapsack problem has been studied for more than a century, with early works dating as far back as 1897 The name "knapsack problem" dates back to the early works of mathematician Tobias Dantzig (1884–1956), and refers to the commonplace problem of packing the most valuable or useful items without overloading the luggage.

---

## Documentation

This module uses docstrings to enable the use of Python's in-built `help(...)` function.
For instance, try `help(Vector)`, `help(unit_basis_vector)`, and `help(CLASSNAME.METHODNAME)`.

---

## Usage

Import the module `knapsack.py` from the **.** directory into your project.

---

## Tests

`.` contains Python unit tests which can be run with `python3 -m unittest -v`.
