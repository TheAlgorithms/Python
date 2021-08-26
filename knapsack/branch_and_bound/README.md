# Least Cost Branch and Bound algorithm to solve 0-1 Knapsack Problem

The overview is taken from:
https://en.wikipedia.org/wiki/Branch_and_bound
https://www.geeksforgeeks.org/0-1-knapsack-using-least-count-branch-and-bound/#:~:text=Branch%20and%20Bound%20can%20be,one%20with%20the%20least%20cost.

---

## Overview

Branch and bound (BB, B&B, or BnB) is an algorithm design paradigm for discrete and combinatorial optimization problems, as well as mathematical optimization. A branch-and-bound algorithm consists of a systematic enumeration of candidate solutions by means of state space search: the set of candidate solutions is thought of as forming a rooted tree with the full set at the root. The algorithm explores branches of this tree, which represent subsets of the solution set. Before enumerating the candidate solutions of a branch, the branch is checked against upper and lower estimated bounds on the optimal solution, and is discarded if it cannot produce a better solution than the best one found so far by the algorithm.

The least cost(LC) is considered the most intelligent as it selects the next node based on a Heuristic Cost Function. It picks the one with the least cost.
As 0/1 Knapsack is about maximizing the total value, we cannot directly use the LC Branch and Bound technique to solve this. Instead, we convert this into a minimization problem by taking negative of the given values.
Follow the steps below to solve the problem:

1. Sort the items based on their value/weight(V/W) ratio.
2. Insert a dummy node into the priority queue.
3. Repeat the following steps until the priority queue is empty:
   - Extract the peek element from the priority queue and assign it to the current node.
   - If the upper bound of the current node is less than minLB, the minimum lower bound of all the nodes explored, then there is no point of exploration. So, continue with the next element. The reason for not considering the nodes whose upper bound is greater than minLB is that, the upper bound stores the best value that might be achieved. If the best value itself is not optimal than minLB, then exploring that path is of no use.
   - Update the path array.
   - If the current node’s level is N, then check whether the lower bound of the current node is less than finalLB, minimum lower bound of all the paths that reached the final level. If it is true, update the finalPath and finalLB. Otherwise, continue with the next element.
   - Calculate the lower and upper bounds of the right child of the current node.
   - If the current item can be inserted into the knapsack, then calculate the lower and upper bound of the left child of the current node.
   - Update the minLB and insert the children if their upper bound is less than minLB.

---

## Usage

Import the folder 'BranchAndBound' into your project.

---

## Text File

#### Sample Data

Ant Repellent,1,2
Blanket,4,3
Brownies,3,10
Frisbee,1,6
Salad,5,4
Watermelon,10,10

#### Text File Formatting

The data is seperated by ','
First data is the name of item.
Second data is the weight of item.
Third data is the rating of the item.
(Name,Weight,Rating)

## Tests

To be completed.

---
