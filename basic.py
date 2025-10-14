"""
The Algorithms - Python
A comprehensive collection of algorithms implemented in Python for educational purposes.
All implementations are designed for learning and may not be optimized for production use.
"""

import math
from typing import List, Optional, Tuple, Any
from collections import deque, defaultdict
import heapq


# ==================== SORTING ALGORITHMS ====================

def bubble_sort(arr: List[int]) -> List[int]:
    """
    Bubble Sort Algorithm
    Time Complexity: O(n²), Space Complexity: O(1)
    """
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


def quick_sort(arr: List[int]) -> List[int]:
    """
    Quick Sort Algorithm
    Time Complexity: O(n log n) average, O(n²) worst
    Space Complexity: O(log n)
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr: List[int]) -> List[int]:
    """
    Merge Sort Algorithm
    Time Complexity: O(n log n), Space Complexity: O(n)
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
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


def heap_sort(arr: List[int]) -> List[int]:
    """
    Heap Sort Algorithm
    Time Complexity: O(n log n), Space Complexity: O(1)
    """
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr


# ==================== SEARCHING ALGORITHMS ====================

def binary_search(arr: List[int], target: int) -> int:
    """
    Binary Search Algorithm (iterative)
    Time Complexity: O(log n), Space Complexity: O(1)
    Returns: index of target or -1 if not found
    """
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


def binary_search_recursive(arr: List[int], target: int, left: int = 0, right: int = None) -> int:
    """
    Binary Search Algorithm (recursive)
    Time Complexity: O(log n), Space Complexity: O(log n)
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def linear_search(arr: List[int], target: int) -> int:
    """
    Linear Search Algorithm
    Time Complexity: O(n), Space Complexity: O(1)
    """
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def jump_search(arr: List[int], target: int) -> int:
    """
    Jump Search Algorithm
    Time Complexity: O(√n), Space Complexity: O(1)
    """
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


# ==================== GRAPH ALGORITHMS ====================

class Graph:
    """Graph representation using adjacency list"""
    
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u: int, v: int):
        """Add an edge to the graph"""
        self.graph[u].append(v)
    
    def bfs(self, start: int) -> List[int]:
        """
        Breadth-First Search
        Time Complexity: O(V + E), Space Complexity: O(V)
        """
        visited = set()
        queue = deque([start])
        result = []
        
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend([v for v in self.graph[vertex] if v not in visited])
        
        return result
    
    def dfs(self, start: int) -> List[int]:
        """
        Depth-First Search (iterative)
        Time Complexity: O(V + E), Space Complexity: O(V)
        """
        visited = set()
        stack = [start]
        result = []
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                stack.extend(reversed(self.graph[vertex]))
        
        return result
    
    def dfs_recursive(self, start: int, visited: Optional[set] = None, result: Optional[List[int]] = None) -> List[int]:
        """
        Depth-First Search (recursive)
        Time Complexity: O(V + E), Space Complexity: O(V)
        """
        if visited is None:
            visited = set()
        if result is None:
            result = []
        
        visited.add(start)
        result.append(start)
        
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited, result)
        
        return result


def dijkstra(graph: dict, start: int) -> dict:
    """
    Dijkstra's Shortest Path Algorithm
    Time Complexity: O((V + E) log V)
    graph format: {node: [(neighbor, weight), ...]}
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current_dist > distances[current]:
            continue
        
        for neighbor, weight in graph.get(current, []):
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances


# ==================== DYNAMIC PROGRAMMING ====================

def fibonacci(n: int) -> int:
    """
    Fibonacci Number (Dynamic Programming)
    Time Complexity: O(n), Space Complexity: O(n)
    """
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


def fibonacci_optimized(n: int) -> int:
    """
    Fibonacci Number (Space Optimized)
    Time Complexity: O(n), Space Complexity: O(1)
    """
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b


def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    """
    0/1 Knapsack Problem
    Time Complexity: O(n * capacity), Space Complexity: O(n * capacity)
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]


def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Longest Common Subsequence
    Time Complexity: O(m * n), Space Complexity: O(m * n)
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]


def coin_change(coins: List[int], amount: int) -> int:
    """
    Coin Change Problem (minimum coins)
    Time Complexity: O(amount * len(coins))
    Returns: minimum coins needed or -1 if impossible
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


# ==================== STRING ALGORITHMS ====================

def is_palindrome(s: str) -> bool:
    """
    Check if string is palindrome
    Time Complexity: O(n), Space Complexity: O(1)
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True


def kmp_search(text: str, pattern: str) -> List[int]:
    """
    Knuth-Morris-Pratt Pattern Matching
    Time Complexity: O(n + m), Space Complexity: O(m)
    Returns: list of starting indices where pattern is found
    """
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
    
    if not pattern:
        return []
    
    lps = compute_lps(pattern)
    result = []
    i = j = 0
    
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == len(pattern):
            result.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return result


def longest_palindrome_substring(s: str) -> str:
    """
    Find longest palindromic substring
    Time Complexity: O(n²), Space Complexity: O(1)
    """
    if not s:
        return ""
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    start = end = 0
    
    for i in range(len(s)):
        len1 = expand_around_center(i, i)
        len2 = expand_around_center(i, i + 1)
        max_len = max(len1, len2)
        
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    
    return s[start:end + 1]


# ==================== MATHEMATICAL ALGORITHMS ====================

def gcd(a: int, b: int) -> int:
    """
    Greatest Common Divisor (Euclidean Algorithm)
    Time Complexity: O(log(min(a, b)))
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """
    Least Common Multiple
    Time Complexity: O(log(min(a, b)))
    """
    return abs(a * b) // gcd(a, b)


def is_prime(n: int) -> bool:
    """
    Prime Number Check
    Time Complexity: O(√n)
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True


def sieve_of_eratosthenes(n: int) -> List[int]:
    """
    Find all primes up to n
    Time Complexity: O(n log log n)
    """
    if n < 2:
        return []
    
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    return [i for i in range(n + 1) if is_prime[i]]


def power(base: int, exp: int, mod: int = None) -> int:
    """
    Fast Exponentiation (Binary Exponentiation)
    Time Complexity: O(log exp)
    """
    result = 1
    base = base % mod if mod else base
    
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod if mod else result * base
        exp = exp >> 1
        base = (base * base) % mod if mod else base * base
    
    return result


# ==================== DATA STRUCTURES ====================

class Stack:
    """Stack implementation using list"""
    
    def __init__(self):
        self.items = []
    
    def push(self, item: Any):
        self.items.append(item)
    
    def pop(self) -> Any:
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from empty stack")
    
    def peek(self) -> Any:
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Peek from empty stack")
    
    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    def size(self) -> int:
        return len(self.items)


class Queue:
    """Queue implementation using deque"""
    
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item: Any):
        self.items.append(item)
    
    def dequeue(self) -> Any:
        if not self.is_empty():
            return self.items.popleft()
        raise IndexError("Dequeue from empty queue")
    
    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    def size(self) -> int:
        return len(self.items)


# ==================== DEMO USAGE ====================

if __name__ == "__main__":
    print("=" * 50)
    print("THE ALGORITHMS - PYTHON DEMO")
    print("=" * 50)
    
    # Sorting Demo
    print("\n--- SORTING ALGORITHMS ---")
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {arr}")
    print(f"Bubble Sort: {bubble_sort(arr.copy())}")
    print(f"Quick Sort: {quick_sort(arr.copy())}")
    print(f"Merge Sort: {merge_sort(arr.copy())}")
    
    # Searching Demo
    print("\n--- SEARCHING ALGORITHMS ---")
    sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    print(f"Array: {sorted_arr}, Target: {target}")
    print(f"Binary Search: Index {binary_search(sorted_arr, target)}")
    
    # Dynamic Programming Demo
    print("\n--- DYNAMIC PROGRAMMING ---")
    print(f"Fibonacci(10): {fibonacci(10)}")
    print(f"LCS('ABCDGH', 'AEDFHR'): {longest_common_subsequence('ABCDGH', 'AEDFHR')}")
    
    # Math Demo
    print("\n--- MATHEMATICAL ALGORITHMS ---")
    print(f"GCD(48, 18): {gcd(48, 18)}")
    print(f"Is 17 prime? {is_prime(17)}")
    print(f"Primes up to 30: {sieve_of_eratosthenes(30)}")
    
    print("\n" + "=" * 50)
    print("Implementations complete! Visit TheAlgorithms/Python on GitHub for more!")
    print("=" * 50)
