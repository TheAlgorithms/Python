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
    def LCSS(X, Y, m, n, W):
        maxLength = 0    # keeps the max length of LCSS
        lastIndexOnY = n  # keeps the last index of LCSS in Y
        W = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if X[i - 1] == Y[j - 1]:
                    W[i][j] = W[i - 1][j - 1] + 1
                else:
                    W[i][j] = W[i - 1][j]
                if W[i][j] > maxLength:
                    maxLength = W[i][j]
                    lastIndexOnY = j

        return Y[lastIndexOnY - maxLength:lastIndexOnY]

if __name__ == "__main__":
    X = input("Input the first string: ")
    Y = input("Input the second string: ")

    m, n = len(X), len(Y)
    W1 = [[0] * (n + 1) for _ in range(m + 1)]

    lcss_result = LCSubseqSubstr.LCSS(X, Y, m, n, W1)

    print(f"The longest string which is a subsequence of {X} and a substring of {Y} is {lcss_result}")
    print(f"The length of the longest string which is a subsequence of {X} and a substring of {Y} is {len(lcss_result)}")
