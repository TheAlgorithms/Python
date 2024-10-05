from collections import Counter


class Solution:
    def check_inclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n2 < n1:
            return False
        freq1, freq2 = Counter(s1), Counter(s2[0:n1])
        if freq1 == freq2:
            return True
        left, right = 1, n1
        while right < n2:
            freq2[s2[left - 1]] -= 1
            if freq2[s2[left - 1]] == 0:
                del freq2[s2[left - 1]]  # Remove characters with zero frequency
            freq2[s2[right]] += 1
            if freq1 == freq2:
                return True
            right += 1
            left += 1
        return False


# Test the function
if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"

    sol = Solution()
    result = sol.check_inclusion(s1, s2)
    print(result)  # Should return True or False based on the input strings
