"""
The nested brackets problem is a problem that determines if a sequence of
brackets are properly nested.  A sequence of brackets s is considered properly nested
if any of the following conditions are true:

        - s is empty
        - s has the form (U) or [U] or {U} where U is a properly nested string
        - s has the form VW where V and W are properly nested strings

For example, the string "()()[()]" is properly nested but "[(()]" is not.

The function called is_balanced takes as input a string S which is a sequence of
brackets and returns true if S is nested and false otherwise.
"""


def is_balanced(s):
    stack = []
    open_brackets = set({"(", "[", "{"})
    closed_brackets = set({")", "]", "}"})
    open_to_closed = {"{": "}", "[": "]", "(": ")"}

    for i in range(len(s)):
        if s[i] in open_brackets:
            stack.append(s[i])

        elif s[i] in closed_brackets and (
            len(stack) == 0 or (len(stack) > 0 and open_to_closed[stack.pop()] != s[i])
        ):
            return False

    return len(stack) == 0


def main():
    s = input("Enter sequence of brackets: ")
    if is_balanced(s):
        print(s, "is balanced")
    else:
        print(s, "is not balanced")


if __name__ == "__main__":
    main()
