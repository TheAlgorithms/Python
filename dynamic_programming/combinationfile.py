"""
The Algorithms - Python
A comprehensive collection of algorithm implementations
"""

# ============================================================================
# SORTING ALGORITHMS
# ============================================================================


def bubble_sort(arr):
    """Bubble Sort - O(n^2)"""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def quick_sort(arr):
    """Quick Sort - O(n log n) average"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    """Merge Sort - O(n log n)"""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    """Helper function for merge sort"""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def insertion_sort(arr):
    """Insertion Sort - O(n^2)"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# ============================================================================
# SEARCHING ALGORITHMS
# ============================================================================


def binary_search(arr, target):
    """Binary Search - O(log n) - requires sorted array"""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def linear_search(arr, target):
    """Linear Search - O(n)"""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def jump_search(arr, target):
    """Jump Search - O(√n) - requires sorted array"""
    import math

    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[prev] == target:
        return prev

    return -1


# ============================================================================
# GRAPH ALGORITHMS
# ============================================================================


def bfs(graph, start):
    """Breadth-First Search"""
    visited = set()
    queue = [start]
    result = []

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            queue.extend([n for n in graph[vertex] if n not in visited])

    return result


def dfs(graph, start, visited=None):
    """Depth-First Search"""
    if visited is None:
        visited = set()

    visited.add(start)
    result = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))

    return result


def dijkstra(graph, start):
    """Dijkstra's Shortest Path Algorithm"""
    import heapq

    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    visited = set()

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if curr_node in visited:
            continue

        visited.add(curr_node)

        for neighbor, weight in graph[curr_node].items():
            distance = curr_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# ============================================================================
# DYNAMIC PROGRAMMING
# ============================================================================


def fibonacci(n, memo={}):
    """Fibonacci with Memoization - O(n)"""
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


def knapsack(weights, values, capacity):
    """0/1 Knapsack Problem"""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


def longest_common_subsequence(s1, s2):
    """Longest Common Subsequence"""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


# ============================================================================
# STRING ALGORITHMS
# ============================================================================


def kmp_search(text, pattern):
    """Knuth-Morris-Pratt String Matching"""

    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    i = j = 0
    indices = []

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            indices.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return indices


def is_palindrome(s):
    """Check if string is palindrome"""
    return s == s[::-1]


# ============================================================================
# MATHEMATICAL ALGORITHMS
# ============================================================================


def gcd(a, b):
    """Greatest Common Divisor - Euclidean Algorithm"""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Least Common Multiple"""
    return abs(a * b) // gcd(a, b)


def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def sieve_of_eratosthenes(limit):
    """Generate all primes up to limit"""
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False

    return [i for i in range(limit + 1) if primes[i]]


def power(base, exp):
    """Fast Exponentiation - O(log n)"""
    if exp == 0:
        return 1
    if exp == 1:
        return base

    if exp % 2 == 0:
        half = power(base, exp // 2)
        return half * half
    else:
        return base * power(base, exp - 1)


# ============================================================================
# DATA STRUCTURE IMPLEMENTATIONS
# ============================================================================


class Stack:
    """Stack Implementation"""

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None

    def peek(self):
        return self.items[-1] if self.items else None

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    """Queue Implementation"""

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if self.items else None

    def is_empty(self):
        return len(self.items) == 0


# ============================================================================
# DEMONSTRATION
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("THE ALGORITHMS - PYTHON IMPLEMENTATION")
    print("=" * 60)

    # Sorting
    print("\n--- SORTING ALGORITHMS ---")
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {arr}")
    print(f"Quick Sort: {quick_sort(arr.copy())}")
    print(f"Merge Sort: {merge_sort(arr.copy())}")

    # Searching
    print("\n--- SEARCHING ALGORITHMS ---")
    sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    print(f"Array: {sorted_arr}, Target: {target}")
    print(f"Binary Search: Index {binary_search(sorted_arr, target)}")

    # Graph Algorithms
    print("\n--- GRAPH ALGORITHMS ---")
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }
    print(f"BFS from 'A': {bfs(graph, 'A')}")
    print(f"DFS from 'A': {dfs(graph, 'A')}")

    # Dynamic Programming
    print("\n--- DYNAMIC PROGRAMMING ---")
    print(f"Fibonacci(10): {fibonacci(10)}")
    print(f"LCS('ABCDGH', 'AEDFHR'): {longest_common_subsequence('ABCDGH', 'AEDFHR')}")

    # Mathematical
    print("\n--- MATHEMATICAL ALGORITHMS ---")
    print(f"GCD(48, 18): {gcd(48, 18)}")
    print(f"Is 17 prime? {is_prime(17)}")
    print(f"Primes up to 30: {sieve_of_eratosthenes(30)}")

    print("\n" + "=" * 60)
