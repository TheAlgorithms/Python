try:
    from .stack import Stack
except Exception:  # pragma: no cover - fallback for direct script execution / doctest
    # When this module is executed directly (for example via `python -m doctest`),
    # package-relative imports like `from .stack import Stack` may fail because
    # there's no package context. Load the sibling `stack.py` file directly as a
    # module so the functions here still work when run from the filesystem.
    import importlib.util
    import sys
    from pathlib import Path

    stack_path = Path(__file__).with_name("stack.py")
    spec = importlib.util.spec_from_file_location("data_structures.stacks.stack", str(stack_path))
    _stack = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = _stack
    spec.loader.exec_module(_stack)  # type: ignore[attr-defined]
    Stack = _stack.Stack


def balanced_parentheses(parentheses: str) -> bool:
    """Use a stack to check if a string of parentheses is balanced.
    >>> balanced_parentheses("([]{})")
    True
    >>> balanced_parentheses("[()]{}{[()()]()}")
    True
    >>> balanced_parentheses("[(])")
    False
    >>> balanced_parentheses("1+2*3-4")
    True
    >>> balanced_parentheses("")
    True
    """
    stack: Stack[str] = Stack()
    bracket_pairs = {"(": ")", "[": "]", "{": "}"}
    for bracket in parentheses:
        if bracket in bracket_pairs:
            stack.push(bracket)
        elif bracket in (")", "]", "}") and (
            stack.is_empty() or bracket_pairs[stack.pop()] != bracket
        ):
            return False
    return stack.is_empty()


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    examples = ["((()))", "((())", "(()))"]
    print("Balanced parentheses demonstration:\n")
    for example in examples:
        not_str = "" if balanced_parentheses(example) else "not "
        print(f"{example} is {not_str}balanced")
