# Function to check if a string is palindrome
def is_palindrome(s):
    return s == s[::-1]

# Backtracking function to find all palindrome partitions
def partition_helper(s, path, result):
    # Base case: if string is empty, add the current path to result
    if not s:
        result.append(path)
        return
    
    # Explore all possible partitions
    for i in range(1, len(s) + 1):
        prefix = s[:i]
        
        # If prefix is palindrome, recurse for the remaining string
        if is_palindrome(prefix):
            partition_helper(s[i:], path + [prefix], result)

# Main function
def palindrome_partitioning(s):
    result = []
    partition_helper(s, [], result)
    return result

# Example usage
string = "aab"
print("All possible palindrome partitions of:", string)
partitions = palindrome_partitioning(string)
for p in partitions:
    print(p)
