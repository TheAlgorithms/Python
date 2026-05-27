"""
evaluate-reverse-polish-notation

Problem statement:
Array of tokens that represents an arithmetic expression in Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Constraints:

1 <= tokens.length <= 104
tokens[i] is an operator: "+", "-", "*", or "/".
Or an integer in the range [-200, 200].
"""


class Solution:
    def eval_rpn(self, tokens: list[str]) -> int:
        """
        Function to evaluate the reverse polish notation
        :param tokens: List of strings
        :return: int

        Time complexity: O(n)
        Space complexity: O(n)

        Example:
        >>> s = Solution()
        >>> s.eval_rpn(["2","1","+","3","*"])
        9
        >>> s.eval_rpn(["4","13","5","/","+"])
        6
        """
        s = []
        for i in tokens:
            if i not in ["+", "-", "*", "/"]:
                s.append(int(i))
            else:
                b = s.pop()
                a = s.pop()
                if i == "+":
                    s.append(a + b)
                elif i == "-":
                    s.append(a - b)
                elif i == "*":
                    s.append(a * b)
                else:
                    ele = abs(a) // abs(b)
                    if a * b < 0:
                        ele = -1 * ele
                    s.append(ele)
        return s.pop()


if __name__ == "__main__":
    s = Solution()
    print(s.eval_rpn(["2", "1", "+", "3", "*"]))  # 9
    print(s.eval_rpn(["4", "13", "5", "/", "+"]))  # 6
    print(
        s.eval_rpn(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        )
    )  # 22
