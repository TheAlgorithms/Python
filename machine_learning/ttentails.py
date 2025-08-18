"""
TT-ENTAILS Algorithm (Propositional Logic)
Reference: [Russell & Norvig, Artificial Intelligence: A Modern Approach, Ch. 7](https://aima.cs.berkeley.edu/)
Wikipedia: [Entailment](https://en.wikipedia.org/wiki/Entailment)

This algorithm checks if a knowledge base (KB) entails a query sentence (a)
using truth tables. Returns True if KB entails a, False otherwise.
"""

import itertools
import ast
import operator

OPS = {
    ast.And: operator.and_,
    ast.Or: operator.or_,
    ast.Not: operator.not_
}

def safe_eval(expr: str, model: dict[str, bool]) -> bool:
    """Safely evaluate propositional logic expression using ast."""
    tree = ast.parse(expr, mode="eval")

    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.Name):
            return model[node.id]
        if isinstance(node, ast.Constant):  # True / False
            return node.value
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
            return OPS[ast.Not](_eval(node.operand))
        if isinstance(node, ast.BoolOp):
            if isinstance(node.op, ast.And):
                return all(_eval(v) for v in node.values)
            if isinstance(node.op, ast.Or):
                return any(_eval(v) for v in node.values)
        raise ValueError(f"Unsupported expression: {expr}")

    return _eval(tree)

def tt_entails(kb: list[str], query: str, symbols: list[str]) -> bool:
    """
    Check if the knowledge base entails the query using truth tables.

    Args:
        kb (List[str]): List of propositional sentences in KB as strings
        query (str): Query sentence to test entailment
        symbols (List[str]): List of all propositional symbols used

    Returns:
        bool: True if KB entails query, False otherwise

    Example:
        tt_entails(["P or Q"], "Q", ["P","Q"])

    """
    for values in itertools.product([True, False], repeat=len(symbols)):
        model: dict[str, bool] = dict(zip(symbols, values))
        # Check if KB is true under this model
        # # If query is false in this model, KB does not entail query
        if all(safe_eval(sentence, model) for sentence in kb) and not safe_eval(query, model):
            return False
    return True


# Example usage
if __name__ == "__main__":
    # Example 1: KB entails query → should return True
    symbols = ["P", "Q"]
    kb = ["P or Q", "not P or Q"]  # KB says P or Q is True, and not P or Q is True
    query = "Q"  # Query: Is Q True?
    print("Does KB entail query? : ", tt_entails(kb, query, symbols))

    # Example 2: KB does NOT entail query → should return False
    symbols2 = ["P", "Q"]
    kb2 = ["P"]  # KB says only P is True
    query2 = "Q"  # Query asks if Q is True
    print("Does KB2 entail query2? : ", tt_entails(kb2, query2, symbols2))
