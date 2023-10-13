# // This is a new dynamic programming problem. I have published a research paper
# // about this problem under the guidance of Professor Rao Li (University of
# // South Carolina, Aiken) along with my friend. The paper has been accepted by
# // the Journal of Mathematics and Informatics.The problem is a variation of the
# // standard longest common subsequence problem. It says that--> "Suppose there
# // are two strings, X and Y. Now we need to find the longest string, which is a
# // subsequence of X and a substring of Y."

# // Link of the paper--> http://www.researchmathsci.org/JMIart/JMI-v25-8.pdf


class LCSubseqSubstr:
    @staticmethod
    def lcss(x, y, m, n, w):
        maxlength = 0  # keeps the max length of LCSS
        lastindexony = n  # keeps the last index of LCSS in Y
        w = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if x[i - 1] == y[j - 1]:
                    w[i][j] = w[i - 1][j - 1] + 1
                else:
                    w[i][j] = w[i - 1][j]
                if w[i][j] > maxlength:
                    maxlength = w[i][j]
                    lastindexony = j

        return y[lastindexony - maxlength : lastindexony]


if __name__ == "__main__":
    x = input("Input the first string: ")
    y = input("Input the second string: ")

    m, n = len(x), len(y)
    w1 = [[0] * (n + 1) for _ in range(m + 1)]

    lcs_res = LCSubseqSubstr.lcss(x, y, m, n, w1)

    print(f"longest string that is subsequence of {x} and substring of {y} {lcs_res}")
    print(f"The length is {len(lcs_res)}")
