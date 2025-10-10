from collections import Counter

def are_anagrams(s1, s2):
    return Counter(s1) == Counter(s2)

# Example
print("Anagram:", are_anagrams("listen", "silent"))
