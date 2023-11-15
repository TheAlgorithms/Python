# Question:

# Given an m x n board of characters and a list of strings words, return all words on the board.
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

# Example 1:
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]

# Example 2:
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
 
# Constraints:
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 104
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.

# Solution:

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(node, i, j):
            char = board[i][j]
            curr_node = node.children.get(char)
            
            if not curr_node:
                return
            
            if curr_node.word:
                result.append(curr_node.word)
                curr_node.word = None  # Avoid duplicates
            
            board[i][j] = "#"  # Mark the cell as visited
            
            # Explore adjacent cells
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != "#":
                    dfs(curr_node, ni, nj)
            
            board[i][j] = char  # Restore the cell
    
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        result = []
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                dfs(trie.root, i, j)
        
        return result

# Example usage:
solution = Solution()
board1 = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words1 = ["oath","pea","eat","rain"]
print(solution.findWords(board1, words1))  # Output: ["eat", "oath"]

board2 = [["a","b"],["c","d"]]
words2 = ["abcb"]
print(solution.findWords(board2, words2))  # Output: []

# Explaination



# ### Trie (Tree-like data structure):
# - Imagine a dictionary where you can efficiently look up words. This is what the Trie helps us achieve.
# - It's like building a tree structure where each node represents a character, and you can follow the path from the root to a node to spell a word.

# ### Depth-First Search (DFS):
# - Think of it like exploring a maze or a grid.
# - Start at a position on the board, move to neighboring positions, and keep exploring until you reach the end or a dead-end.
# - If you find a word along the way, record it.

# ### Solution Steps:
# 1. **Build a Trie from the list of words:**
#    - For each word, create a path in the Trie. Each node along the path represents a character in the word.

# 2. **Explore the Board using DFS:**
#    - Start from each cell on the board.
#    - For each cell, check if there's a word in the Trie that starts with the letter at that cell.
#    - If yes, start DFS to explore the neighboring cells and form words.

# 3. **Mark Visited Cells:**
#    - Mark cells as visited during DFS to avoid reusing the same letter in a word.

# 4. **Record Found Words:**
#    - When you reach the end of a word during DFS, record it.

# 5. **Return the List of Found Words:**
#    - Provide the list of words found on the board.



# This algorithm efficiently searches for words on the board using a Trie and DFS, making it a good solution for the problem.
