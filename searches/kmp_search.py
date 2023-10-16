# The Knuth-Morris-Pratt (KMP) algorithm is a string searching and pattern matching algorithm.
# It efficiently identifies the occurrences of a given pattern within a longer text or string.
class KMPSearch:
    def KMPSearch(self, pat, txt):
        M = len(pat)
        N = len(txt)

        lps = [0] * M
        j = 0

        self.computeLPSArray(pat, M, lps)

        i = 0
        while (N - i) >= (M - j):
            if pat[j] == txt[i]:
                j += 1
                i += 1
            if j == M:
                print("Found pattern at index", (i - j))
                index = (i - j)
                j = lps[j - 1]
                return index
            elif i < N and pat[j] != txt[i:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i = i + 1
        print("No pattern found")
        return -1

    def computeLPSArray(self, pat, M, lps):
        len = 0
        i = 1
        lps[0] = 0

        while i < M:
            if pat[i] == pat[len]:
                len += 1
                lps[i] = len
                i += 1
            else:
                if len != 0:
                    len = lps[len - 1]
                else:
                    lps[i] = len
                    i += 1
